# %%
from typing import Union
import pandas as pd
from fastapi import APIRouter, HTTPException

from utils import handle_request
from services import (TechVitals, TechDaily, TechWeekly, 
                      TechMonthly, TechQuarterly, TechYearly)
from models import TickerRequest, TechBasicIndexes, TechDailyIndexes

router = APIRouter()

# %%
@router.post("/vitals")
async def get_vitals(request:TickerRequest):
    data = handle_request(
        ticker = request.ticker,
        service_class = TechVitals,
        method_name = 'get_vitals',
        include_content = False
    )

    '''
    TODO
    add model
    '''
    return data

@router.post("/daily", response_model=TechDailyIndexes)
async def get_daily(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechDaily,
            method_name = 'get_basic_index',
            include_content = False
        )

        return construct_tech_indexes(data, daily=True)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/weekly", response_model=TechBasicIndexes)
async def get_weekly(request:TickerRequest):

    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechWeekly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return construct_tech_indexes(data, daily=False)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/monthly", response_model=TechBasicIndexes)
async def get_monthly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechMonthly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return construct_tech_indexes(data, daily=False)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quarterly", response_model=TechBasicIndexes)
async def get_quarterly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechQuarterly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return construct_tech_indexes(data, daily=False)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/yearly", response_model=TechBasicIndexes)
async def get_yearly(request:TickerRequest):
    try:
        data = handle_request(
            ticker = request.ticker,
            service_class = TechYearly,
            method_name = 'get_basic_index',
            include_content = False
        )

        return construct_tech_indexes(data, daily=False)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def construct_tech_indexes(data: pd.DataFrame, daily: bool) -> Union[TechDailyIndexes, TechBasicIndexes]:
    if daily:
        return TechDailyIndexes(
            date=data.index.tolist(),
            open=data['open'].tolist(),
            high=data['high'].tolist(),
            low=data['low'].tolist(),
            close=data['close'].tolist(),
            volume=data['volume'].tolist(),
            SMA5=data['SMA5'].tolist(),
            SMA20=data['SMA20'].tolist(),
            SMA60=data['SMA60'].tolist(),
            EMA5=data['EMA5'].tolist(),
            EMA20=data['EMA20'].tolist(),
            EMA40=data['EMA40'].tolist(),
            EMA12=data['EMA12'].tolist(),
            EMA26=data['EMA26'].tolist(),
            RSI7=data['RSI7'].tolist(),
            RSI14=data['RSI14'].tolist(),
            RSI21=data['RSI21'].tolist(),
            MACD=data['MACD'].tolist(),
            signal_line=data['Signal Line'].tolist(),
            middle_band=data['Middle Band'].tolist(),
            upper_band=data['Upper Band'].tolist(),
            lower_band=data['Lower Band'].tolist(),
            percent_b=data['%b'].tolist(),
            BBW=data['BBW'].tolist(),
            ATR=data['ATR'].tolist(),
            EMA_cycle=data['EMA Cycle'].tolist(),
            EMA_cycle_instructions=data['EMA Cycle Instructions'].tolist(),
            close_yesterday=data['close_yesterday'].tolist(),
            day_trading_signal=data['Day Trading Signal'].tolist()
        )
    
    return TechBasicIndexes(
        date=data.index.tolist(),
        open=data['open'].tolist(),
        high=data['high'].tolist(),
        low=data['low'].tolist(),
        close=data['close'].tolist(),
        volume=data['volume'].tolist(),
        SMA5=data['SMA5'].tolist(),
        SMA20=data['SMA20'].tolist(),
        SMA60=data['SMA60'].tolist(),
        EMA5=data['EMA5'].tolist(),
        EMA20=data['EMA20'].tolist(),
        EMA40=data['EMA40'].tolist(),
        EMA12=data['EMA12'].tolist(),
        EMA26=data['EMA26'].tolist(),
        RSI7=data['RSI7'].tolist(),
        RSI14=data['RSI14'].tolist(),
        RSI21=data['RSI21'].tolist(),
        MACD=data['MACD'].tolist(),
        signal_line=data['Signal Line'].tolist(),
        middle_band=data['Middle Band'].tolist(),
        upper_band=data['Upper Band'].tolist(),
        lower_band=data['Lower Band'].tolist(),
        percent_b=data['%b'].tolist(),
        BBW=data['BBW'].tolist(),
        ATR=data['ATR'].tolist(),
    )