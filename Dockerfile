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

# 設定預設端口
ENV PORT 8080

# 開放應用程式端口
EXPOSE 8080

# 啟動應用程式
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080"]
