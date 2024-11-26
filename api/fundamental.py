from fastapi import APIRouter

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

router = APIRouter()


# Vitals
@router.post("/vitals/overview", response_model=OverviewModel)
async def get_finance_overview(request: TickerRequest):
    return handle_request(
        request.ticker, 
        FundVitals, 
        'get_overview'
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
@router.post("/revenue/month_revenue")
async def get_month_revenue(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_month_revenue',
    )

@router.post("/revenue/revenue_over_years", response_model=TitleArray)
async def get_revenue_over_years(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_revenue_over_years',
        include_content=request.include_content,
        content_method_name='get_revenue_over_years_text'
    )

@router.post("/revenue/grand_total_over_years", response_model=TitleArray)
async def get_grand_total_over_years(request: TickerRequest):
    return handle_request(
        request.ticker, 
        RevenStatements, 
        'get_grand_total_over_years',
        include_content=request.include_content,
        content_method_name='get_grand_total_over_years_text'
    )

# BalanceSheet
@router.post("/balance_sheet/full_table")
async def get_balance_sheet_full_table(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_full_table'
    )

@router.post("/balance_sheet/total_asset", response_model=TitleArray)
async def get_total_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_total_asset', 
        include_content=request.include_content,
        content_method_name='get_total_asset_text'
    )

@router.post("/balance_sheet/current_asset", response_model=TitleArray)
async def get_current_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_asset', 
        include_content=request.include_content,
        content_method_name='get_current_asset_text'
    )

@router.post("/balance_sheet/non_current_asset", response_model=TitleArray)
async def get_non_current_asset(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_asset', 
        include_content=request.include_content,
        content_method_name='get_non_current_asset_text'
    )

@router.post("/balance_sheet/current_debt", response_model=TitleArray)
async def get_current_debt(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_current_debt', 
        include_content=request.include_content,
        content_method_name='get_current_debt_text'
    )

@router.post("/balance_sheet/non_current_debt", response_model=TitleArray)
async def get_non_current_debt(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_non_current_debt', 
        include_content=request.include_content,
        content_method_name='get_non_current_debt_text'
    )

@router.post("/balance_sheet/equity", response_model=TitleArray)
async def get_equity(request: TickerRequest):
    return handle_request(
        request.ticker, 
        BalanceSheet, 
        'get_equity', 
        include_content=request.include_content,
        content_method_name='get_equity_text'
    )

# Cashflow
@router.post("/cashflow/full_table")
async def get_cashflow_full_table(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_full_table'
    )

@router.post("/cashflow/operation", response_model=TitleArray)
async def get_operation(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_operation', 
        include_content=request.include_content,
        content_method_name = 'get_operation_text'
    )

@router.post("/cashflow/investment", response_model=TitleArray)
async def get_investment(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_investment', 
        include_content=request.include_content,
        content_method_name = 'get_investment_text'
    )

@router.post("/cashflow/fundraising", response_model=TitleArray)
async def get_fundraising(request: TickerRequest):
    return handle_request(
        request.ticker, 
        CashflowSheet, 
        'get_fundraising', 
        include_content=request.include_content,
        content_method_name = 'get_fundraising_text'
    )