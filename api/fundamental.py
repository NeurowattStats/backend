from fastapi import APIRouter, HTTPException
from models import (
    TickerRequest,
    OverviewModel, 
    PerShareModel, 
    ProfitabilityModel, 
    GrowthMomentumModel, 
    FinancialResilienceModel, 
    BalanceSheetModel,
    OperatingIndicatorsModel,
    TitleArray
)
from services import (
    FundVitals, 
    FundResponse, 
    RevenStatements,
    ProfitLoss, 
    BalanceSheet,
    CashflowSheet,
    Dividend, 
    Report
)
from utils import handle_request
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()

# Vitals
@router.post("/vitals/overview", response_model=OverviewModel)
async def get_finance_overview(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_overview"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_overview'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/per_share", response_model=PerShareModel)
async def get_per_share(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_per_share"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_per_share'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/profitability", response_model=ProfitabilityModel)
async def get_profitability(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_profitability"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_profitability'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/growth_momentum", response_model=GrowthMomentumModel)
async def get_growth_momentum(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_growth_momentum"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_growth_momentum'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/operating_indicators", response_model=OperatingIndicatorsModel)
async def get_operating_indicators(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_operating_indicators"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_operating_indicators'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/financial_resilience", response_model=FinancialResilienceModel)
async def get_financial_resilience(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_financial_resilience"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_financial_resilience'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/vitals/balance_sheet", response_model=BalanceSheetModel)
async def get_balance_sheet(request: TickerRequest):
    cache_key = f"{request.ticker}:FundVitals_get_balance_sheet"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        FundVitals, 
        'get_balance_sheet'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

# Revenues
@router.post("/revenue/month_revenue")
async def get_month_revenue(request: TickerRequest):
    cache_key = f"{request.ticker}:RevenStatements_get_month_revenue"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        RevenStatements, 
        'get_month_revenue',
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/revenue/revenue_over_years")
async def get_revenue_over_years(request: TickerRequest):
    cache_key = f"{request.ticker}:RevenStatements_get_revenue_over_years_{request.include_content}_get_revenue_over_years_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        RevenStatements, 
        'get_revenue_over_years',
        include_content=request.include_content,
        content_method_name='get_revenue_over_years_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/revenue/grand_total_over_years")
async def get_grand_total_over_years(request: TickerRequest):
    cache_key = f"{request.ticker}:RevenStatements_get_grand_total_over_years_{request.include_content}_get_grand_total_over_years_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        RevenStatements, 
        'get_grand_total_over_years',
        include_content=request.include_content,
        content_method_name='get_grand_total_over_years_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

# BalanceSheet
@router.post("/balance_sheet/full_table")
async def get_balance_sheet_full_table(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_full_table"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_full_table'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/total_asset")
async def get_total_asset(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_total_asset_{request.include_content}_get_full_table"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_total_asset', 
        include_content=request.include_content,
        content_method_name='get_total_asset_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/current_asset")
async def get_current_asset(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_current_asset_{request.include_content}_get_current_asset_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_asset', 
        include_content=request.include_content,
        content_method_name='get_current_asset_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/non_current_asset")
async def get_non_current_asset(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_non_current_asset_{request.include_content}_get_non_current_asset_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_asset', 
        include_content=request.include_content,
        content_method_name='get_non_current_asset_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/current_debt")
async def get_current_debt(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_current_debt_{request.include_content}_get_current_debt_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_debt', 
        include_content=request.include_content,
        content_method_name='get_current_debt_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/non_current_debt")
async def get_non_current_debt(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_non_current_debt_{request.include_content}_get_non_current_debt_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_debt', 
        include_content=request.include_content,
        content_method_name='get_non_current_debt_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/balance_sheet/equity")
async def get_equity(request: TickerRequest):
    cache_key = f"{request.ticker}:BalanceSheet_get_equity_{request.include_content}_get_equity_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_equity', 
        include_content=request.include_content,
        content_method_name='get_equity_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

# Cashflow
@router.post("/cashflow/full_table")
async def get_cashflow_full_table(request: TickerRequest):
    cache_key = f"{request.ticker}:CashflowSheet_get_full_table"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_full_table'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/cashflow/operation")
async def get_operation(request: TickerRequest):
    cache_key = f"{request.ticker}:CashflowSheet_get_operation_{request.include_content}_get_operation_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_operation', 
        include_content=request.include_content,
        content_method_name='get_operation_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/cashflow/investment")
async def get_investment(request: TickerRequest):
    cache_key = f"{request.ticker}:CashflowSheet_get_investment_{request.include_content}_get_investment_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_investment', 
        include_content=request.include_content,
        content_method_name='get_investment_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data

@router.post("/cashflow/fundraising")
async def get_fundraising(request: TickerRequest):
    cache_key = f"{request.ticker}:CashflowSheet_get_fundraising_{request.include_content}_get_fundraising_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    data = handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_fundraising', 
        include_content=request.include_content,
        content_method_name='get_fundraising_text'
    )

    redis_connector.set(cache_key, json.dumps(data.dict()))  # Serialize data
    return data
