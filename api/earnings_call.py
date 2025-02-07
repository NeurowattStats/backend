from fastapi import APIRouter, HTTPException 
from services import EarningsCallResponse 
from models import EarningsCallRequest 

router = APIRouter()

@router.post("/presentation")
async def get_presentation(request: EarningsCallRequest):
    try:
        service = EarningsCallResponse(
            ticker=request.ticker, 
            year=request.year, 
            quarter=request.quarter
        )
        
        result = service.get_presentation()

        return result 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
