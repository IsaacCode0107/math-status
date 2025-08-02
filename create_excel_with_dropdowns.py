import csv
import json
from datetime import datetime

# 課程資料結構 - 按冊分組
course_data = {
    "第三冊": {
        "第一章 三角函數": [
            {"code": "1-1_主題1", "name": "弧度量(A+B版)", "time": "40:39", "status": "已完成", "note": "基礎概念"},
            {"code": "1-1_主題2", "name": "扇形弧長與面積(A+B版)", "time": "15:20", "status": "已完成", "note": "應用計算"},
            {"code": "1-1_主題3", "name": "三角函數的圖形(A+B版)", "time": "01:12:32", "status": "已完成", "note": "圖形分析"},
            {"code": "1-1_主題4", "name": "三角方程式(A+B版)", "time": "23:55", "status": "進行中", "note": "方程求解"},
            {"code": "1-1_主題5", "name": "三角不等式(A+B版)", "time": "14:26", "status": "未開始", "note": "不等式解法"},
            {"code": "1-1_主題6", "name": "三角函數的極值(A+B版)", "time": "03:37", "status": "未開始", "note": "極值問題"},
            {"code": "1-1_主題7", "name": "三角函數的應用(A+B版)", "time": "13:39", "status": "未開始", "note": "實際應用"},
            {"code": "1-2_主題1", "name": "和差角公式(A版)", "time": "01:19:38", "status": "未開始", "note": "公式推導"},
            {"code": "1-2_主題2", "name": "平方差(課外補充)(A版)", "time": "06:08", "status": "未開始", "note": "補充內容"},
            {"code": "1-2_主題3", "name": "正切的和差角(A版)", "time": "27:06", "status": "未開始", "note": "正切公式"},
            {"code": "1-2_主題4", "name": "二倍角(A版)", "time": "28:12", "status": "未開始", "note": "倍角公式"},
            {"code": "1-2_主題5", "name": "二倍角(A版)", "time": "21:51", "status": "未開始", "note": "延續內容"},
            {"code": "1-2_主題6", "name": "半角公式(A版)", "time": "26:03", "status": "未開始", "note": "半角推導"},
            {"code": "1-3_主題1", "name": "正餘弦的疊合(A版)", "time": "40:16", "status": "未開始", "note": "函數疊合"},
            {"code": "1-3_主題2", "name": "正餘弦疊合的極值(A版)", "time": "44:27", "status": "未開始", "note": "極值計算"},
            {"code": "1-3_主題3", "name": "正餘弦疊合的應用問題(A版)", "time": "28:05", "status": "未開始", "note": "應用題型"}
        ],
        "第二章 指數與對數函數": [
            {"code": "2-1_主題1", "name": "指數函數的圖形(A+B版)", "time": "42:24", "status": "未開始", "note": "圖形性質"},
            {"code": "2-1_主題2", "name": "指數比大小(A+B版)", "time": "09:01", "status": "未開始", "note": "大小比較"},
            {"code": "2-1_主題3", "name": "指數方程式與不等式(A+B版)", "time": "09:01", "status": "未開始", "note": "方程不等式"},
            {"code": "2-1_主題4", "name": "指數函數的極值(A+B版)", "time": "11:03", "status": "未開始", "note": "極值問題"},
            {"code": "2-1_主題5", "name": "指數函數的應用(A+B版)", "time": "08:15", "status": "未開始", "note": "實際應用"},
            {"code": "2-2_主題1", "name": "對數的定義(A+B版)", "time": "14:32", "status": "未開始", "note": "基本定義"},
            {"code": "2-2_主題2", "name": "對數律(A+B版)", "time": "01:04:23", "status": "未開始", "note": "對數運算律"},
            {"code": "2-2_主題3", "name": "對數方程(A+B版)", "time": "21:12", "status": "未開始", "note": "方程求解"},
            {"code": "2-2_主題4", "name": "科學記號與常用對數(A+B版)", "time": "24:07", "status": "未開始", "note": "科學應用"},
            {"code": "2-3_主題1", "name": "對數函數的圖形(A+B版)", "time": "44:59", "status": "未開始", "note": "圖形分析"},
            {"code": "2-3_主題2", "name": "對數比大小(A+B版)", "time": "12:06", "status": "未開始", "note": "大小比較"},
            {"code": "2-3_主題3", "name": "對數不等式(A+B版)", "time": "23:56", "status": "未開始", "note": "不等式解法"},
            {"code": "2-3_主題4", "name": "對數求極值(A+B版)", "time": "07:08", "status": "未開始", "note": "極值計算"},
            {"code": "2-3_主題5", "name": "對數應用問題(A+B版)", "time": "33:57", "status": "已完成", "note": "應用題型"}
        ],
        "第三章 平面向量": [
            {"code": "3-1_主題1", "name": "平面向量的幾何表示法(A+B版)", "time": "05:53", "status": "未開始", "note": "幾何表示"},
            {"code": "3-1_主題2", "name": "平面向量的座標表示法(A+B版)", "time": "14:51", "status": "未開始", "note": "座標表示"},
            {"code": "3-1_主題3", "name": "向量的運算(A+B版)", "time": "24:45", "status": "已完成", "note": "基本運算"},
            {"code": "3-1_主題4", "name": "向量的線性組合(A+B版)", "time": "28:52", "status": "未開始", "note": "線性組合"},
            {"code": "3-1_主題5", "name": "共線理論(A+B版)", "time": "35:00", "status": "未開始", "note": "共線性質"},
            {"code": "3-1_主題6", "name": "面積比(A+B版)", "time": "07:25", "status": "未開始", "note": "面積計算"},
            {"code": "3-1_主題7", "name": "斜座標(A+B版)", "time": "19:00", "status": "未開始", "note": "座標系統"},
            {"code": "3-2_主題1", "name": "內積(A+B版)", "time": "26:00", "status": "未開始", "note": "內積運算"},
            {"code": "3-2_主題2", "name": "內積的性質(A+B版)", "time": "14:19", "status": "未開始", "note": "性質探討"},
            {"code": "3-2_主題3", "name": "正射影(A+B版)", "time": "26:11", "status": "未開始", "note": "投影計算"},
            {"code": "3-2_主題4", "name": "直線參數式(A+B版)", "time": "27:25", "status": "未開始", "note": "參數方程"},
            {"code": "3-2_主題5", "name": "直線的夾角(A+B版)", "time": "10:36", "status": "未開始", "note": "角度計算"},
            {"code": "3-2_主題6", "name": "柯西不等式(A版)", "time": "26:59", "status": "未開始", "note": "不等式理論"},
            {"code": "3-3_主題1", "name": "向量的面積公式(A版)", "time": "18:09", "status": "未開始", "note": "面積公式"},
            {"code": "3-3_主題2", "name": "二階行列式(A版)", "time": "29:15", "status": "未開始", "note": "行列式計算"},
            {"code": "3-3_主題3", "name": "克拉瑪公式(A版)", "time": "12:17", "status": "未開始", "note": "線性方程組"},
            {"code": "3-3_主題4", "name": "二元一次方程組的向量觀點(A版)", "time": "12:02", "status": "未開始", "note": "向量觀點"}
        ]
    },
    "第四冊": {
        "第一章 空間向量": [
            {"code": "1-1_主題1", "name": "空間概念(A+B版)", "time": "23:07", "status": "未開始", "note": "基礎概念"},
            {"code": "1-1_主題2", "name": "二面角(A+B版)", "time": "30:00", "status": "未開始", "note": "角度計算"},
            {"code": "1-1_主題3", "name": "立體圖形計算(A+B版)", "time": "14:50", "status": "未開始", "note": "立體幾何"},
            {"code": "1-2_主題1", "name": "空間坐標系(A+B版)", "time": "32:39", "status": "未開始", "note": "坐標系統"},
            {"code": "1-2_主題2", "name": "空間向量的表示法(A+B版)", "time": "25:52", "status": "未開始", "note": "向量表示"},
            {"code": "1-2_主題3", "name": "空間向量的線性組合(A+B版)", "time": "11:01", "status": "未開始", "note": "線性運算"},
            {"code": "1-3_主題1", "name": "空間向量的內積(A版)", "time": "21:25", "status": "未開始", "note": "內積計算"},
            {"code": "1-3_主題2", "name": "柯西不等式(A版)", "time": "21:58", "status": "未開始", "note": "不等式"},
            {"code": "1-4_主題1", "name": "外積(A版)", "time": "18:27", "status": "未開始", "note": "外積運算"},
            {"code": "補充", "name": "內積與外積比較", "time": "06:34", "status": "未開始", "note": "概念比較"},
            {"code": "1-4_主題2", "name": "空間向量求體積(A版)", "time": "04:57", "status": "未開始", "note": "體積計算"},
            {"code": "1-4_主題3", "name": "三階行列式(A版)", "time": "24:50", "status": "未開始", "note": "行列式"},
            {"code": "1-4_主題4", "name": "三階行列式的應用(A版)", "time": "12:44", "status": "未開始", "note": "應用計算"},
            {"code": "數B補充", "name": "如何判斷圓錐截痕", "time": "04:27", "status": "未開始", "note": "幾何判斷"},
            {"code": "數B補充", "name": "球面與經緯度", "time": "20:27", "status": "未開始", "note": "球面幾何"}
        ],
        "第二章 空間的平面與直線(A版)": [
            {"code": "2-1_主題1", "name": "平面方程式", "time": "24:59", "status": "未開始", "note": "方程建立"},
            {"code": "2-1_主題2", "name": "平面的截距式", "time": "18:42", "status": "未開始", "note": "截距表示"},
            {"code": "2-1_主題3", "name": "平面的夾角", "time": "09:30", "status": "未開始", "note": "角度計算"},
            {"code": "2-1_主題4", "name": "點到平面的距離", "time": "24:21", "status": "未開始", "note": "距離公式"},
            {"code": "2-2_主題1", "name": "直線方程式", "time": "37:02", "status": "未開始", "note": "方程建立"},
            {"code": "2-2_主題2", "name": "直線與平面", "time": "29:32", "status": "未開始", "note": "關係分析"},
            {"code": "2-2_主題3", "name": "點與直線", "time": "06:50", "status": "未開始", "note": "位置關係"},
            {"code": "2-2_主題4", "name": "直線與直線", "time": "39:55", "status": "未開始", "note": "線線關係"}
        ],
        "第三章 條件機率(A+B版)": [
            {"code": "3-1~3-2_主題1", "name": "條件機率", "time": "23:37", "status": "未開始", "note": "機率計算"},
            {"code": "3-2_主題2", "name": "獨立事件", "time": "30:05", "status": "未開始", "note": "事件獨立性"},
            {"code": "3-3_主題1", "name": "貝氏定理", "time": "27:36", "status": "未開始", "note": "定理應用"}
        ],
        "第四章 矩陣": [
            {"code": "4-1_主題1", "name": "高斯消去法(A版)", "time": "37:19", "status": "未開始", "note": "解方程組"},
            {"code": "4-2_主題1", "name": "矩陣的加減法(A+B版)", "time": "11:50", "status": "未開始", "note": "基本運算"},
            {"code": "4-2_主題2", "name": "矩陣的乘法(A+B版)", "time": "21:19", "status": "未開始", "note": "乘法運算"},
            {"code": "4-2_主題3", "name": "矩陣的高次方(A+B版)", "time": "24:19", "status": "未開始", "note": "冪次計算"},
            {"code": "4-2_主題4", "name": "反方陣(A+B版)", "time": "46:26", "status": "未開始", "note": "逆矩陣"},
            {"code": "4-3_主題1", "name": "轉移矩陣(A版)", "time": "38:11", "status": "未開始", "note": "狀態轉移"},
            {"code": "4-3_主題2~3", "name": "平面線性變換(A版)", "time": "10:19", "status": "未開始", "note": "幾何變換"},
            {"code": "4-3_主題4~5", "name": "伸縮與推移矩陣(A版)", "time": "13:58", "status": "未開始", "note": "變換矩陣"},
            {"code": "4-3_主題6", "name": "鏡射矩陣(A版)", "time": "12:17", "status": "未開始", "note": "對稱變換"},
            {"code": "4-3_主題7", "name": "旋轉矩陣(A版)", "time": "24:45", "status": "未開始", "note": "旋轉變換"}
        ]
    }
}

def time_to_minutes(time_str):
    """將時間字符串轉換為分鐘數"""
    parts = time_str.split(':')
    if len(parts) == 3:  # HH:MM:SS
        return int(parts[0]) * 60 + int(parts[1]) + int(parts[2]) / 60
    elif len(parts) == 2:  # MM:SS
        return int(parts[0]) + int(parts[1]) / 60
    return 0

def minutes_to_hours(minutes):
    """將分鐘數轉換為小時格式"""
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    return f"{hours}h{mins}m"

# 生成課程資料 CSV 檔案
filename = f"數學課程進度追蹤表_完整版_{datetime.now().strftime('%Y%m%d')}.csv"

all_courses = []
course_count = 0

# 準備所有課程資料
for volume, chapters in course_data.items():
    # 添加冊標題
    all_courses.append({
        '冊別': f"=== {volume} ===",
        '章節': '',
        '課程編號': '',
        '課程名稱': '',
        '時長': '',
        '狀態': '',
        '備註': '',
        '完成日期': ''
    })
    
    for chapter_name, courses in chapters.items():
        # 添加章節標題
        all_courses.append({
            '冊別': '',
            '章節': chapter_name,
            '課程編號': '',
            '課程名稱': '',
            '時長': '',
            '狀態': '',
            '備註': '',
            '完成日期': ''
        })
        
        # 添加課程資料
        for course in courses:
            course_count += 1
            all_courses.append({
                '冊別': '',
                '章節': '',
                '課程編號': course['code'],
                '課程名稱': course['name'],
                '時長': course['time'],
                '狀態': course['status'],
                '備註': course['note'],
                '完成日期': ''
            })

# 寫入主要課程資料
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['冊別', '章節', '課程編號', '課程名稱', '時長', '狀態', '備註', '完成日期']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(all_courses)

print(f"✅ 主要課程檔案已生成：{filename}")

# 生成各冊統計檔案
for volume, chapters in course_data.items():
    stats_filename = f"{volume}_統計表_{datetime.now().strftime('%Y%m%d')}.csv"
    
    stats_data = []
    
    # 總體統計
    stats_data.append({
        '項目': f"{volume} 總體統計",
        '數值': '',
        '公式': '',
        '說明': ''
    })
    
    total_courses = sum(len(courses) for courses in chapters.values())
    completed = sum(1 for courses in chapters.values() for course in courses if course['status'] == '已完成')
    in_progress = sum(1 for courses in chapters.values() for course in courses if course['status'] == '進行中')
    not_started = sum(1 for courses in chapters.values() for course in courses if course['status'] == '未開始')
    completion_rate = (completed / total_courses * 100) if total_courses > 0 else 0
    
    # 計算總時間
    total_minutes = sum(time_to_minutes(course['time']) for courses in chapters.values() for course in courses)
    completed_minutes = sum(time_to_minutes(course['time']) for courses in chapters.values() for course in courses if course['status'] == '已完成')
    remaining_minutes = total_minutes - completed_minutes
    
    stats_data.extend([
        {'項目': '總課程數', '數值': total_courses, '公式': f'=COUNTA(主要檔案.C:C)-{len(chapters)+1}', '說明': '計算課程編號欄位非空值'},
        {'項目': '已完成課程', '數值': completed, '公式': '=COUNTIF(主要檔案.F:F,"已完成")', '說明': '統計已完成的課程數'},
        {'項目': '進行中課程', '數值': in_progress, '公式': '=COUNTIF(主要檔案.F:F,"進行中")', '說明': '統計進行中的課程數'},
        {'項目': '未開始課程', '數值': not_started, '公式': '=COUNTIF(主要檔案.F:F,"未開始")', '說明': '統計未開始的課程數'},
        {'項目': '完成率', '數值': f'{completion_rate:.1f}%', '公式': '=ROUND(C3/C2*100,1)&"%"', '說明': '已完成課程/總課程數*100'},
        {'項目': '總學習時間', '數值': minutes_to_hours(total_minutes), '公式': '', '說明': '所有課程的總時長'},
        {'項目': '已學習時間', '數值': minutes_to_hours(completed_minutes), '公式': '', '說明': '已完成課程的總時長'},
        {'項目': '剩餘時間', '數值': minutes_to_hours(remaining_minutes), '公式': '', '說明': '未完成課程的總時長'},
        {'項目': '', '數值': '', '公式': '', '說明': ''},
    ])
    
    # 各章節統計
    stats_data.append({
        '項目': f"{volume} 各章節統計",
        '數值': '',
        '公式': '',
        '說明': ''
    })
    
    for chapter_name, courses in chapters.items():
        chapter_total = len(courses)
        chapter_completed = sum(1 for course in courses if course['status'] == '已完成')
        chapter_in_progress = sum(1 for course in courses if course['status'] == '進行中')
        chapter_not_started = sum(1 for course in courses if course['status'] == '未開始')
        chapter_completion_rate = (chapter_completed / chapter_total * 100) if chapter_total > 0 else 0
        chapter_minutes = sum(time_to_minutes(course['time']) for course in courses)
        
        stats_data.extend([
            {'項目': f'{chapter_name}', '數值': '', '公式': '', '說明': ''},
            {'項目': f'  總課程數', '數值': chapter_total, '公式': '', '說明': ''},
            {'項目': f'  已完成', '數值': chapter_completed, '公式': '', '說明': ''},
            {'項目': f'  進行中', '數值': chapter_in_progress, '公式': '', '說明': ''},
            {'項目': f'  未開始', '數值': chapter_not_started, '公式': '', '說明': ''},
            {'項目': f'  完成率', '數值': f'{chapter_completion_rate:.1f}%', '公式': '', '說明': ''},
            {'項目': f'  總時長', '數值': minutes_to_hours(chapter_minutes), '公式': '', '說明': ''},
            {'項目': '', '數值': '', '公式': '', '說明': ''},
        ])
    
    # 寫入統計檔案
    with open(stats_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['項目', '數值', '公式', '說明']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(stats_data)
    
    print(f"📊 {volume} 統計檔案已生成：{stats_filename}")

# 生成使用說明檔案
instructions_filename = f"Excel使用說明_{datetime.now().strftime('%Y%m%d')}.txt"
with open(instructions_filename, 'w', encoding='utf-8') as f:
    f.write("📋 Excel 課程進度追蹤系統使用說明\n")
    f.write("=" * 50 + "\n\n")
    
    f.write("📁 檔案說明：\n")
    f.write(f"1. {filename} - 主要課程進度追蹤檔案\n")
    for volume in course_data.keys():
        f.write(f"2. {volume}_統計表_*.csv - {volume}專用統計檔案\n")
    f.write("\n")
    
    f.write("🎯 在 Excel 中設定狀態下拉選單：\n")
    f.write("1. 開啟主要課程檔案\n")
    f.write("2. 選取「狀態」欄位 (F欄)\n")
    f.write("3. 前往 [資料] → [資料驗證]\n")
    f.write("4. 選擇 [清單]，來源輸入：未開始,進行中,已完成\n")
    f.write("5. 勾選 [顯示下拉式箭頭]\n")
    f.write("6. 點擊 [確定]\n\n")
    
    f.write("🎨 設定條件格式 (狀態顏色)：\n")
    f.write("1. 選取「狀態」欄位\n")
    f.write("2. 前往 [常用] → [設定格式化的條件] → [新增規則]\n")
    f.write("3. 選擇 [只格式化包含的儲存格]\n")
    f.write("4. 設定規則：\n")
    f.write("   - 儲存格值 = 已完成 → 綠色背景\n")
    f.write("   - 儲存格值 = 進行中 → 黃色背景\n")
    f.write("   - 儲存格值 = 未開始 → 紅色背景\n\n")
    
    f.write("📊 使用統計功能：\n")
    f.write("1. 開啟對應的統計檔案\n")
    f.write("2. 統計會顯示各項進度指標\n")
    f.write("3. 可以複製統計數據到主檔案中\n")
    f.write("4. 建議將統計表放在主檔案的另一個工作表\n\n")
    
    f.write("💡 實用公式：\n")
    f.write("- 總課程數：=COUNTA(C:C)-標題行數\n")
    f.write("- 已完成數：=COUNTIF(F:F,\"已完成\")\n")
    f.write("- 完成率：=COUNTIF(F:F,\"已完成\")/COUNTA(C:C)*100\n")
    f.write("- 進度條：可使用條件格式建立視覺化進度條\n\n")
    
    f.write("🔄 維護建議：\n")
    f.write("1. 定期更新完成日期\n")
    f.write("2. 在備註欄記錄學習心得\n")
    f.write("3. 可以增加「學習評分」欄位\n")
    f.write("4. 建議每週檢視一次進度\n")
    
print(f"📖 使用說明已生成：{instructions_filename}")

print(f"\n🎉 完成！共生成 {2 + len(course_data)} 個檔案：")
print(f"   📋 1個主要追蹤檔案")
print(f"   📊 {len(course_data)}個統計檔案")
print(f"   📖 1個使用說明檔案")
print(f"\n總計 {course_count} 門課程已整理完畢！")
