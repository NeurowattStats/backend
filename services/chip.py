from neurostats_API.fetchers.institution import InstitutionFetcher
from .base import ResponseService
from models import TitleArray, InstitutionOverall
import pandas as pd

class ChipResponse(ResponseService):

    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker

class InstitutionResponse(ChipResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

        self.data_fetcher = InstitutionFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )

        self.full_data = ResponseService.replace_empty_values(
            data = self.data_fetcher.query_data(),
            marker = '不適用'
        )

    def get_overall(self):

        overall = self.full_data.get('price')
        if '52weeks_range' in overall:
            overall['weeks_range_52'] = overall.pop('52weeks_range')

        return InstitutionOverall(**overall)
    
    def get_overall_text(self):

        return {'content':'in process'}
    
    def get_latest(self):

        latest_trading = self.full_data.get('latest_trading').get('table')
        
        return self._transform_latest_table(latest_trading)
    
    def get_history(self):

        history = self.full_data.get('annual_trading').drop('date',axis=1)
        history_t = history.T.reset_index()
        array = ChipResponse.df_to_title_array(
            df=history_t,
            index_col='index'
        )

        return TitleArray(array = array)
    

    def _transform_latest_table(df:pd.DataFrame):
        result = {}
        for category in df['category'].unique():
            category_data = df[df['category'] == category]
            category_dict = {}
            for variable in category_data['variable'].unique():
                variable_data = category_data[category_data['variable'] == variable].iloc[0]
                category_dict[variable] = {
                    'buy': float(variable_data['buy']),
                    'over_buy_sell': float(variable_data['over_buy_sell']),
                    'sell': float(variable_data['sell'])
                }
            result[category] = category_dict
        return result


class MarginTrade(ChipResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

    def get_overall(self):

        pass
    
    def get_overall_text(self):

        return {'content':'in process'}
    
    def get_latest(self):

        pass

    def get_history(self):
        
        pass

    
    
        

        
        