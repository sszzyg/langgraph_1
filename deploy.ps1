# LangGraph + Chroma 部署脚本 (Windows PowerShell)

Write-Host "======================================" -ForegroundColor Green
Write-Host "LangGraph + Chroma 一键部署脚本" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green

# 检查 Docker
$dockerCheck = docker --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker 未安装或未启动" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Docker 已安装: $dockerCheck" -ForegroundColor Green

# 检查 Docker Compose
$composeCheck = docker compose version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker Compose 未安装" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Docker Compose 已安装: $composeCheck" -ForegroundColor Green

# 检查 .env 文件
if (-not (Test-Path ".env")) {
    Write-Host "⚠️  .env 文件不存在，复制 .env.server 模板" -ForegroundColor Yellow
    Copy-Item ".env.server" ".env"
    Write-Host "⚠️  请编辑 .env 文件，填入你的 Dify API Key" -ForegroundColor Yellow
    Write-Host "   编辑命令: code .env" -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ .env 文件已存在" -ForegroundColor Green

# 创建数据目录
if (-not (Test-Path "chroma_data")) {
    New-Item -ItemType Directory -Path "chroma_data" | Out-Null
}
if (-not (Test-Path "app\library")) {
    New-Item -ItemType Directory -Path "app\library" | Out-Null
}
Write-Host "✅ 目录已准备" -ForegroundColor Green

# 启动容器
Write-Host ""
Write-Host "启动 Docker 容器..." -ForegroundColor Cyan
docker compose -f docker-compose.prod.yml up -d

Write-Host ""
Write-Host "======================================" -ForegroundColor Green
Write-Host "✅ 部署完成！" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host ""
Write-Host "📝 服务地址:" -ForegroundColor Cyan
Write-Host "   API:       http://your-server-ip:8000"
Write-Host "   API Docs:  http://your-server-ip:8000/docs"
Write-Host "   Chroma:    http://your-server-ip:8001"
Write-Host ""
Write-Host "🔍 查看日志:" -ForegroundColor Cyan
Write-Host "   docker compose -f docker-compose.prod.yml logs -f api"
Write-Host ""
Write-Host "🛑 停止服务:" -ForegroundColor Cyan
Write-Host "   docker compose -f docker-compose.prod.yml down"
Write-Host ""
