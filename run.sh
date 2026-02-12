#!/bin/bash

# Facebook Ads Creative Manager - Startup Script

echo "🎨 Facebook 广告创意管理系统"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安装"
    exit 1
fi

# Check if streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "📦 安装依赖..."
    pip install -r requirements.txt
fi

echo "✅ 所有依赖已就绪"
echo ""
echo "🚀 启动应用..."
echo ""
echo "应用将在以下地址运行："
echo "  Local URL: http://localhost:8501"
echo ""
echo "按 Ctrl+C 停止应用"
echo ""

streamlit run app.py
