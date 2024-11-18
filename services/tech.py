import os
from .base import ResponseService
from neurostats_API.fetchers.tech import TechFetcher


class TechResponse(ResponseService):
    
    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = TechFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )


class TechVitals(TechResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

    def get_vitals(self):
        
        n_days = 30
        vitals = self.data_fetcher.get_daily().tail(n_days)
        
        return ResponseService.replace_empty_values(
            vitals,
            marker = '不適用'
        )

class TechDaily(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return ResponseService.replace_empty_values(
            self.data_fetcher.get_daily(),
            marker = '不適用'
        )

class TechWeekly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return ResponseService.replace_empty_values(
            self.data_fetcher.get_weekly(),
            marker = '不適用'
        )    
    
class TechMonthly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return ResponseService.replace_empty_values(
            self.data_fetcher.get_monthly(),
            marker = '不適用'
        )
    
    
class TechQuarterly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return ResponseService.replace_empty_values(
            self.data_fetcher.get_quarterly(),
            marker = '不適用'
        )
    
class TechYearly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return ResponseService.replace_empty_values(
            self.data_fetcher.get_yearly(),
            marker = '不適用'
        )
    
    
    