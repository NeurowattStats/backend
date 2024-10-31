from pydantic import BaseModel

class FinanceData(BaseModel):
    quarter: str
    unit: str
    operating_revenue: int
    gross_profit: int
    operating_income: int
    net_income: int
    cash_flow_from_operating_activities: int
    net_cash_flow_from_investing_activities: int
    net_cash_flow_from_financing_activities: int
    free_cash_flow: int

class PerShareData(BaseModel):
    quarter: str
    unit: str
    revenue_per_share: float
    gross_profit_per_share: float
    operating_income_per_share: float
    earnings_per_share_eps: float
    operating_cash_flow_per_share: float
    free_cash_flow_per_share: float
    interest_bearing_debt_per_share: float
    net_asset_per_share: float

class FinancialRatios(BaseModel):
    quarter: str
    unit: str
    return_on_assets_roa: float
    return_on_equity_roe: float
    gross_profit_to_total_assets: float
    return_on_capital_employed_roce: float
    gross_profit_margin: float
    operating_income_margin: float
    net_profit_margin: float
    operating_cash_flow_margin: float


