from .base import ResponseService


class ValueResponse(ResponseService):

    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self._get_10_years_values()
    
    def get_value_table(self):

        yearly_data = self.years_10_values['yearly_data'].set_index('year').fillna("不適用")
        
        return yearly_data.to_dict()
    
    def get_value_overview(self):

        daily_data = self.years_10_values['daily_data']

        return {
            'P/E_Ratio': daily_data.get('P_E', '不適用'),
            'P/FCF_Ratio': daily_data.get('P_FCF', '不適用'),
            'P/B_Ratio': daily_data.get('P_B', '不適用'),
            'P/S_Ratio': daily_data.get('P_S', '不適用'),
            'EV/OPI_Ratio': daily_data.get('EV_OPI', '不適用'),
            'EV/EBIT_Ratio': daily_data.get('EV_EBIT', '不適用'),
            'EV/EBITDA_Ratio': daily_data.get('EV_EBITDA', '不適用'),
            'EV/S_Ratio': daily_data.get('EV_S', '不適用'),
        }

    def _get_10_years_values(self):
        
        self.years_10_values = self.data_fetcher.get_value_sheet(self.ticker)


        