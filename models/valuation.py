from pydantic import BaseModel
from typing import Union, Optional, Dict

class ValuationOverview(BaseModel):
    P_E: Optional[Union[float, str]]  # P/E Ratio
    P_FCF: Optional[Union[float, str]]  # Price-to-Free Cash Flow Ratio
    P_B: Optional[Union[float, str]]  # Price-to-Book Ratio
    P_S: Optional[Union[float, str]]  # Price-to-Sales Ratio
    EV_OPI: Optional[Union[float, str]]  # Enterprise Value-to-Operating Income
    EV_EBIT: Optional[Union[float, str]]  # Enterprise Value-to-EBIT
    EV_EBITDA: Optional[Union[float, str]]  # Enterprise Value-to-EBITDA
    EV_S: Optional[Union[float, str]]  # Enterprise Value-to-Sales


class ValuationTable(BaseModel):
    P_E: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 市盈率
    P_FCF: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 自由現金流市盈率
    P_B: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 市帳率
    P_S: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 市銷率
    EV_OPI: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 企業價值/操作利潤
    EV_EBIT: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 企業價值/息稅前利潤
    EV_EBITDA: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 企業價值/息稅折舊攤銷前利潤
    EV_S: Optional[Dict[Union[int, str], Union[float, str]]] = None  # 企業價值/銷售額