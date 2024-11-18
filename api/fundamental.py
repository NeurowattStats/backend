from fastapi import APIRouter, HTTPException

from models import (
    TickerRequest,
    OverviewModel, 
    PerShareModel, 
    ProfitabilityModel, 
    GrowthMomentumModel, 
    FinancialResilienceModel, 
    BalanceSheetModel,
    OperatingIndicatorsModel
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

router = APIRouter()


# Vitals
@router.post("/vitals/overview", response_model=OverviewModel)
async def get_finance_overview(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_finance'
    )

@router.post("/vitals/per_share", response_model=PerShareModel)
async def get_per_share(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_per_share'
    )

@router.post("/vitals/profitability", response_model=ProfitabilityModel)
async def get_profitability(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_profitability'
    )

@router.post("/vitals/growth_momentum", response_model=GrowthMomentumModel)
async def get_growth_momentum(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_growth_momentum'
    )

@router.post("/vitals/operating_indicators", response_model=OperatingIndicatorsModel)
async def get_operating_indicators(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_operating_indicators'
    )

@router.post("/vitals/financial_resilience", response_model=FinancialResilienceModel)
async def get_financial_resilience(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_financial_resilience'
    )

@router.post("/vitals/balance_sheet", response_model=BalanceSheetModel)
async def get_balance_sheet(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_balance_sheet'
    )

# Revenues
@router.post("/revenue/monthly")
async def get_monthly(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_monthly'
    )

@router.post("/revenue/this_month")
async def get_this_month(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_this_month'
    )

@router.post("/revenue/this_month_text")
async def get_this_month_text(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_this_month_text'
    )

# BalanceSheet
@router.post("/balance_sheet/full_table")
async def get_balance_sheet_full_table(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_full_table'
    )

@router.post("/balance_sheet/total_asset")
async def get_total_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_total_asset', 
        include_content=True
    )

@router.post("/balance_sheet/current_asset")
async def get_current_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_asset', 
        include_content=True
    )

@router.post("/balance_sheet/non_current_asset")
async def get_non_current_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_asset', 
        include_content=True
    )

@router.post("/balance_sheet/current_debt")
async def get_current_debt(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_debt', 
        include_content=True
    )

@router.post("/balance_sheet/non_current_debt")
async def get_non_current_debt(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_debt', 
        include_content=True
    )

@router.post("/balance_sheet/equity")
async def get_equity(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_equity', 
        include_content=True
    )

# Cashflow
@router.post("/cashflow/full_table")
async def get_cashflow_full_table(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_full_table'
    )

@router.post("/cashflow/operation")
async def get_operation(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_operation', 
        include_content=True
    )

@router.post("/cashflow/investment")
async def get_investment(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_investment', 
        include_content=True
    )

@router.post("/cashflow/fundraising")
async def get_fundraising(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_fundraising', 
        include_content=True
    )