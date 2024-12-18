# %%
from typing import Union
import pandas as pd
from fastapi import APIRouter, HTTPException
from utils import handle_request
from services import (
    TechVitals, 
    TechDaily, 
    TechWeekly, 
    TechMonthly, 
    TechQuarterly, 
    TechYearly
)
from models import (
    TickerRequest, 
    TechIndexesList
)
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()


# %%
@router.post("/vitals", response_model=TechIndexesList)
async def get_vitals(request: TickerRequest):
    cache_key = f"{request.ticker}:TechVitals_get_vitals"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechVitals,
        method_name='get_vitals',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ])) 
    return TechIndexesList(array=data)

@router.post("/daily", response_model=TechIndexesList)
async def get_daily(request: TickerRequest):
    cache_key = f"{request.ticker}:TechDaily_get_basic_index"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechDaily,
        method_name='get_basic_index',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ]))
    return TechIndexesList(array=data)

@router.post("/weekly", response_model=TechIndexesList)
async def get_weekly(request: TickerRequest):
    cache_key = f"{request.ticker}:TechWeekly_get_basic_index"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechWeekly,
        method_name='get_basic_index',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ]))
    return TechIndexesList(array=data)

@router.post("/monthly", response_model=TechIndexesList)
async def get_monthly(request: TickerRequest):
    cache_key = f"{request.ticker}:TechMonthly_get_basic_index"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechMonthly,
        method_name='get_basic_index',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ]))
    return TechIndexesList(array=data)

@router.post("/quarterly", response_model=TechIndexesList)
async def get_quarterly(request: TickerRequest):
    cache_key = f"{request.ticker}:TechQuarterly_get_basic_index"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechQuarterly,
        method_name='get_basic_index',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ]))
    return TechIndexesList(array=data)
    
@router.post("/yearly", response_model=TechIndexesList)
async def get_yearly(request: TickerRequest):
    cache_key = f"{request.ticker}:TechYearly_get_basic_index"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return TechIndexesList(array=json.loads(cached_data))  # Deserialize cached data

    data = handle_request(
        ticker=request.ticker,
        service_class=TechYearly,
        method_name='get_basic_index',
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([
        {
            **item.dict(),
            "date": item.date.isoformat() if hasattr(item, "date") else None  # 確保 date 可序列化
        }
        for item in data
    ]))
    return TechIndexesList(array=data)
