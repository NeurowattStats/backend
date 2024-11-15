# 使用 Python 3.11 作為基礎映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 安裝 git
RUN apt-get update && apt-get install -y git && apt-get clean

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY . .

# 拉取外部依賴 package（使用 Personal Access Token）
ARG GITHUB_TOKEN
RUN cd utils && git clone https://$GITHUB_TOKEN@github.com/NeurowattStats/NeuroStats_API.git

# 設定預設端口
ENV PORT 9090

# 開放應用程式端口
EXPOSE 9090

# 啟動應用程式
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
