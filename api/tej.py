from fastapi import APIRouter, HTTPException
from models import (
    TickerRequest,
)
from services import (
    TEJCompanySelfSettlement,
    TEJFinanceStatement
)
from utils import handle_request
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()

@router.post("/finance_statement/over_quarter")
async def  get_finance_statement_serial_value(request: TickerRequest):
    cache_key = f"{request.ticker}:TEJ_{request.include_content}_finance_statement_serial_value"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data
    
    tej_finance_value = handle_request(
        ticker=request.ticker, 
        service_class=TEJFinanceStatement, 
        method_name='get_serial_data_without_growth', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([tej_finance_value]))  # Serialize data
    return [tej_finance_value]

@router.post("/finance_statement/over_year")
async def get_finance_statement_verticle_value(request: TickerRequest):
    cache_key = f"{request.ticker}:TEJ_{request.include_content}_finance_statement_vertical_value"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data
    
    tej_finance_value = handle_request(
        ticker=request.ticker, 
        service_class=TEJFinanceStatement, 
        method_name='get_vertical_data_without_growth', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([tej_finance_value]))  # Serialize data
    return [tej_finance_value]

@router.post("/finance_statement/over_quarter_with_QoQ")
async def get_finance_statement_verticle_with_growth(request: TickerRequest):
    cache_key = f"{request.ticker}:TEJ_{request.include_content}_finance_statement_vertical_with_QoQ"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data
    
    tej_finance_value = handle_request(
        ticker=request.ticker, 
        service_class=TEJFinanceStatement, 
        method_name='get_serial_data_with_growth', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([tej_finance_value]))  # Serialize data
    return [tej_finance_value]



@router.post("/company_self_settlement/over_quarter")
async def get_self_settlement_serial_value(request: TickerRequest):
    cache_key = f"{request.ticker}:TEJ_{request.include_content}_self_settlement_serial_value"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data
    
    tej_finance_value = handle_request(
        ticker=request.ticker, 
        service_class=TEJCompanySelfSettlement, 
        method_name='get_serial_data_without_growth', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([tej_finance_value]))  # Serialize data
    return [tej_finance_value]

@router.post("/company_self_settlement/over_year")
async def get_self_settlement_vertical_value(request: TickerRequest):
    cache_key = f"{request.ticker}:TEJ_{request.include_content}_self_settlement_serial_value"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data
    
    tej_finance_value = handle_request(
        ticker=request.ticker, 
        service_class=TEJCompanySelfSettlement, 
        method_name='get_vertical_data_without_growth', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([tej_finance_value]))  # Serialize data
    return [tej_finance_value]
