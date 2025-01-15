from pydantic import BaseModel
from typing import Optional, Union, List


class TickerRequest(BaseModel):
    """
    功能:單純輸入ticker
    目標:要求回應可選的財報列表
    """
    ticker: str

class FinanceReportRequest(BaseModel):
    """
    指定財報的request
    """

    ticker: str
    year: Optional[str] = '2024'
    season: Optional[str] = '2'
    top_k: Optional[int] = 3
    zone: Optional[str] = 'tw'


class QueryInput(BaseModel):
    """
    對chatBot輸入的問題
    """
    question: Optional[str] = None
    ticker: str
    top_k: Optional[int] = 3
    zone: Optional[str] = 'tw'

class QueryResponse(BaseModel):
    """
    與RAG輸入問題得到的response
    """
    response: Optional[str] = "可以查詢關於財報的資料，可以選擇指定的年份與季度"
    top_k_candidate: Optional[List[str]] = []
