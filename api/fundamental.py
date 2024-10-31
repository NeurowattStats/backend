from fastapi import APIRouter, HTTPException

from models import (TickerRequest, FinanceData, 
                    PerShareData, FinancialRatios)

from services import FundVitals, RevenStatements

router = APIRouter()

@router.post("/vitals/finance_data", response_model=FinanceData)
async def get_finance_data(request: TickerRequest):

    try:
        responser = FundVitals(ticker=request.ticker)
        data = responser.get_finance()

        return FinanceData(
            quarter=data.get('Quarter'),
            unit=data.get('Unit'),
            operating_revenue=data.get('Operating_Revenue'),
            gross_profit=data.get('Gross_Profit'),
            operating_income=data.get('Operating_Income'),
            net_income = data.get('Net_Income'),
            cash_flow_from_operating_activities=data.get('Cash_Flow_from_Operating_Activities'),
            net_cash_flow_from_investing_activities=data.get('Net_Cash_Flow_from_Investing_Activities'),
            net_cash_flow_from_financing_activities=data.get('Net_Cash_Flow_from_Financing_Activities'),
            free_cash_flow = data.get('Free_Cash_Flow')
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/vitals/per_share", response_model=PerShareData)
async def get_per_share(request: TickerRequest):

    try:
        responser = FundVitals(ticker=request.ticker)
        data = responser.get_per_share()

        return PerShareData(
            quarter=data.get('Quarter'),
            unit=data.get('Unit'),
            revenue_per_share=data.get('Revenue_per_Share'),
            gross_profit_per_share = data.get('Gross_Profit_per_Share'),
            operating_income_per_share=data.get('Operating_Income_per_Share'),
            earnings_per_share_eps=data.get('Earnings_per_Share_EPS'),
            operating_cash_flow_per_share=data.get('Operating_Cash_Flow_per_Share'),
            free_cash_flow_per_share = data.get('Free_Cash_Flow_per_Share'),
            interest_bearing_debt_per_share=data.get('Interest_Bearing_Debt_per_Share'),
            net_asset_per_share=data.get('Net_Asset_per_Share')
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/vitals/ratios", response_model=FinancialRatios)
async def get_ratios(request: TickerRequest):

    try:
        responser = FundVitals(ticker=request.ticker)
        data = responser.get_ratios()

        return FinancialRatios(
            quarter=data.get('Quarter'),
            unit=data.get('Unit'),
            return_on_assets_roa=data.get('Return_on_Assets_ROA'),
            return_on_equity_roe = data.get('Return_on_Equity_ROE'),
            gross_profit_to_total_assets=data.get('Gross_Profit_to_Total_Assets'),
            return_on_capital_employed_roce=data.get('Return_on_Capital_Employed_ROCE'),
            gross_profit_margin=data.get('Gross_Profit_Margin'),
            operating_income_margin = data.get('Operating_Income_Margin'),
            net_profit_margin=data.get('Net_Profit_Margin'),
            operating_cash_flow_margin=data.get('Operating_Cash_Flow_Margin')
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/revenue/monthly")
async def get_monthly(request: TickerRequest):

    try:
        responser = RevenStatements(ticker=request.ticker)
        data = responser.get_monthly()

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/revenue/this_month")
async def get_this_month(request: TickerRequest):

    try:
        responser = RevenStatements(ticker=request.ticker)
        data = responser.get_this_month()

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/revenue/this_month_text")
async def get_this_month_text(request: TickerRequest):

    try:
        responser = RevenStatements(ticker=request.ticker)
        data = responser.get_this_month_text()

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))