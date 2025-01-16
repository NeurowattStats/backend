from pydantic import BaseModel

class EarningsCallRequest(BaseModel):
    ticker: str
    year: int 
    quarter: int 