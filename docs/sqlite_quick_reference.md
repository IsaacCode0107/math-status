# 🚀 Math Status SQLite 快速測試參考

> **快速參考版本** | 完整版請見 `sqlite_testing_guide.md`

## ⚡ **快速啟動**

```bash
# 1. 啟動伺服器
cd /Users/hank/code/math
node server.js

# 2. 測試 API（新終端）
curl -X POST http://localhost:3000/save-progress \
  -H "Content-Type: application/json" \
  -d '{"courses":[{"code":"TEST","name":"測試","time":"10:00","status":"已完成","note":"測試","completedDate":"2024-08-01"}]}'

# 3. 檢查結果
curl http://localhost:3000/progress
```

## 📋 **核心測試命令**

### **API 測試**

```bash
# 寫入測試
curl -X POST localhost:3000/save-progress -H "Content-Type: application/json" -d '{"courses":[{"code":"T1","name":"測試","time":"10:00","status":"進行中"}]}'

# 讀取測試  
curl localhost:3000/progress

# 統計測試
curl localhost:3000/stats
```

### **資料庫驗證**

```bash
# 查看資料
sqlite3 progress.sqlite "SELECT * FROM progress;"

# 統計驗證
sqlite3 progress.sqlite "SELECT COUNT(*) as total FROM progress;"
```

## ✅ **成功指標**

| 測試 | 預期結果 |
|------|----------|
| **啟動** | `Connected to SQLite database` |
| **寫入** | `{"success":true,"count":1}` |
| **讀取** | JSON 格式資料陣列 |
| **統計** | `{"total":N,"completed":M}` |

## 🔧 **常見問題**

| 問題 | 解決方案 |
|------|----------|
| **模組找不到** | `npm install` |
| **端口被占用** | 更改 `server.js` 中的端口 |
| **權限錯誤** | `chmod 755 progress.sqlite` |

## 🎯 **測試檢查清單**

- [ ] 伺服器成功啟動
- [ ] API 寫入回傳 success:true
- [ ] API 讀取回傳資料陣列
- [ ] SQLite 直接查詢有資料
- [ ] 網頁 <http://localhost:3000> 可訪問
- [ ] 統計功能正常運作

**✅ 全部通過 = SQLite 功能正常！**
