from .base import ResponseService
from database import MilvusConnector
from database import MilvusHelper
from llama_index.core.vector_stores import (FilterOperator, MetadataFilter,
                                            MetadataFilters)
from llama_index.core import Settings
from models import QueryResponse
import os
from pymilvus import MilvusClient


class FinancialReportService:

    def __init__(self):
        """
        """
        self.milvus_address = os.getenv("MILVUS_ADDRESS")
        self.milvus_token = os.getenv("MILVUS_TOKEN")
        self.db_connector = MilvusConnector(address=self.milvus_address,
                                            token=self.milvus_token)
        self.milvus_client = MilvusClient(uri=os.getenv('MILVUS_ADDRESS'),
                                          token=os.getenv("MILVUS_TOKEN"))
        self.index = self.db_connector.load_vector_store(
            collection='finance_report')
        self.query_helper = MilvusHelper()
        self.datetime_format = '%Y-%m-%d'


class RAGService(FinancialReportService):

    def __init__(self, ticker: str, year: str, season: str, top_k: int,
                 question: str):
        """
        實作RAG對話頁面
        """

        super().__init__()
        self.ticker = ticker
        self.year = year
        self.season = season
        self.top_k = top_k
        self.question = question

    def _reinit(self, ticker: str, year: str, season: int, top_k: int):
        """
        重新設定指定的ticker, year, season
        """

        self.ticker = ticker
        self.year = year
        self.season = season
        self.top_k = top_k

    def init_query_engine(self):
        """
        初始化/刷新 Query Engine
        """

        filters = MetadataFilters(filters=[
            MetadataFilter(
                key='ticker', operator=FilterOperator.EQ, value=self.ticker),
            MetadataFilter(
                key='year', operator=FilterOperator.EQ, value=self.year),
            MetadataFilter(
                key='season', operator=FilterOperator.EQ, value=self.season),
        ])

        self.query_engine = self.index.as_query_engine(
            filters=filters, similarity_top_k=self.top_k)

    def get_response(self):
        """
        回覆答案
        """
        # if ((ticker, year, season, top_k)
        #         != (self.ticker, self.year, self.season, self.top_k)):
        #     self._reinit(ticker, year, season, top_k)
        response = self.query_engine.query(self.question)
        top_k_node_text = [
            node.node.get_text().replace("\n", " ")
            for node in response.source_nodes
        ]
        return QueryResponse(response=response.response,
                             top_k_candidate=top_k_node_text)
