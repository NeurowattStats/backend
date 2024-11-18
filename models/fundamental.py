from pydantic import BaseModel
from typing import Optional

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


# vitals model 
class OverviewModel(BaseModel):
    year: str
    season: str
    revenue: Optional[float] = None
    gross_profit: Optional[float] = None
    operating_income: Optional[float] = None
    net_income: Optional[float] = None
    operating_cash_flow: Optional[float] = None
    invest_cash_flow: Optional[float] = None
    financing_cash_flow: Optional[float] = None

class PerShareModel(BaseModel):
    year: str
    season: str
    revenue_per_share: Optional[float] = None
    gross_per_share: Optional[float] = None
    operating_income_per_share: Optional[float] = None
    eps: Optional[float] = None
    operating_cash_flow_per_share: Optional[float] = None
    fcf_per_share: Optional[float] = None

class ProfitabilityModel(BaseModel):
    year: str
    season: str
    roa: Optional[float] = None
    roe: Optional[float] = None
    gross_over_asset: Optional[float] = None
    roce: Optional[float] = None
    gross_profit_margin: Optional[float] = None
    operation_profit_rate: Optional[float] = None
    net_income_rate: Optional[float] = None
    operating_cash_flow_profit_rate: Optional[float] = None

class GrowthMomentumModel(BaseModel):
    year: str
    season: str
    revenue_YoY: Optional[float] = None
    gross_prof_YoY: Optional[float] = None
    operating_income_YoY: Optional[float] = None
    net_income_YoY: Optional[float] = None
    operating_cash_flow_YoY: Optional[float] = None
    operating_cash_flow_per_share_YoY: Optional[float] = None

class FinancialResilienceModel(BaseModel):
    year: str
    season: str
    current_ratio: Optional[float] = None
    quick_ratio: Optional[float] = None
    debt_to_equity_ratio: Optional[float] = None
    net_debt_to_equity_ratio: Optional[float] = None
    interest_coverage_ratio: Optional[float] = None
    debt_to_operating_cash_flow: Optional[float] = None
    debt_to_free_cash_flow: Optional[float] = None
    cash_flow_ratio: Optional[float] = None

class BalanceSheetModel(BaseModel):
    year: str
    season: str
    current_assets: Optional[float] = None
    current_liabilities: Optional[float] = None
    non_current_assets: Optional[float] = None
    non_current_liabilities: Optional[float] = None
    total_asset: Optional[float] = None
    total_liabilities: Optional[float] = None
    equity: Optional[float] = None

