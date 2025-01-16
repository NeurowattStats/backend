from .base import ResponseService
import os

class EarningsCallResponse(ResponseService):
    """Service for handling earnings call analysis operations."""
    def __init__(self, ticker: str, year: int, quarter: int):
        """Initialize the earnings call service."""
        super().__init__()
        self.mongo_address = os.getenv("MONGO_URI")

        self.ticker = ticker
        self.year = year
        self.quarter = quarter
        
        self.earnings_call_collection = self.db_connector.point_collection(
            name="earnings_calls",
            collection="html_reports"
        )

    def get_presentation(self):
        """
        Get presentation content for specific ticker, year, and quarter.
        
        :param year: Year of the presentation
        :param quarter: Quarter of the presentation
        :returns: Presentation content or message if not found
        """
        try:
            result = self.query_helper.find_the_latest(
                collection=self.earnings_call_collection,
                query={
                    "ticker": self.ticker,
                    "year": self.year,
                    "quarter": self.quarter
                }
            )

            if not result:
                return f"股票代號 {self.ticker} 於 {self.year}年第{self.quarter}季的法說會分析資料目前尚未更新"

            return result.get("content")
            
        except Exception as e:
            return f"Error retrieving presentation for {self.ticker}: {str(e)}"