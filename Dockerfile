# 使用 Python 3.8 作為基礎映像
FROM python:3.11.9-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY . .

# 設定預設端口（若未設置 PORT 環境變數，將使用 9090）
ENV PORT 9090

# 開放應用程式端口
EXPOSE ${PORT}

# 啟動應用程式，根據 PORT 環境變數設定埠號
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
