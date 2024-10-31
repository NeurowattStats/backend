from pydantic import BaseModel
from typing import Optional

class TickerRequest(BaseModel):
    ticker: str                          # "2330"
    end_date: Optional[str] = None       # "2199-12-31"
    start_date: Optional[str] = None     # "2018-01-01"
    n_days : Optional[int] = None        # 90 

