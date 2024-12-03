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

router = APIRouter()

# %%
@router.post("/vitals", response_model=TechIndexesList)
async def get_vitals(request:TickerRequest):
    data = handle_request(
        ticker = request.ticker,
        service_class = TechVitals,
        method_name = 'get_vitals',
        include_content = False
    )

    return TechIndexesList(array = data)

@router.post("/daily", response_model=TechIndexesList)
async def get_daily(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechDaily,
            method_name = 'get_basic_index',
            include_content = False
        )

        return TechIndexesList(array = data)

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/weekly", response_model=TechIndexesList)
async def get_weekly(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechWeekly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return TechIndexesList(array = data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/monthly", response_model=TechIndexesList)
async def get_monthly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechMonthly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return TechIndexesList(array = data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quarterly", response_model=TechIndexesList)
async def get_quarterly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechQuarterly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return TechIndexesList(array = data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/yearly", response_model=TechIndexesList)
async def get_yearly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechYearly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return TechIndexesList(array = data)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
