from pydantic import BaseModel
from typing import List, Optional, Union
import datetime

class TechBasicIndexes(BaseModel):
    date: List[datetime.datetime]
    open: List[Optional[Union[float, str]]]
    high: List[Optional[Union[float, str]]]
    low: List[Optional[Union[float, str]]]
    close: List[Optional[Union[float, str]]]
    volume: List[Optional[Union[int, str]]]
    SMA5: List[Optional[Union[float, str]]]
    SMA20: List[Optional[Union[float, str]]]
    SMA60: List[Optional[Union[float, str]]]
    EMA5: List[Optional[Union[float, str]]]
    EMA20: List[Optional[Union[float, str]]]
    EMA40: List[Optional[Union[float, str]]]
    EMA12: List[Optional[Union[float, str]]]
    EMA26: List[Optional[Union[float, str]]]
    RSI7: List[Optional[Union[float, str]]]
    RSI14: List[Optional[Union[float, str]]]
    RSI21: List[Optional[Union[float, str]]]
    MACD: List[Optional[Union[float, str]]]
    signal_line: List[Optional[Union[float, str]]]
    middle_band: List[Optional[Union[float, str]]]
    upper_band: List[Optional[Union[float, str]]]
    lower_band: List[Optional[Union[float, str]]]
    percent_b: List[Optional[Union[float, str]]]
    BBW: List[Optional[Union[float, str]]]
    ATR: List[Optional[Union[float, str]]]

class TechDailyIndexes(BaseModel):
    date: List[datetime.datetime]
    open: List[Optional[Union[float, str]]]
    high: List[Optional[Union[float, str]]]
    low: List[Optional[Union[float, str]]]
    close: List[Optional[Union[float, str]]]
    volume: List[Optional[Union[int, str]]]
    SMA5: List[Optional[Union[float, str]]]
    SMA20: List[Optional[Union[float, str]]]
    SMA60: List[Optional[Union[float, str]]]
    EMA5: List[Optional[Union[float, str]]]
    EMA20: List[Optional[Union[float, str]]]
    EMA40: List[Optional[Union[float, str]]]
    EMA12: List[Optional[Union[float, str]]]
    EMA26: List[Optional[Union[float, str]]]
    RSI7: List[Optional[Union[float, str]]]
    RSI14: List[Optional[Union[float, str]]]
    RSI21: List[Optional[Union[float, str]]]
    MACD: List[Optional[Union[float, str]]]
    signal_line: List[Optional[Union[float, str]]]
    middle_band: List[Optional[Union[float, str]]]
    upper_band: List[Optional[Union[float, str]]]
    lower_band: List[Optional[Union[float, str]]]
    percent_b: List[Optional[Union[float, str]]]
    BBW: List[Optional[Union[float, str]]]
    ATR: List[Optional[Union[float, str]]]
    EMA_cycle: List[Optional[str]]
    EMA_cycle_instructions: List[Optional[str]]
    close_yesterday: List[Optional[Union[float, str]]]
    day_trading_signal: List[Optional[str]]


class TechIndexes(BaseModel):
    date: datetime.datetime
    open: Optional[Union[float, str]]
    high: Optional[Union[float, str]]
    low: Optional[Union[float, str]]
    close: Optional[Union[float, str]]
    volume: Optional[Union[int, str]]
    SMA5: Optional[Union[float, str]]
    SMA20: Optional[Union[float, str]]
    SMA60: Optional[Union[float, str]]
    EMA5: Optional[Union[float, str]]
    EMA20: Optional[Union[float, str]]
    EMA40: Optional[Union[float, str]]
    EMA12: Optional[Union[float, str]]
    EMA26: Optional[Union[float, str]]
    RSI7: Optional[Union[float, str]]
    RSI14: Optional[Union[float, str]]
    RSI21: Optional[Union[float, str]]
    MACD: Optional[Union[float, str]]
    signal_line: Optional[Union[float, str]]
    middle_band: Optional[Union[float, str]]
    upper_band: Optional[Union[float, str]]
    lower_band: Optional[Union[float, str]]
    percent_b: Optional[Union[float, str]]
    BBW: Optional[Union[float, str]]
    ATR: Optional[Union[float, str]]
    EMA_cycle: Optional[str]
    EMA_cycle_instructions: Optional[str]
    close_yesterday: Optional[Union[float, str]]
    day_trading_signal: Optional[str]

# 定義包含多行的列表模型
class TechIndexesList(BaseModel):
    array: List[TechIndexes]