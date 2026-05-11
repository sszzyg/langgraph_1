#!/bin/bash
set -e

echo "======================================"
echo "LangGraph + Chroma 一键部署脚本"
echo "======================================"

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装"
    exit 1
fi

echo "✅ Docker 已安装"

# 检查 Docker Compose
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose 未安装"
    exit 1
fi

echo "✅ Docker Compose 已安装"

# 检查 .env 文件
if [ ! -f ".env" ]; then
    echo "⚠️  .env 文件不存在，复制 .env.server 模板"
    cp .env.server .env
    echo "⚠️  请编辑 .env 文件，填入你的 Dify API Key"
    echo "   编辑命令: nano .env"
    exit 1
fi

echo "✅ .env 文件已存在"

# 创建数据目录
mkdir -p chroma_data
mkdir -p app/library

echo "✅ 目录已准备"

# 启动容器
echo ""
echo "启动 Docker 容器..."
docker compose -f docker-compose.prod.yml up -d

echo ""
echo "======================================"
echo "✅ 部署完成！"
echo "======================================"
echo ""
echo "📝 服务地址："
echo "   API:       http://your-server-ip:8000"
echo "   API Docs:  http://your-server-ip:8000/docs"
echo "   Chroma:    http://your-server-ip:8001"
echo ""
echo "🔍 查看日志："
echo "   docker compose -f docker-compose.prod.yml logs -f api"
echo ""
echo "🛑 停止服务："
echo "   docker compose -f docker-compose.prod.yml down"
echo ""
