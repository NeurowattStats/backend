from pydantic import BaseModel
from typing import Optional, Union

# vitals model 
class OverviewModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    revenue: Union[int, str] = '不適用'
    gross_profit: Union[int, str] = '不適用'
    operating_income: Union[int, str] = '不適用'
    net_income: Union[int, str] = '不適用'
    operating_cash_flow: Union[int, str] = '不適用'
    invest_cash_flow: Union[int, str] = '不適用'
    financing_cash_flow: Union[int, str] = '不適用'

class PerShareModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    revenue_per_share: Union[float, str] = '不適用'
    gross_per_share: Union[float, str] = '不適用'
    operating_income_per_share: Union[float, str] = '不適用'
    eps: Union[float, str] = '不適用'
    operating_cash_flow_per_share: Union[float, str] = '不適用'
    fcf_per_share: Union[float, str] = '不適用'

class ProfitabilityModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    roa: Union[float, str] = '不適用'
    roe: Union[float, str] = '不適用'
    gross_over_asset: Union[float, str] = '不適用'
    roce: Union[float, str] = '不適用'
    gross_profit_margin: Union[float, str] = '不適用'
    operation_profit_rate: Union[float, str] = '不適用'
    net_income_rate: Union[float, str] = '不適用'
    operating_cash_flow_profit_rate: Union[float, str] = '不適用'

class GrowthMomentumModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    revenue_YoY: Union[float, str] = '不適用'
    gross_prof_YoY: Union[float, str] = '不適用'
    operating_income_YoY: Union[float, str] = '不適用'
    net_income_YoY: Union[float, str] = '不適用'
    operating_cash_flow_YoY: Union[float, str] = '不適用'
    operating_cash_flow_per_share_YoY: Union[float, str] = '不適用'

class OperatingIndicatorsModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    dso: Union[float, str] = '不適用'  # Days Sales Outstanding
    account_receive_over_revenue: Union[float, str] = '不適用'
    dio: Union[float, str] = '不適用'  # Days Inventory Outstanding
    inventories_revenue_ratio: Union[float, str] = '不適用'
    dpo: Union[float, str] = '不適用'  # Days Payables Outstanding
    cash_of_conversion_cycle: Union[float, str] = '不適用'
    asset_turnover: Union[float, str] = '不適用'
    applcation_turnover: Union[float, str] = '不適用'

class FinancialResilienceModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    current_ratio: Union[float, str] = '不適用'
    quick_ratio: Union[float, str] = '不適用'
    debt_to_equity_ratio: Union[float, str] = '不適用'
    net_debt_to_equity_ratio: Union[float, str] = '不適用'
    interest_coverage_ratio: Union[float, str] = '不適用'
    debt_to_operating_cash_flow: Union[float, str] = '不適用'
    debt_to_free_cash_flow: Union[float, str] = '不適用'
    cash_flow_ratio: Union[float, str] = '不適用'

class BalanceSheetModel(BaseModel):
    year: Union[int, str]
    season: Union[int, str]
    current_assets: Union[int, str] = '不適用'
    current_liabilities: Union[int, str] = '不適用'
    non_current_assets: Union[int, str] = '不適用'
    non_current_liabilities: Union[int, str] = '不適用'
    total_asset: Union[int, str] = '不適用'
    total_liabilities: Union[int, str] = '不適用'
    equity: Union[int, str] = '不適用'