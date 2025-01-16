from fastapi import FastAPI, Depends  # Import Depends
from fastapi.middleware.cors import CORSMiddleware
from api.fundamental import router as fundamental_router
from api.valuation import router as valuation_router
from api.tech import router as tech_router
from api.profit_loss import router as profit_loss_router
from api.chip import router as chip_router
from api.financial_report import router as financial_report_router
from api.earnings_call import router as earnings_call_router 
from dotenv import load_dotenv
from database.connection import redis_connector  # Import the existing redis_connector

import uvicorn
import os
import openai

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.environ['OPENAI_KEY']

# Flush all data from Redis
redis_connector.client.flushall()

app = FastAPI()

# Set CORS allowed origins, modify as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, consider setting specific domains based on needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include fundamental router
app.include_router(fundamental_router, prefix="/neurostats/fundamental", tags=["Fundamental"])

# Include valuation router
app.include_router(valuation_router, prefix="/neurostats/valuation", tags=["Valuation"])

# Include tech router
app.include_router(tech_router, prefix="/neurostats/tech", tags=["Tech"])  # New router

# Include profit_loss router
app.include_router(profit_loss_router, prefix="/neurostats/fundamental/profit_loss", tags=["ProfitAndLoss"])  # New router

# Include chip router
app.include_router(chip_router, prefix="/neurostats/chip", tags=["Chip"])  # New router

# Inclue financial report RAG router
app.include_router(financial_report_router, prefix="/neurostats/RAG", tags=['RAG']) 

# Include earnings call router
app.include_router(earnings_call_router, prefix="/neurostats/earnings_call", tags=['EarningsCall'])

# Start application
if __name__ == "__main__":
    # Get host and port from environment variables, default to 0.0.0.0 and 8080
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8080))

    uvicorn.run(app, host=host, port=port)
