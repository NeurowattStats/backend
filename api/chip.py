# %%
from fastapi import APIRouter, HTTPException

from utils import handle_request

from services import (
    InstitutionResponse,
    MarginTrade
)

from models import (
    ChipOverall,
    TickerRequest
)

router = APIRouter()

# %%
@router.post("/institution/overall")
async def get_institution_overall(request:TickerRequest):

    data = handle_request(
        ticker = request.ticker,
        service_class = InstitutionResponse,
        method_name = 'get_overall',
        include_content = request.include_content,
        content_method_name = 'get_overall_text'
    )

    return data

@router.post("/institution/latest")
async def get_institution_latest(request:TickerRequest):

    data = handle_request(
        ticker = request.ticker,
        service_class = InstitutionResponse,
        method_name = 'get_latest',
        include_content = False
    )

    return data

@router.post("/institution/history")
async def get_institution_history(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = InstitutionResponse,
            method_name = 'get_history',
            include_content = False
        )

        return data

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/margin_trade/overall")
async def get_margin_trade_overall(request:TickerRequest):

    data = handle_request(
        ticker = request.ticker,
        service_class = MarginTrade,
        method_name = 'get_overall',
        include_content = request.include_content,
        content_method_name = 'get_overall_text'
    )

    return data

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

