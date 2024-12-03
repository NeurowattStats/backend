from .base import ResponseService
from models import TechIndexes
from neurostats_API.fetchers.tech import TechFetcher


class TechResponse(ResponseService):
    
    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = TechFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )

    def fit_model(self, data: list):
        tech_indexes_list = []
        for index_dict in data:
            # 创建 TechIndexes 模型实例
            indexes = TechIndexes(
                date=index_dict.get('date'),
                open=index_dict.get('open'),
                high=index_dict.get('high'),
                low=index_dict.get('low'),
                close=index_dict.get('close'),
                volume=index_dict.get('volume'),
                SMA5=index_dict.get('SMA5'),
                SMA20=index_dict.get('SMA20'),
                SMA60=index_dict.get('SMA60'),
                EMA5=index_dict.get('EMA5'),
                EMA20=index_dict.get('EMA20'),
                EMA40=index_dict.get('EMA40'),
                EMA12=index_dict.get('EMA12'),
                EMA26=index_dict.get('EMA26'),
                RSI7=index_dict.get('RSI7'),
                RSI14=index_dict.get('RSI14'),
                RSI21=index_dict.get('RSI21'),
                MACD=index_dict.get('MACD'),
                signal_line=index_dict.get('Signal Line'), 
                middle_band=index_dict.get('Middle Band'),
                upper_band=index_dict.get('Upper Band'),
                lower_band=index_dict.get('Lower Band'),
                percent_b=index_dict.get('%b'),  # %b percent_b
                BBW=index_dict.get('BBW'),
                ATR=index_dict.get('ATR'),
                EMA_cycle=index_dict.get('EMA Cycle'),
                EMA_cycle_instructions=index_dict.get('EMA Cycle Instructions'),
                close_yesterday=index_dict.get('close_yesterday'),
                day_trading_signal=index_dict.get('Day Trading Signal')
            )

            # 将创建的模型实例添加到列表中
            tech_indexes_list.append(indexes)

        return tech_indexes_list


class TechVitals(TechResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

    def get_vitals(self):
        
        n_days = 30
        vitals = self.data_fetcher.get_daily().tail(n_days)
        non_empty = ResponseService.replace_empty_values(
            vitals,
            marker = '不適用'
        )

        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)

class TechDaily(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):

        non_empty = ResponseService.replace_empty_values(
            self.data_fetcher.get_daily(),
            marker = '不適用'
        )
        
        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)

class TechWeekly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):

        non_empty = ResponseService.replace_empty_values(
            self.data_fetcher.get_weekly(),
            marker = '不適用'
        )    
        
        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)
    
class TechMonthly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):

        non_empty = ResponseService.replace_empty_values(
            self.data_fetcher.get_monthly(),
            marker = '不適用'
        )
        
        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)
    
    
class TechQuarterly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):

        non_empty = ResponseService.replace_empty_values(
            self.data_fetcher.get_quarterly(),
            marker = '不適用'
        )
    
        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)
    
class TechYearly(TechResponse):
    
    def __init__(self, ticker):
        super().__init__(ticker)

    def get_basic_index(self):
        
        non_empty = ResponseService.replace_empty_values(
            self.data_fetcher.get_yearly(),
            marker = '不適用'
        )
        
        data = non_empty.reset_index().to_dict(orient='records')

        return self.fit_model(data)
    
    
    