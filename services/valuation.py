from .base import ResponseService


class ValueResponse(ResponseService):

    def __init__(self, ticker:str):
        super().__init__()
        self.ticker = ticker
        self._get_10_years_values()
    
    def get_value_table(self):
        
        return self.years_10_values
    
    def get_value_overview(self):
        
        return {key: value["Past_4_Quarters"] for key, value in self.years_10_values.items()}

    def _get_10_years_values(self):
        
        self.years_10_values = self.full_fake['years_10_values']


        