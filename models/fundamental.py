from pydantic import BaseModel
from typing import Optional

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

class OperatingIndicatorsModel(BaseModel):
    year: str
    season: str
    dso: Optional[float] = None  # Days Sales Outstanding
    account_receive_over_revenue: Optional[float] = None
    dio: Optional[float] = None  # Days Inventory Outstanding
    inventories_revenue_ratio: Optional[float] = None
    dpo: Optional[float] = None  # Days Payables Outstanding
    cash_of_conversion_cycle: Optional[float] = None
    asset_turnover: Optional[float] = None
    applcation_turnover: Optional[float] = None

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

