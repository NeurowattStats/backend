
# NeuroStats API

此專案提供金融數據查詢的 API 服務，包括公司財務資料、每股數據、財務比率、月營收數據等多項資訊，使用 [FastAPI](https://fastapi.tiangolo.com/) 開發。

## 快速開始

### 環境需求
- Python 3.8+
- FastAPI
- Uvicorn

### 安裝

1. 克隆本專案：

   ```bash
   git clone https://github.com/NeurowattStats/backend.git
   cd backend
   ```

2. 建立虛擬環境並安裝依賴項：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 venv\Scripts\activate
   pip install -r requirements.txt
   
   cd utils 
   git clone https://github.com/NeurowattStats/stock_price_revenue_crawler.git # 篩選 data package
   ```
   
3. 啟動 API 服務：

   首先，您可以在項目目錄下更改 `.env` 文件來動態設置主機和端口：

   ```plaintext
   HOST=0.0.0.0
   PORT=9090
   ```

   若 `.env` 中未設置主機和端口，預設將使用 `HOST=0.0.0.0` 和 `PORT=9090`。

   然後啟動服務：

   ```bash
   uvicorn main:app
   ```

   API 將根據 `.env` 文件中的配置在相應的主機和端口運行，默認情況下為 `http://0.0.0.0:9090`。

## API 路由

以下是可用的 API 路徑及其使用說明。

### Fundamental 路由

| 路徑                                  | 方法  | 描述                     |
|---------------------------------------|-------|--------------------------|
| `/neurostats/fundamental/vitals/finance_data` | POST  | 財務分析-重要指標-財務概況  |
| `/neurostats/fundamental/vitals/per_share`    | POST  | 財務分析-重要指標-每股財務狀況   |
| `/neurostats/fundamental/vitals/ratios`       | POST  | 財務分析-重要指標-獲利能力  |
| `/neurostats/fundamental/revenue/monthly`     | POST  | 財務分析-每月營收-採用IFRSs   |
| `/neurostats/fundamental/revenue/this_month`  | POST  | 財務分析-每月營收-單月營收       |
| `/neurostats/fundamental/revenue/this_month_text` | POST | 財務分析-每月營收-單月營收解析  |

### Valuation 路由

| 路徑                                  | 方法  | 描述                     |
|---------------------------------------|-------|--------------------------|
| `/neurostats/valuation/overview`      | POST  | 價值投資-市場評價-過去4季總攬 |
| `/neurostats/valuation/table`         | POST  | 價值投資-市場評價-過去10年表格 |

### API 使用範例

所有請求皆需提交 `ticker` 參數，以下是一些範例：
ticker 限定為 str, ex: "2330"

#### 取得公司財務數據

**請求**
```javascript
fetch("http://0.0.0.0:9090/neurostats/fundamental/vitals/finance_data", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ ticker: "2330" })
})
.then(response => response.json())
.then(data => {
    console.log("Finance Data:", data);
})
.catch(error => {
    console.error("Error fetching finance data:", error);
});
```

**請求**
```bash
curl -X POST "http://0.0.0.0:9090/neurostats/fundamental/vitals/finance_data" -H "Content-Type: application/json" -d '{"ticker": "2330"}'
```

**回應**
```json
{
  "quarter": "2024 Q2",
  "unit": "thousand NTD",
  "operating_revenue": 673510177,
  "gross_profit": 358124478,
  "operating_income": 286555542,
  "net_income": 247661438,
  "cash_flow_from_operating_activities": 377668210,
  "net_cash_flow_from_investing_activities": -197607330,
  "net_cash_flow_from_financing_activities": -90244583,
  "free_cash_flow": 171993526
}
```

#### 取得估值概況

**請求**
```bash
curl -X POST "http://0.0.0.0:9090/neurostats/valuation/overview" -H "Content-Type: application/json" -d '{"ticker": "2330"}'
```

**回應**
```json
{
  "PE_Ratio": 28.15,
  "PFCF_Ratio": 23.05,
  "PB_Ratio": 15.8,
  "PS_Ratio": 5.4,
  "EV_OPI_Ratio": 22.3,
  "EV_EBIT_Ratio": 20.1,
  "EV_EBITDA_Ratio": 18.6,
  "EV_S_Ratio": 4.9
}
```

## API 測試

在 `api_test.py` 中包含了每個 API 路徑的單元測試，確保每個路由能夠正常運行並返回預期結果。以下是測試的使用方法：

1. 確保虛擬環境已安裝 `pytest` 和 `pytest-asyncio` 以支持異步測試：

   ```bash
   pip install pytest pytest-asyncio
   ```

2. 執行測試：

   ```bash
   pytest api_test.py
   ```

   測試結果將顯示所有路由的測試結果。每個測試方法以 `test_` 開頭，測試會自動檢查 API 是否返回狀態碼 200 並包含必要的數據欄位。

### 測試範例

以下是一個測試函數的範例：

```python
@pytest.mark.asyncio
async def test_get_finance_data():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/vitals/finance_data", json={"ticker": "AAPL"})
    assert response.status_code == 200
    data = response.json()
    assert "quarter" in data
    assert "operating_revenue" in data
```

此函數測試 `/neurostats/fundamental/vitals/finance_data` 路徑，檢查返回狀態是否為 200 並確認回應中包含 `quarter` 和 `operating_revenue` 字段。

## 說明

### API 結構
- `neurostats/fundamental/` 提供有關公司的財務基本面數據。
- `neurostats/valuation/` 提供公司估值的相關數據。



