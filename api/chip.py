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
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()

# Use the redis_connector instance from main.py
# No need to initialize Redis connection here

# %%
@router.post("/institution/overall")
async def get_institution_overall(request: TickerRequest):
    cache_key = f"{request.ticker}:InstitutionResponse_get_overall_{request.include_content}"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=InstitutionResponse,
        method_name='get_overall',
        include_content=request.include_content,
        content_method_name='get_overall_text'
    )

    redis_connector.set(cache_key, json.dumps({
        "content": data["content"],
        "array": data["array"].__dict__  # Convert ChipOverall object to dictionary
    }))  # Serialize data
    return data

@router.post("/institution/latest")
async def get_institution_latest(request: TickerRequest):
    cache_key = f"{request.ticker}:InstitutionResponse_get_latest"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=InstitutionResponse,
        method_name='get_latest',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data))  # Serialize data
    return data

@router.post("/institution/history")
async def get_institution_history(request: TickerRequest):
    cache_key = f"{request.ticker}:InstitutionResponse_get_history"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=InstitutionResponse,
        method_name='get_history',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data.dict())) # Serialize data
    return data

@router.post("/margin_trade/overall")
async def get_margin_trade_overall(request: TickerRequest):
    cache_key = f"{request.ticker}:MarginTrade_get_overall_{request.include_content}"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=MarginTrade,
        method_name='get_overall',
        include_content=request.include_content,
        content_method_name='get_overall_text'
    )

    redis_connector.set(cache_key, json.dumps({
        "content": data["content"],
        "array": data["array"].__dict__  # Convert ChipOverall object to dictionary
    }))  # Serialize data
    return data

@router.post("/margin_trade/latest")
async def get_margin_trade_latest(request: TickerRequest):
    cache_key = f"{request.ticker}:MarginTrade_get_latest"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=MarginTrade,
        method_name='get_latest',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data))
    return data

@router.post("/margin_trade/history")
async def get_margin_trade_history(request: TickerRequest):
    cache_key = f"{request.ticker}:MarginTrade_get_history"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=MarginTrade,
        method_name='get_history',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps(data))
    return data
