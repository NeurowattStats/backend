from pydantic import BaseModel
from typing import Union, Dict, List, Optional

class TitleArray(BaseModel):
    content : Optional[Dict[Union[str], Union[str]]] = None
    array: List[Dict[Union[float, str], Union[float, str]]]
