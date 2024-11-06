from fastapi import APIRouter, HTTPException

from models import ValuationOverview, TickerRequest
from services import ValueResponse

router = APIRouter()

@router.post("/overview", response_model=ValuationOverview)
async def get_overview(request: TickerRequest):

    try:
        responser = ValueResponse(ticker=request.ticker)
        valuation_overview = responser.get_value_overview()

        return ValuationOverview(
            PE_Ratio=valuation_overview.get('P/E_Ratio'),
            PFCF_Ratio=valuation_overview.get('P/FCF_Ratio'),
            PB_Ratio=valuation_overview.get('P/B_Ratio'),
            PS_Ratio=valuation_overview.get('P/S_Ratio'),
            EV_OPI_Ratio=valuation_overview.get('EV/OPI_Ratio'),
            EV_EBIT_Ratio=valuation_overview.get('EV/EBIT_Ratio'),
            EV_EBITDA_Ratio=valuation_overview.get('EV/EBITDA_Ratio'),
            EV_S_Ratio=valuation_overview.get('EV/S_Ratio')
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/table")
async def get_table(request: TickerRequest):

    try:
        responser = ValueResponse(ticker=request.ticker)

        return responser.get_value_table()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))