from fastapi import APIRouter, HTTPException
from models import QueryInput, QueryResponse
from services import RAGService
from utils import handle_request, handle_RAG_query

router = APIRouter()


@router.post("/financial_report")
async def init_RAG(request: QueryInput):
    handle_RAG_query(ticker=request.ticker,
                     year=request.year,
                     season=request.season,
                     top_k=request.top_k,
                     question=request.question,
                     service_class=RAGService,
                     method_name='init_query_engine',
                     include_content=False)


@router.post("/financial_report/query", response_model=QueryResponse)
async def get_RAG_response(request: QueryInput):
    response = handle_RAG_query(ticker=request.ticker,
                                year=request.year,
                                season=request.season,
                                top_k=request.top_k,
                                question=request.question,
                                service_class=RAGService,
                                method_name='get_response',
                                include_content=False)

    return response
