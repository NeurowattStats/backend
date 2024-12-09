from pydantic import BaseModel
from typing import Union, Optional, Dict, List

class ChipOverall(BaseModel):
    open: Optional[Union[int, float, str]]  # P/E Ratio
    close: Optional[Union[int, float, str]]  # Price-to-Free Cash Flow Ratio
    range: Optional[Union[int, float, str]]  # Price-to-Book Ratio
    volume: Optional[Union[int, float, str]]  # Price-to-Sales Ratio
    last_open: Optional[Union[int, float, str]]  # Enterprise Value-to-Operating Income
    last_close: Optional[Union[int, float, str]]  # Enterprise Value-to-EBIT
    last_range: Optional[Union[int, float, str]]  # Enterprise Value-to-EBITDA
    last_volume: Optional[Union[int, float, str]]  # Enterprise Value-to-Sales
    weeks_range_52: Optional[Union[int, float, str]]
