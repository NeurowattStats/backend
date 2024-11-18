# %%
from neurostats_API.fetchers.finance_overview import FinanceOverviewFetcher
from .base import ResponseService
from models import (
    OverviewModel, 
    PerShareModel, 
    ProfitabilityModel, 
    GrowthMomentumModel, 
    FinancialResilienceModel, 
    BalanceSheetModel
)
 
# %%
class FundResponse(ResponseService):

    def __init__(self, ticker: str):
        super().__init__()
        self.ticker = ticker

    def _get_data(self, data: dict, key: str, default='不適用'):
        """Retrieve data with a key from the given data structure and handle missing values."""
        return data.get(key, default)
    
class FundVitals(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.data_fetcher = FinanceOverviewFetcher()
        self.full_data = self.data_fetcher.query_data()
        self.company_name = self.full_data.get('company_name')

        self.recent_season_vitals = self.full_data.get('seasonal_data', {})
        self.year = self.recent_season_vitals.get('year', '不適用')
        self.season = self.recent_season_vitals.get('season', '不適用')

    def _get_multiple_data(self, fields: list) -> dict:
        """Helper method to retrieve multiple fields from seasonal data."""
        return {field: self._get_data(self.recent_season_vitals, field) for field in fields}

    def get_overview(self) -> OverviewModel:
        """Get a dictionary with the overview of financial data."""
        overview_fields = [
            'revenue', 'gross_profit', 'operating_income', 'net_income',
            'operating_cash_flow', 'invest_cash_flow', 'financing_cash_flow'
        ]
        overview = self._get_multiple_data(overview_fields)
        return OverviewModel(year=self.year, season=self.season, **overview)

    def get_per_share(self) -> PerShareModel:
        """Get a dictionary with per-share financial data."""
        per_share_fields = [
            'revenue_per_share', 'gross_per_share', 'operating_income_per_share',
            'eps', 'operating_cash_flow_per_share', 'fcf_per_share'
        ]
        per_share = self._get_multiple_data(per_share_fields)
        return PerShareModel(year=self.year, season=self.season, **per_share)

    def get_profitability(self) -> ProfitabilityModel:
        """Get a dictionary with profitability data."""
        profitability_fields = [
            'roa', 'roe', 'gross_over_asset', 'roce', 'gross_profit_margin',
            'operation_profit_rate', 'net_income_rate', 'operating_cash_flow_profit_rate'
        ]
        profitability = self._get_multiple_data(profitability_fields)
        return ProfitabilityModel(year=self.year, season=self.season, **profitability)

    def get_growth_momentum(self) -> GrowthMomentumModel:
        """Get a dictionary with growth momentum data."""
        growth_momentum_fields = [
            'revenue_YoY', 'gross_prof_YoY', 'operating_income_YoY', 'net_income_YoY',
            'operating_cash_flow_YoY', 'operating_cash_flow_per_share_YoY'
        ]
        growth_momentum = self._get_multiple_data(growth_momentum_fields)
        return GrowthMomentumModel(year=self.year, season=self.season, **growth_momentum)

    def get_financial_resilience(self) -> FinancialResilienceModel:
        """Get a dictionary with financial resilience data."""
        financial_resilience_fields = [
            'current_ratio', 'quick_ratio', 'debt_to_equity_ratio', 
            'net_debt_to_equity_ratio', 'interest_coverage_ratio', 'debt_to_operating_cash_flow',
            'debt_to_free_cash_flow', 'cash_flow_ratio'
        ]
        financial_resilience = self._get_multiple_data(financial_resilience_fields)
        return FinancialResilienceModel(year=self.year, season=self.season, **financial_resilience)

    def get_balance_sheet(self) -> BalanceSheetModel:
        """Get a dictionary with balance sheet data."""
        balance_sheet_fields = [
            'current_assets', 'current_liabilities', 'non_current_assets',
            'non_current_liabilities', 'total_asset', 'total_liabilities', 'equity'
        ]
        balance_sheet = self._get_multiple_data(balance_sheet_fields)
        return BalanceSheetModel(year=self.year, season=self.season, **balance_sheet)


class RevenStatements(FundResponse):

    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.raw_full_data = self.data_fetcher.get_month_revenue_sheet(ticker)
        if not self.raw_full_data:
            raise ValueError("No revenue data available for the given ticker.")
        
        self.full_data = FundResponse.replace_empty_values(data=self.raw_full_data, marker='不適用')

    def get_monthly(self):
        return FundResponse._get_data(self.full_data, 'month_revenue')
    
    def get_this_month(self):
        return FundResponse._get_data(self.full_data, 'this_month_revenue_over_years')

    def get_this_month_text(self):
        return 'in process'
    
    def get_cumulative(self):
        return FundResponse._get_data(self.full_data, 'grand_total_over_years')
    
    def get_cumulative_text(self):
        return 'in process'

class ProfitLoss(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)

class BalanceSheet(FundResponse):

    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.raw_full_data = self.data_fetcher.get_balance_sheet(ticker)
        self.full_data = FundResponse.replace_empty_values(data=self.raw_full_data, marker='不適用')
    
    def get_full_table(self):
        return FundResponse._get_data(self.full_data, 'balance_sheet')
    
    def get_total_asset(self):
        return FundResponse._get_data(self.full_data, 'total_asset')
    
    def get_total_asset_text(self):
        return 'in process'
    
    def get_current_asset(self):
        return FundResponse._get_data(self.full_data, 'current_asset')
    
    def get_current_asset_text(self):
        return 'in process'

    def get_non_current_asset(self):
        return FundResponse._get_data(self.full_data, 'non_current_asset')
    
    def get_non_current_asset_text(self):
        return 'in process'
    
    def get_current_debt(self):
        return FundResponse._get_data(self.full_data, 'current_debt')
    
    def get_current_debt_text(self):
        return 'in process'
       
    def get_non_current_debt(self):
        return FundResponse._get_data(self.full_data, 'non_current_debt')

    def get_non_current_debt_text(self):
        return 'in process'   

    def get_equity(self):
        return FundResponse._get_data(self.full_data, 'equity')
    
    def get_equity_text(self):
        return 'in process'   

class CashflowSheet(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)
        self.raw_full_data = self.data_fetcher.get_cash_flow(ticker)
        self.full_data = FundResponse.replace_empty_values(data=self.raw_full_data, marker='不適用')

    def get_full_table(self):
        return FundResponse._get_data(self.full_data, 'cash_flow')
    
    def get_operation(self):
        return FundResponse._get_data(self.full_data, 'CASHO')
    
    def get_operation_text(self):
        return 'in process'
    
    def get_investment(self):
        return FundResponse._get_data(self.full_data,'CASHI')
    
    def get_investment_text(self):
        return 'in process'
    
    def get_fundraising(self):
        return FundResponse._get_data(self.full_data, 'CASHF')
    
    def get_fundraising_text(self):
        return 'in process'

class Dividend(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

class Report(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

    
