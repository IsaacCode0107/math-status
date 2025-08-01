#!/bin/bash

# 數學課程進度追蹤 - 一鍵啟動腳本
echo "🚀 啟動數學課程進度追蹤系統..."

# 取得腳本所在目錄
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 切換到專案目錄
cd "$DIR"

# 檢查是否存在獨立版本
if [ -f "math_status_standalone.html" ]; then
    echo "✅ 找到獨立版本，直接開啟..."
    open "math_status_standalone.html"
    echo "🎉 系統已啟動！無需等待伺服器。"
    echo "📁 資料會自動保存到瀏覽器本地存儲"
    echo "🔄 重開機後資料依然存在"
else
    echo "⚠️  獨立版本不存在，啟動伺服器版本..."
    
    # 檢查 Node.js 是否安裝
    if ! command -v node &> /dev/null; then
        echo "❌ 未安裝 Node.js！請先安裝 Node.js"
        echo "📥 下載位置: https://nodejs.org/"
        read -p "按 Enter 鍵結束..."
        exit 1
    fi
    
    # 檢查依賴是否安裝
    if [ ! -d "node_modules" ]; then
        echo "📦 正在安裝依賴套件..."
        npm install
    fi
    
    # 啟動伺服器
    echo "🌐 啟動伺服器..."
    node server.js &
    SERVER_PID=$!
    
    # 等待伺服器啟動
    sleep 3
    
    # 開啟瀏覽器
    echo "🖥️  開啟瀏覽器..."
    open "http://localhost:3000"
    
    echo ""
    echo "🎉 系統已啟動！"
    echo "📋 伺服器 PID: $SERVER_PID"
    echo "🌐 訪問地址: http://localhost:3000"
    echo "⏹️  要停止伺服器，請按 Ctrl+C 或關閉此視窗"
    
    # 等待用戶按下 Ctrl+C
    trap "echo ''; echo '⏹️  正在停止伺服器...'; kill $SERVER_PID 2>/dev/null; echo '✅ 伺服器已停止'; exit 0" SIGINT
    
    echo "⌨️  按 Ctrl+C 停止伺服器"
    wait $SERVER_PID
fi

echo ""
echo "👋 感謝使用數學課程進度追蹤系統！"