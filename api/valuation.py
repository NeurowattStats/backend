from fastapi import APIRouter

from models import ValuationOverview, TickerRequest, ValuationTable
from services import ValueResponse

from utils import handle_request


router = APIRouter()

@router.post("/overview", response_model=ValuationOverview)
async def get_overview(request: TickerRequest):

    return handle_request(
        ticker = request.ticker,
        service_class = ValueResponse,
        method_name = 'get_value_overview',
        include_content = False
    )
    
@router.post("/table", response_model=ValuationTable)
async def get_table(request: TickerRequest):

    return handle_request(
        ticker = request.ticker,
        service_class = ValueResponse,
        method_name = 'get_value_table',
        include_content = False
    )