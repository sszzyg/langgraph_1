FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

# 复制依赖文件并安装
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt -i https://pypi.org/simple || \
	pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目代码
COPY . .

# 初始化知识库（如果还未初始化）
RUN python -c "from app.faiss_kb import FAISSKnowledgeBase; kb = FAISSKnowledgeBase(); kb.index_library()" || true
