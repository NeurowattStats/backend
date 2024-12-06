# %%
from fastapi import APIRouter, HTTPException

from utils import handle_request

from services import (
    InstitutionOverall,
    MarginTrade
)

from models import (
    InstitutionOverall,
    TickerRequest
)

router = APIRouter()

# %%
@router.post("/institution/latest", response_model=InstitutionOverall)
async def get_institution_latest(request:TickerRequest):

    data = handle_request(
        ticker = request.ticker,
        service_class = InstitutionOverall,
        method_name = 'get_latest',
        include_content = False
    )

    return data

@router.post("/institution/history")
async def get_institution_history(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = InstitutionOverall,
            method_name = 'get_history',
            include_content = False
        )

        return data

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/margin_trade/latest")
async def get_margin_trade_latest(request:TickerRequest):

    data = handle_request(
        ticker = request.ticker,
        service_class = MarginTrade,
        method_name = 'get_latest',
        include_content = False
    )

    return data

@router.post("/margin_trade/history")
async def get_margin_trade_history(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = MarginTrade,
            method_name = 'get_history',
            include_content = False
        )

        return data

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

