const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
const port = 3000;

// Middleware
app.use(cors({
  origin: 'http://localhost:3000',
  methods: ['GET', 'POST'],
}));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'LocalStorage')));

// Log all incoming requests
app.use((req, res, next) => {
  console.log(`Incoming request: ${req.method} ${req.url}`);
  res.on('finish', () => {
    console.log(`Response status: ${res.statusCode}`);
  });
  next();
});

// Endpoint to serve the main HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'LocalStorage', 'math_status.html'));
});

// Initialize SQLite database
const db = new sqlite3.Database('./progress.sqlite', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to SQLite database');
    // Create table with proper structure for math progress
    db.run(`CREATE TABLE IF NOT EXISTS progress (
      code TEXT PRIMARY KEY,
      name TEXT,
      time TEXT,
      status TEXT,
      note TEXT,
      completedDate TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);
    
    // Create trigger to update timestamp
    db.run(`CREATE TRIGGER IF NOT EXISTS update_progress_timestamp 
            AFTER UPDATE ON progress 
            BEGIN 
              UPDATE progress SET updated_at = CURRENT_TIMESTAMP WHERE code = NEW.code;
            END`);
  }
});

// Endpoint to save progress data
app.post('/save-progress', (req, res) => {
  const courses = req.body.courses;
  console.log('Progress data received for saving:', courses);
  
  if (!courses || !Array.isArray(courses)) {
    console.error('No courses data provided');
    return res.status(400).json({ error: 'No courses data provided' });
  }

  // Use transaction for batch insert/update
  db.serialize(() => {
    db.run('BEGIN TRANSACTION');
    
    const stmt = db.prepare(`
      INSERT OR REPLACE INTO progress (code, name, time, status, note, completedDate) 
      VALUES (?, ?, ?, ?, ?, ?)
    `);
    
    let errorOccurred = false;
    let processedCount = 0;
    
    courses.forEach(course => {
      stmt.run([course.code, course.name, course.time, course.status, course.note, course.completedDate], function(err) {
        if (err) {
          console.error('Error saving course:', course.code, err.message);
          errorOccurred = true;
        } else {
          processedCount++;
        }
      });
    });
    
    stmt.finalize((err) => {
      if (err || errorOccurred) {
        db.run('ROLLBACK');
        console.error('Transaction rolled back due to errors');
        return res.status(500).json({ error: 'Failed to save progress data' });
      } else {
        db.run('COMMIT');
        console.log(`Successfully saved ${processedCount} courses`);
        res.status(200).json({ 
          success: true, 
          message: `Saved ${processedCount} courses`,
          count: processedCount 
        });
      }
    });
  });
});

// Legacy endpoint for compatibility
app.post('/save', (req, res) => {
  const { data } = req.body;
  console.log('Legacy data save request:', data);
  
  if (!data) {
    return res.status(400).json({ error: 'No data provided' });
  }
  
  // Store as JSON in a separate table for legacy support
  db.run(`CREATE TABLE IF NOT EXISTS legacy_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);
  
  db.run('INSERT INTO legacy_data (data) VALUES (?)', [data], function (err) {
    if (err) {
      console.error('Error inserting legacy data:', err.message);
      return res.status(500).json({ error: 'Failed to save data' });
    }
    console.log('Legacy data saved with ID:', this.lastID);
    res.status(200).json({ id: this.lastID });
  });
});

// Endpoint to fetch progress data
app.get('/progress', (req, res) => {
  db.all('SELECT * FROM progress ORDER BY code', [], (err, rows) => {
    if (err) {
      console.error('Error fetching progress:', err.message);
      return res.status(500).json({ error: 'Failed to fetch progress data' });
    }
    console.log(`Fetched ${rows.length} progress records`);
    res.status(200).json({
      success: true,
      data: rows,
      count: rows.length,
      timestamp: new Date().toISOString()
    });
  });
});

// Legacy endpoint for compatibility
app.get('/data', (req, res) => {
  // First try to get legacy data
  db.all('SELECT * FROM legacy_data ORDER BY id DESC', [], (err, legacyRows) => {
    if (err) {
      console.log('No legacy data table, fetching progress data instead');
      // Fallback to progress data
      db.all('SELECT * FROM progress ORDER BY code', [], (err, rows) => {
        if (err) {
          console.error('Error fetching data:', err.message);
          return res.status(500).json({ error: 'Failed to fetch data' });
        }
        res.status(200).json(rows);
      });
    } else {
      res.status(200).json(legacyRows);
    }
  });
});

// Endpoint to get progress statistics
app.get('/stats', (req, res) => {
  const statsQueries = {
    total: 'SELECT COUNT(*) as count FROM progress',
    completed: "SELECT COUNT(*) as count FROM progress WHERE status = '已完成'",
    inProgress: "SELECT COUNT(*) as count FROM progress WHERE status = '進行中'",
    notStarted: "SELECT COUNT(*) as count FROM progress WHERE status = '未開始'"
  };
  
  const stats = {};
  let queriesCompleted = 0;
  const totalQueries = Object.keys(statsQueries).length;
  
  Object.entries(statsQueries).forEach(([key, query]) => {
    db.get(query, [], (err, row) => {
      if (err) {
        console.error(`Error fetching ${key} stats:`, err.message);
        stats[key] = 0;
      } else {
        stats[key] = row.count;
      }
      
      queriesCompleted++;
      if (queriesCompleted === totalQueries) {
        const completionRate = stats.total > 0 ? ((stats.completed / stats.total) * 100).toFixed(1) : 0;
        res.status(200).json({
          ...stats,
          completionRate: parseFloat(completionRate),
          timestamp: new Date().toISOString()
        });
      }
    });
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
