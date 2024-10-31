from pydantic import BaseModel
from typing import Union, Optional

class ValuationOverview(BaseModel):
    PE_Ratio: Optional[Union[float, str]]  # P/E Ratio
    PFCF_Ratio: Optional[Union[float, str]]  # Price-to-Free Cash Flow Ratio
    PB_Ratio: Optional[Union[float, str]]  # Price-to-Book Ratio
    PS_Ratio: Optional[Union[float, str]]  # Price-to-Sales Ratio
    EV_OPI_Ratio: Optional[Union[float, str]]  # Enterprise Value-to-Operating Income
    EV_EBIT_Ratio: Optional[Union[float, str]]  # Enterprise Value-to-EBIT
    EV_EBITDA_Ratio: Optional[Union[float, str]]  # Enterprise Value-to-EBITDA
    EV_S_Ratio: Optional[Union[float, str]]  # Enterprise Value-to-Sales


