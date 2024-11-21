from neurostats_API.fetchers.value_invest import ValueFetcher
from .base import ResponseService
from models import ValuationOverview, ValuationTable


class ValueResponse(ResponseService):

    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = ValueFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )
        self.full_data = self.data_fetcher.query_data()
        self.yearly_data = self.full_data.get('yearly_data')
        self.years_10_values = self.yearly_data.set_index('year')
        self.daily_data = self.full_data.get('daily_data')

    def get_value_table(self):

        table_df = ResponseService.replace_empty_values(
            data = self.yearly_data,
            marker = '不適用'
        )
    
        result = []

        for column in table_df.columns[1:]:
            column_data = {
                "title": column,
            }
            for i, year in enumerate(table_df['year']):
                column_data[year] = table_df[column].iloc[i]
            result.append(column_data)

        return ValuationTable(
            array = result
        )

    def get_value_overview(self):

        return ValuationOverview(
            P_E = self.daily_data.get('P_E', '不適用'),
            P_FCF = self.daily_data.get('P_FCF', '不適用'),
            P_B = self.daily_data.get('P_B', '不適用'),
            P_S = self.daily_data.get('P_S', '不適用'),
            EV_OPI = self.daily_data.get('EV_OPI', '不適用'),
            EV_EBIT = self.daily_data.get('EV_EBIT', '不適用'),
            EV_EBITDA = self.daily_data.get('EV_EBITDA', '不適用'),
            EV_S = self.daily_data.get('EV_S', '不適用')
        )
        
