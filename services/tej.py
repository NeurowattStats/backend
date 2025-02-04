from neurostats_API.fetchers import (
    FinanceReportFetcher,
)

from .base import ResponseService


class TEJService(ResponseService):

    def __init__(self):
        super().__init__()
        self.ticker = None
        self.data_fetcher = None

    def get_serial_data_without_growth(self):
        """
        API呼叫單純每季的數值(無成長率)
        """
        return self._get_data_without_growth(
            fetch_mode=self.data_fetcher.FetchMode.QOQ_NOCAL,
            report_type="Q"
        )

    def get_vertical_data_without_growth(self):
        """
        API呼叫單純每年該季的數值(無成長率)
        """
        return self._get_data_without_growth(
            fetch_mode=self.data_fetcher.FetchMode.YOY_NOCAL,
            report_type="Q"
        )
    
    def get_serial_data_with_growth(self):
        """
        API呼叫單純每季的數值(有成長率)
        """

        return self._get_data_with_growth(
            fetch_mode=self.data_fetcher.FetchMode.QOQ,
            report_type='Q'
        )

    def _get_data_without_growth(self, fetch_mode, start_date=None, report_type="Q"):
        try:
            data = self.data_fetcher.get(
                self.ticker,
                fetch_mode=fetch_mode,
                report_type=report_type,
                start_date=start_date,
            )

            data = data.T.reset_index()

            data = ResponseService.replace_empty_values(
                data, 
                marker='不適用'
            )
            array = self.df_to_title_array(
                df=data,
                index_col='index'
            )

            return array
        except Exception as e:
            return f"Error retriving TEJ data for {self.ticker} : {str(e)}"
    
    def _get_data_with_growth(self, fetch_mode, start_date=None, report_type = 'Q'):
        try:
            data = self.data_fetcher.get(
                self.ticker,
                fetch_mode=fetch_mode,
                report_type=report_type,
                start_date=start_date,
            )
            for key, df in data.items():
                df = df.rename(index = {x : f"{key}_{x}" for x in df.index})
                df = df.T.reset_index()
                df = ResponseService.replace_empty_values(
                    df, 
                    marker='不適用'
                )

                data[key] = self.df_to_title_array(
                    df=df,
                    index_col='index'
                )
                
            dfs  = []
            for df in data.values():
                dfs += df

            return dfs
        except Exception as e:
            return f"Error retriving TEJ data for {self.ticker} : {str(e)}"

class TEJFinanceStatement(TEJService):

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = FinanceReportFetcher(
            mongo_uri=self.mongo_address, 
            db_name="company", 
            collection_name="TWN/AINVFQ1"
        )


class TEJCompanySelfSettlement(TEJService):

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.data_fetcher = FinanceReportFetcher(
            mongo_uri=self.mongo_address, 
            db_name="company", 
            collection_name="TWN/AFESTM1"
        )
