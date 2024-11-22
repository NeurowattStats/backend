from pydantic import BaseModel
from typing import Union, Optional, Dict, List

class ValuationOverview(BaseModel):
    P_E: Optional[Union[float, str]]  # P/E Ratio
    P_FCF: Optional[Union[float, str]]  # Price-to-Free Cash Flow Ratio
    P_B: Optional[Union[float, str]]  # Price-to-Book Ratio
    P_S: Optional[Union[float, str]]  # Price-to-Sales Ratio
    EV_OPI: Optional[Union[float, str]]  # Enterprise Value-to-Operating Income
    EV_EBIT: Optional[Union[float, str]]  # Enterprise Value-to-EBIT
    EV_EBITDA: Optional[Union[float, str]]  # Enterprise Value-to-EBITDA
    EV_S: Optional[Union[float, str]]  # Enterprise Value-to-Sales
