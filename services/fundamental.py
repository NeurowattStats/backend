# %%
from .base import ResponseService


# %%
class FundResponse(ResponseService):

    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker

class FundVitals(FundResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)
        self.ticker = ticker

    def get_finance(self)->dict:
        
        self.finance = self.full_fake['finance']

        return self.finance
    
    def get_per_share(self)->dict:

        self.per_share_data = self.full_fake['per_share_data']

        return self.per_share_data
    
    def get_ratios(self)->dict:

        self.financial_ratios = self.full_fake['financial_ratios']

        return self.financial_ratios
    
class RevenStatements(FundResponse):

    def __init__(self, ticker: str):
        super().__init__(ticker)

    def get_monthly(self):
        
        self.monthly_revenue = self.full_fake['monthly_revenue']

        return self.monthly_revenue
    
    def get_this_month(self):

        self.this_monthly_revenue = self.full_fake['revenue_growth']

        return self.this_monthly_revenue

    def get_this_month_text(self):

        self.revenue_gen = self.fake_gen['monthly_growth']

        return self.revenue_gen
            