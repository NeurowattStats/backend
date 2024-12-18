from fastapi import APIRouter, HTTPException
from models import ValuationOverview, TickerRequest, TitleArray
from services import ValueResponse
from utils import handle_request
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()

# Initialize Redis connection


@router.post("/overview", response_model=ValuationOverview)
async def get_overview(request: TickerRequest):
    cache_key = f"{request.ticker}:ValueResponse_get_value_overview"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=ValueResponse,
        method_name='get_value_overview',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/table", response_model=TitleArray)
async def get_table(request: TickerRequest):
    cache_key = f"{request.ticker}:ValueResponse_get_value_table"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=ValueResponse,
        method_name='get_value_table',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data
