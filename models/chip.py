from pydantic import BaseModel
from typing import Union, Optional, Dict, List

class InstitutionOverall(BaseModel):
    open: Optional[Union[float, str]]  # P/E Ratio
    close: Optional[Union[float, str]]  # Price-to-Free Cash Flow Ratio
    range: Optional[Union[float, str]]  # Price-to-Book Ratio
    volume: Optional[Union[float, str]]  # Price-to-Sales Ratio
    last_open: Optional[Union[float, str]]  # Enterprise Value-to-Operating Income
    last_close: Optional[Union[float, str]]  # Enterprise Value-to-EBIT
    last_range: Optional[Union[float, str]]  # Enterprise Value-to-EBITDA
    last_volume: Optional[Union[float, str]]  # Enterprise Value-to-Sales
    weeks_range_52: Optional[Union[float, str]]
