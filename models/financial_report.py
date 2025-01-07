from pydantic import BaseModel
from typing import Optional, Union, List


class QueryInput(BaseModel):
    """
    對chatBot輸入的問題
    """
    question: Optional[str] = None
    ticker: str
    year: Optional[str] = '2024'
    season: Optional[int] = 2
    top_k: Optional[int] = 3


class QueryResponse(BaseModel):
    """
    與RAG輸入問題得到的response
    """
    response: Optional[str] = "可以查詢關於財報的資料，可以選擇指定的年份與季度"
    top_k_candidate: Optional[List[str]] = []
