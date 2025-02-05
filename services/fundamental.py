# %%
from neurostats_API.fetchers import (
    ProfitLoseFetcher,
    FinanceOverviewFetcher,
    BalanceSheetFetcher,
    MonthRevenueFetcher,
    CashFlowFetcher,
)

from .base import ResponseService
from models import (
    OverviewModel, 
    PerShareModel, 
    ProfitabilityModel, 
    GrowthMomentumModel, 
    FinancialResilienceModel, 
    BalanceSheetModel,
    OperatingIndicatorsModel,
    TitleArray
)
 
# %%
class FundResponse(ResponseService):

    def __init__(self, ticker: str):
        super().__init__()
        self.ticker = ticker

    def _get_data(self, data: dict, key: str, default='不適用'):
        """Retrieve data with a key from the given data structure and handle missing values."""
        non_empty_data = ResponseService.replace_empty_values(
            data = data,
            marker = default
        )
        return non_empty_data.get(key, default)
    
class FundVitals(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.data_fetcher = FinanceOverviewFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )
        self.full_data = self.data_fetcher.query_data()
        self.company_name = self.full_data.get('company_name')

        self.recent_season_vitals = self.full_data.get('seasonal_data', {})
        self.year = self.recent_season_vitals.get('year', '不適用')
        self.season = self.recent_season_vitals.get('season', '不適用')

    def _get_multiple_data(self, fields: list) -> dict:
        """Helper method to retrieve multiple fields from seasonal data."""
        return {field: self._get_data(self.recent_season_vitals, field) for field in fields}

    def get_overview(self) -> OverviewModel:
        """Get a dictionary with the overview of financial data."""
        overview_fields = [
            'revenue', 'gross_profit', 'operating_income', 'net_income',
            'operating_cash_flow', 'invest_cash_flow', 'financing_cash_flow'
        ]
        overview = self._get_multiple_data(overview_fields)
        return OverviewModel(year=self.year, season=self.season, **overview)

    def get_per_share(self) -> PerShareModel:
        """Get a dictionary with per-share financial data."""
        per_share_fields = [
            'revenue_per_share', 'gross_per_share', 'operating_income_per_share',
            'eps', 'operating_cash_flow_per_share', 'fcf_per_share'
        ]
        per_share = FundResponse.format_dict_values(self._get_multiple_data(per_share_fields))
        return PerShareModel(year=self.year, season=self.season, **per_share)

    def get_profitability(self) -> ProfitabilityModel:
        """Get a dictionary with profitability data."""
        profitability_fields = [
            'roa', 'roe', 'gross_over_asset', 'roce', 'gross_profit_margin',
            'operation_profit_rate', 'net_income_rate', 'operating_cash_flow_profit_rate'
        ]
        profitability_raw = self._get_multiple_data(profitability_fields)

        convert_keys = profitability_fields
        
        profitability = FundResponse.format_value_to_percentage(
            data = profitability_raw,
            keys = convert_keys,
            decimal_places = 2
        )
        return ProfitabilityModel(year=self.year, season=self.season, **profitability)

    def get_growth_momentum(self) -> GrowthMomentumModel:
        """Get a dictionary with growth momentum data."""
        growth_momentum_fields = [
            'revenue_YoY', 'gross_prof_YoY', 'operating_income_YoY', 'net_income_YoY',
            'operating_cash_flow_YoY', 'operating_cash_flow_per_share_YoY'
        ]
        growth_momentum_raw = self._get_multiple_data(growth_momentum_fields)

        convert_keys = growth_momentum_fields
        
        growth_momentum = FundResponse.format_value_to_percentage(
            data = growth_momentum_raw,
            keys = convert_keys,
            decimal_places = 2
        )

        return GrowthMomentumModel(year=self.year, season=self.season, **growth_momentum)

    def get_operating_indicators(self) -> OperatingIndicatorsModel:
        
        operating_indicators_fields = [
            'dso', 'account_receive_over_revenue', 'dio', 'inventories_revenue_ratio',
            'dpo', 'cash_of_conversion_cycle', 'asset_turnover', 'applcation_turnover'
        ]
        operating_indicators_raw = self._get_multiple_data(operating_indicators_fields)

        convert_keys =  [
            'account_receive_over_revenue',  'inventories_revenue_ratio',
            'asset_turnover', 'applcation_turnover'
        ]

        operating_indicators = FundResponse.format_value_to_percentage(
            data = operating_indicators_raw,
            keys = convert_keys,
            decimal_places = 2
        )

        operating_indicators = FundResponse.format_dict_values(
            operating_indicators,
            2
        )

        return OperatingIndicatorsModel(year=self.year, season=self.season, **operating_indicators)

    def get_financial_resilience(self) -> FinancialResilienceModel:
        """Get a dictionary with financial resilience data."""
        financial_resilience_fields = [
            'current_ratio', 'quick_ratio', 'debt_to_equity_ratio', 
            'net_debt_to_equity_ratio', 'interest_coverage_ratio', 'debt_to_operating_cash_flow',
            'debt_to_free_cash_flow', 'cash_flow_ratio'
        ]
        financial_resilience_raw = self._get_multiple_data(financial_resilience_fields)

        convert_keys = [
            'current_ratio', 'quick_ratio', 'debt_to_equity_ratio', 
            'net_debt_to_equity_ratio', 'interest_coverage_ratio', 'cash_flow_ratio'
        ]

        financial_resilience = FundResponse.format_value_to_percentage(
            data = financial_resilience_raw,
            keys = convert_keys,
            decimal_places = 2
        )

        financial_resilience = FundResponse.format_dict_values(
            financial_resilience,
            2
        )

        return FinancialResilienceModel(year=self.year, season=self.season, **financial_resilience)

    def get_balance_sheet(self) -> BalanceSheetModel:
        """Get a dictionary with balance sheet data."""
        balance_sheet_fields = [
            'current_assets', 'current_liabilities', 'non_current_assets',
            'non_current_liabilities', 'total_asset', 'total_liabilities', 'equity'
        ]
        balance_sheet = self._get_multiple_data(balance_sheet_fields)
        return BalanceSheetModel(year=self.year, season=self.season, **balance_sheet)


class RevenStatements(FundResponse):

    def __init__(self, ticker: str):
        super().__init__(ticker)
        
        self.data_fetcher = MonthRevenueFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )
        self.full_page = FundResponse.replace_empty_values(
            data = self.data_fetcher.query_data(),
            marker = '不適用'
        )

    def get_month_revenue(self):

        data = self._get_data(self.full_page, 'month_revenue').T.reset_index()
        array = ResponseService.df_to_title_array(
            df=data,
            index_col='year',
            empty_values='不適用'
        )

        return array
    
    def get_revenue_over_years(self):

        data = self._get_data(self.full_page, 'this_month_revenue_over_years').T.reset_index()
        array = ResponseService.df_to_title_array(
            df=data,
            index_col='year',
            empty_values='不適用'
        )
        return array

    def get_revenue_over_years_text(self):
        return self.get_lastest_generation(category='revenue_over_years')
    
    def get_grand_total_over_years(self):

        data = self._get_data(self.full_page, 'grand_total_over_years').T.reset_index()
        array = ResponseService.df_to_title_array(
            df=data,
            index_col='year',
            empty_values='不適用'
        )

        return array
    
    def get_grand_total_over_years_text(self):
        return self.get_lastest_generation(category='grand_total_over_years')

class ProfitLoss(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)

        self.data_fetcher = ProfitLoseFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )

        self.full_page_raw = FundResponse.replace_empty_values(
            data = self.data_fetcher.query_data(),
            marker = '不適用'
        )

        self.full_page = FundResponse.format_values_within_range_to_percentage(
            data = self.full_page_raw,
            keys = list(self.full_page_raw.keys())[2:],
        )

    # Data 
    def get_profit_lose(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'profit_lose',
            reverse=True
        )
    
    def get_grand_total_profit_lose(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_profit_lose',
            reverse=True
        )

    def get_revenue(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'revenue',
            reverse=True
        )

    def get_grand_total_revenue(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_revenue',
            reverse=True
        )
    
    def get_gross_profit(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'gross_profit',
            reverse=True
        )

    def get_grand_total_gross_profit(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_gross_profit',
            reverse=True
        )

    def get_gross_profit_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'gross_profit_percentage',
            reverse=True
        )
    
    def get_grand_total_gross_profit_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_gross_profit_percentage',
            reverse=True
        )
    
    def get_operating_income(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'operating_income',
            reverse=True
        )

    def get_grand_total_operating_income(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_operating_income',
            reverse=True
        )
    
    def get_operating_income_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'operating_income_percentage',
            reverse=True
        )
    
    def get_grand_total_operating_income_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_operating_income_percentage',
            reverse=True
        )
    
    def get_net_income_before_tax(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'net_income_before_tax',
            reverse=True
        )
    
    def get_grand_total_net_income_before_tax(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_net_income_before_tax',
            reverse=True
        )
    
    def get_net_income_before_tax_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'net_income_before_tax_percentage',
            reverse=True
        )
    
    def get_grand_total_net_income_before_tax_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_net_income_before_tax_percentage',
            reverse=True
        )
    
    def get_net_income(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'net_income',
            reverse=True
        )
    
    def get_grand_total_net_income(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_net_income',
            reverse=True
        )
    
    def get_net_income_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'net_income_percentage',
            reverse=True
        )
    
    def get_grand_total_income_percentage(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_income_percentage',
            reverse=True
        )
    
    def get_EPS(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'EPS',
            reverse=True
        )

    def get_EPS_growth(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'EPS_growth',
            reverse=True
        )
    
    def get_grand_total_EPS(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_EPS',
            reverse=True
        )
    
    def get_grand_total_EPS_growth(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key = 'grand_total_EPS_growth',
            reverse=True
        )

    # Content
    def get_revenue_text(self):
        return self.get_lastest_generation(category='revenue')
    
    def get_grand_total_revenue_text(self):
        return self.get_lastest_generation(category='grand_total_revenue')
    
    def get_gross_profit_text(self):
        return self.get_lastest_generation(category='gross_profit')
    
    def get_grand_total_gross_profit_text(self):
        return self.get_lastest_generation(category='grand_total_gross_profit')
    
    def get_gross_profit_percentage_text(self):
        return self.get_lastest_generation(category='gross_profit_percentage')
    
    def get_grand_total_gross_profit_percentage_text(self):
        return self.get_lastest_generation(category='grand_total_gross_profit_percentage')
    
    def get_operating_income_text(self):
        return self.get_lastest_generation(category='operating_income')

    def get_grand_total_operating_income_text(self):
        return self.get_lastest_generation(category='grand_total_operating_income')
    
    def get_operating_income_percentage_text(self):
        return self.get_lastest_generation(category='operating_income_percentage')
    
    def get_grand_total_operating_income_percentage_text(self):
        return self.get_lastest_generation(category='grand_total_operating_income_percentage')
    
    def get_net_income_before_tax_text(self):
        return self.get_lastest_generation(category='net_income_before_tax')
    
    def get_grand_total_net_income_before_tax_text(self):
        return self.get_lastest_generation(category='grand_total_net_income_before_tax')
    
    def get_net_income_before_tax_percentage_text(self):
        return self.get_lastest_generation(category='net_income_before_tax_percentage')
    
    def get_grand_total_net_income_before_tax_percentage_text(self):
        return self.get_lastest_generation(category='grand_total_net_income_before_tax_percentage')
    
    def get_net_income_text(self):
        return self.get_lastest_generation(category='net_income')
    
    def get_grand_total_net_income_text(self):
        return self.get_lastest_generation(category='grand_total_net_income')
    
    def get_net_income_percentage_text(self):
        return self.get_lastest_generation(category='net_income_percentage')
    
    def get_grand_total_income_percentage_text(self):
        return self.get_lastest_generation(category='grand_total_income_percentage')
    
    def get_EPS_text(self):
        return self.get_lastest_generation(category='EPS')
    
    def get_EPS_growth_text(self):
        return self.get_lastest_generation(category='EPS_growth')
    
    def get_grand_total_EPS_text(self):
        return self.get_lastest_generation(category='grand_total_EPS')
    
    def get_grand_total_EPS_growth_text(self):
        return self.get_lastest_generation(category='grand_total_EPS_growth')
    
class BalanceSheet(FundResponse):
    
    def __init__(self, ticker: str):
        super().__init__(ticker)

        # 初始化數據抓取器
        self.data_fetcher = BalanceSheetFetcher(
            ticker=self.ticker,
            db_client=self.mongo_clinet
        )

        # 獲取完整的資產負債表並處理空值
        self.full_page = FundResponse.replace_empty_values(
            data=self.data_fetcher.query_data(),
            marker='不適用'
        )

    def _get_and_format_data(self, key: str, reverse:bool=True):
        """
        通用方法：根據鍵提取資料並轉換為標題數組格式
        :param key: 欲提取的資料鍵（如 'balance_sheet', 'total_asset', 'current_asset' 等）
        :return: TitleArray 實例
        """
        if reverse:
            data = self._get_data(self.full_page, key).T.reset_index()
        else:
            data = self._get_data(self.full_page, key).reset_index()

        array = FundResponse.df_to_title_array(
            df=data,
            index_col='index',
            empty_values='不適用'
        )
        return array

    def get_full_table(self):
        return self._get_and_format_data('balance_sheet')

    def get_total_asset(self):
        return self._get_and_format_data('total_asset')

    def get_current_asset(self):
        return self._get_and_format_data('current_asset')

    def get_non_current_asset(self):
        return self._get_and_format_data('non_current_asset')

    def get_current_debt(self):
        return self._get_and_format_data('current_debt')

    def get_non_current_debt(self):
        return self._get_and_format_data('non_current_debt')

    def get_equity(self):
        return self._get_and_format_data('equity')

    # 以下是 text 方法部分：

    def get_total_asset_text(self):
        return self.get_lastest_generation(category='total_asset')
    
    def get_current_asset_text(self):
        return self.get_lastest_generation(category='current_asset')

    def get_non_current_asset_text(self):
        return self.get_lastest_generation(category='non_current_asset')

    def get_current_debt_text(self):
        return self.get_lastest_generation(category='current_debt')
    
    def get_non_current_debt_text(self):
        return self.get_lastest_generation(category='non_current_debt')

    def get_equity_text(self):
        return self.get_lastest_generation(category='equity')

class CashflowSheet(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

        self.data_fetcher = CashFlowFetcher(
            ticker = self.ticker,
            db_client = self.mongo_clinet
        )
        self.full_page = FundResponse.replace_empty_values(
            data = self.data_fetcher.query_data(),
            marker = '不適用'
        )

    def get_full_table(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key='cash_flow',
            reverse=True
        )
    
    def get_operation(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key='CASHO',
            reverse=True
        )
    
    def get_operation_text(self):
        return self.get_lastest_generation(category='operation')
    
    def get_investment(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key='CASHI',
            reverse=True
        )
    
    def get_investment_text(self):
        return self.get_lastest_generation(category='investment')
    
    def get_fundraising(self):
        return self._get_title_array_from_full_page(
            full_page = self.full_page,
            key='CASHF',
            reverse=True
        )
    
    def get_fundraising_text(self):
        return self.get_lastest_generation(category='fundraising')

class Dividend(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

class Report(FundResponse):

    def __init__(self, ticker):
        super().__init__(ticker)

    
