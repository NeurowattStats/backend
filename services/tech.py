from .base import ResponseService
from utils import TechFetcher

class TechResponse(ResponseService):
    
    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = TechFetcher(self.ticker)


class TechVitals(TechResponse):

    def __init__(self, ticker):
        super().__init__(ticker)
        

class TechDaily(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return self.data_fetcher.get_daily()


class TechWeekly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return self.data_fetcher.get_weekly()
    
    
class TechMonthly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return self.data_fetcher.get_monthly()
    
    
class TechQuarterly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return self.data_fetcher.get_quarterly()
    
    
class TechYearly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        return self.data_fetcher.get_yearly()
    
    
    