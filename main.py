from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.fundamental import router as fundamental_router
from api.valuation import router as valuation_router
from api.tech import router as tech_router
from api.profit_loss import router as profit_loss_router
from dotenv import load_dotenv

import uvicorn
import os

# 加載 .env 文件中的環境變量
load_dotenv()

app = FastAPI()

# 設置 CORS 允許的來源，視需求可修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源，建議根據需求設定特定的域
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含 fundamental 的路由
app.include_router(fundamental_router, prefix="/neurostats/fundamental", tags=["Fundamental"])

# 包含 valuation 的路由
app.include_router(valuation_router, prefix="/neurostats/valuation", tags=["Valuation"])

# 包含 tech 的路由
app.include_router(tech_router, prefix="/neurostats/tech", tags=["Tech"])  # 新增的路由

# 包含 tech 的路由
app.include_router(tech_router, prefix="/neurostats/fundamental/profit_loss", tags=["ProfitAndLoss"])  # 新增的路由

# 啟動應用
if __name__ == "__main__":
    
    # 從環境變量中獲取主機和端口，默認為 0.0.0.0 和 8080
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))

    if __name__ == "__main__":
        uvicorn.run(app, host=host, port=port)
