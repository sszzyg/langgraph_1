# 实例配置清单
# Dify Docker Compose 使用指南

## 1. 服务器选择建议

推荐阿里云 ECS，配置如下：
Ubuntu 22.04 64bit
- 镜像：Alibaba Cloud Linux 4 LTS 64bit 容器优化版，或 
- CPU：>= 4 vCPU
- 内存：>= 8 GB
- 系统盘：默认即可，建议不低于 40 GB
- 数据盘：默认即可，生产建议单独挂载
- 公网 IP：分配 IPv4
- 安全组：放行 22, 80, 443 端口

说明：
- 如果仅内网使用，可不开放 80/443 到全网，只对办公网段开放。
- 生产环境建议配置域名和 HTTPS。

## 2. 首次初始化服务器

登录服务器后建议先执行：

```bash
sudo apt update && sudo apt -y upgrade
sudo timedatectl set-timezone Asia/Shanghai
```

## 3. 安装 Docker 与 Compose 插件

Ubuntu 22.04 可用：

```bash
docker --version
docker compose version  # 确认是否支持 Compose V2

sudo apt update
sudo apt -y install ca-certificates curl gnupg lsb-release
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
	$(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker
docker --version
docker compose version
```

## 5. 情况 A：已安装，直接启动

进入你之前的 Dify compose 目录后执行：

```bash
cd dify
cd docker
docker compose up -d
docker compose ps
docker compose logs -f --tail=200
```

常用运维命令：

```bash
docker compose stop
docker compose start
docker compose restart
docker compose down
```

更新版本：

```bash
docker compose pull
docker compose up -d
```

## 6. 情况 B：未安装过，执行全新部署

示例流程：

```bash
cd /opt
sudo git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
docker compose ps
```

初始化后访问：
- http://你的服务器公网IP
- 你的当前服务器地址示例: http://8.136.154.82
# 怎么看公网ip？
 

如果配置了反向代理和证书，则使用 https://你的域名。

## 7. 快速健康检查

### 7.1 端口监听

```bash
sudo ss -lntp | grep -E ":80|:443"
```

### 7.2 容器健康状态

```bash
docker compose ps
```

### 7.3 关键日志

```bash
docker compose logs -f --tail=200
```

## 8. 备份建议

- 备份 .env 文件
- 备份数据库与持久化目录
- 升级前先快照系统盘或数据盘
