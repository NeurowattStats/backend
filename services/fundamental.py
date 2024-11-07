# %%
from .base import ResponseService

# %%
class FundResponse(ResponseService):

    def __init__(self, ticker: str):
        super().__init__()
        self.ticker = ticker

    @staticmethod
    def _get_data(data: dict, key: str, default='不適用'):
        """Retrieve data with a key from the given data structure and handle missing values."""
        return data.get(key, default)

class FundVitals(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)

    def get_finance(self) -> dict:
        return FundResponse._get_data(self.full_fake, 'finance')
    
    def get_per_share(self) -> dict:
        return FundResponse._get_data(self.full_fake, 'per_share_data')
    
    def get_ratios(self) -> dict:
        return FundResponse._get_data(self.full_fake, 'financial_ratios')

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

class ProfitLossTable(FundResponse):
    
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

    
