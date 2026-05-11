# 阿里云服务器部署指南

## 前置要求

- 阿里云 ECS 实例（4 核 8GB，Ubuntu 22.04 LTS）
- Docker 社区版已安装
- 项目已上传到服务器（Git Clone 或 SCP）
- Dify API Key

## 快速部署（5 分钟）

### 1. 登录服务器

```bash
ssh root@your-server-ip
cd /opt/langraph  # 或你的项目目录
```

### 2. 配置环境变量

```bash
cp .env.server .env
nano .env
# 编辑以下字段：
# DIFY_BASE_URL=https://api.dify.ai
# DIFY_API_KEY=app-xxxxxxxxxxxxxxxx
# 按 Ctrl+O 保存，Ctrl+X 退出
```

### 3. 启动容器

```bash
docker compose -f docker-compose.prod.yml up -d
```

### 4. 验证服务

```bash
# 检查容器状态
docker compose -f docker-compose.prod.yml ps

# 查看日志（实时）
docker compose -f docker-compose.prod.yml logs -f api

# 测试 API
curl http://localhost:8000/health
# 应该返回: {"status":"ok"}
```

### 5. 测试知识库检索

```bash
curl -X POST http://localhost:8000/v1/tools/langgraph/run \
  -H "Content-Type: application/json" \
  -d '{
    "query": "请总结 NCAP low speed collisions 的测试条件",
    "strategy": "kb"
  }'
```

---

## 详细说明

### 容器结构

```
chroma         → Chroma 向量数据库（端口 8001，内部通信用 8000）
api            → FastAPI 应用（端口 8000）
```

### 目录映射

```
./app/library        → 知识库文档目录（只读挂载）
./chroma_data        → Chroma 持久化数据
```

### 环境变量说明

| 变量 | 含义 | 示例 |
|------|------|------|
| DIFY_BASE_URL | Dify API 服务地址 | https://api.dify.ai |
| DIFY_API_KEY | Dify 应用 API 密钥 | app-xxxx |
| CHROMA_HOST | Chroma 主机名（容器内通信） | chroma |
| CHROMA_PORT | Chroma HTTP 端口（容器内通信） | 8000 |

---

## 常见问题

### Q: 怎么添加新文档到知识库？

```bash
# 1. 将 Markdown 文件复制到 app/library
scp my_doc.md root@your-server-ip:/opt/langraph/app/library/

# 2. 重新入库
docker compose -f docker-compose.prod.yml exec api python -m app.index_library

# 3. 检查日志确认入库成功
docker compose -f docker-compose.prod.yml logs api
```

### Q: 怎么查看实时日志？

```bash
docker compose -f docker-compose.prod.yml logs -f api
```

### Q: 怎么重启服务？

```bash
docker compose -f docker-compose.prod.yml restart api
```

### Q: 怎么更新代码？

```bash
# 1. 拉取最新代码
git pull

# 2. 重新构建镜像
docker compose -f docker-compose.prod.yml build --no-cache api

# 3. 重启容器
docker compose -f docker-compose.prod.yml up -d
```

### Q: 容器崩溃了怎么办？

```bash
# 查看详细日志
docker compose -f docker-compose.prod.yml logs api --tail=50

# 重启所有服务
docker compose -f docker-compose.prod.yml restart
```

---

## 安全建议

### 1. 限制 API 访问

在服务器安全组中：
- 只允许你的 IP 访问 8000 和 8001 端口
- 生产环境建议配置 HTTPS + 反向代理

### 2. 配置 API Key

在 `.env` 中设置 `TOOL_API_KEY`，然后所有请求需要：

```bash
curl -H "X-API-Key: your-secret-key" \
  http://your-server-ip:8000/v1/tools/langgraph/run
```

### 3. 定期备份

```bash
# 备份 Chroma 数据
tar -czf chroma_backup_$(date +%Y%m%d).tar.gz chroma_data/

# 上传到阿里云 OSS
aliyun oss cp chroma_backup_*.tar.gz oss://your-bucket/backups/
```

---

## 监控 & 告警

### 检查容器资源使用

```bash
docker stats
```

### 设置自动重启

容器已配置 `restart: unless-stopped`，Docker 会自动重启崩溃的容器。

---

## 性能优化

### 1. 调整 Chroma 索引参数

编辑 `.env`：
```
CHROMA_CHUNK_SIZE=800      # 增加块大小（更少块，检索快）
CHROMA_CHUNK_OVERLAP=150   # 增加重叠（上下文更多）
CHROMA_TOP_K=6             # 增加返回结果数（召回率更高）
```

### 2. 增加 API 并发

编辑 `docker-compose.prod.yml`，API 服务增加：
```yaml
environment:
  - WORKERS=4
```

---

## 故障排查

| 症状 | 原因 | 解决方案 |
|------|------|---------|
| 连接超时 | Chroma 未启动 | `docker compose -f docker-compose.prod.yml up -d` |
| API 返回 401 | Dify API Key 错误 | 检查 `.env` 中的 `DIFY_API_KEY` |
| 知识库为空 | 未执行入库 | `docker compose -f docker-compose.prod.yml exec api python -m app.index_library` |
| 内存不足 | 容器内存限制 | 增加 EC S 内存或优化模型 |

---

## 如需帮助

在服务器上收集调试信息：

```bash
# 保存所有日志
docker compose -f docker-compose.prod.yml logs > debug.log 2>&1

# 导出容器配置
docker compose -f docker-compose.prod.yml config > config.yml

# 检查网络连接
docker compose -f docker-compose.prod.yml exec api curl http://chroma:8000/api/v1
```
