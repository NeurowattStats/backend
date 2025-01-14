from fastapi import APIRouter, HTTPException
from models import QueryInput, QueryResponse
from services import RAGService
from utils import handle_request, handle_RAG_query

router = APIRouter()

@router.post("/financial_report/query", response_model=QueryResponse)
async def get_RAG_response(request: QueryInput):
    try:
        service = RAGService(
            ticker=request.ticker,
            top_k=request.top_k,
            zone=request.zone
        )
        
        response = service.get_response(request.question)

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))
