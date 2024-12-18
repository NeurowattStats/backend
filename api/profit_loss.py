from fastapi import APIRouter, HTTPException
from models import (
    TickerRequest,
    TitleArray
)
from services import (
    ProfitLoss
)
from utils import handle_request
from database.connection import redis_connector
import json  # Import json for serialization

router = APIRouter()



@router.post("/profit_lose")
async def get_profit_lose(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_get_profit_lose"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    profit_lose = handle_request(
        ticker=request.ticker, 
        service_class=ProfitLoss, 
        method_name='get_profit_lose', 
        include_content=False
    )

    grand_total_profit_lose = handle_request(
        ticker=request.ticker, 
        service_class=ProfitLoss, 
        method_name='get_grand_total_profit_lose', 
        include_content=False
    )

    redis_connector.set(cache_key, json.dumps([profit_lose, grand_total_profit_lose]))  # Serialize data
    return [profit_lose, grand_total_profit_lose]

@router.post("/revenue")
async def get_revenue(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_revenue_text_get_grand_total_revenue_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    revenue = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_revenue', 
        include_content=request.include_content,
        content_method_name='get_revenue_text'
    )

    grand_total_revenue = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_revenue', 
        include_content=request.include_content,
        content_method_name='get_grand_total_revenue_text'
    )

    redis_connector.set(cache_key, json.dumps([revenue, grand_total_revenue]))  # Serialize data
    return [revenue, grand_total_revenue]

@router.post("/gross_profit")
async def get_gross_profit(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_gross_profit_text_get_grand_total_gross_profit_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    gross_profit = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_gross_profit', 
        include_content=request.include_content,
        content_method_name='get_gross_profit_text'
    )

    grand_total_gross_profit = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_gross_profit', 
        include_content=request.include_content,
        content_method_name='get_grand_total_gross_profit_text'
    )

    redis_connector.set(cache_key, json.dumps([gross_profit, grand_total_gross_profit]))  # Serialize data
    return [gross_profit, grand_total_gross_profit]

@router.post("/gross_profit_percentage")
async def get_gross_profit_percentage(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_gross_profit_percentage_text_get_grand_total_gross_profit_percentage_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    gross_profit_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_gross_profit_percentage', 
        include_content=request.include_content,
        content_method_name='get_gross_profit_percentage_text'
    )

    grand_total_gross_profit_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_gross_profit_percentage', 
        include_content=request.include_content,
        content_method_name='get_grand_total_gross_profit_percentage_text'
    )

    redis_connector.set(cache_key, json.dumps([gross_profit_percentage, grand_total_gross_profit_percentage]))  # Serialize data
    return [gross_profit_percentage, grand_total_gross_profit_percentage]

@router.post("/operating_income")
async def get_operating_income(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_operating_income_text_get_grand_total_operating_income_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    operating_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_operating_income', 
        include_content=request.include_content,
        content_method_name='get_operating_income_text'
    )

    grand_total_operating_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_operating_income', 
        include_content=request.include_content,
        content_method_name='get_grand_total_operating_income_text'
    )

    redis_connector.set(cache_key, json.dumps([operating_income, grand_total_operating_income]))  # Serialize data
    return [operating_income, grand_total_operating_income]

@router.post("/operating_income_percentage")
async def get_operating_income_percentage(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_operating_income_percentage_text_get_grand_total_operating_income_percentage_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    operating_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_operating_income_percentage', 
        include_content=request.include_content,
        content_method_name='get_operating_income_percentage_text'
    )

    grand_total_operating_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_operating_income_percentage', 
        include_content=request.include_content,
        content_method_name='get_grand_total_operating_income_percentage_text'
    )

    redis_connector.set(cache_key, json.dumps([operating_income_percentage, grand_total_operating_income_percentage]))  # Serialize data
    return [operating_income_percentage, grand_total_operating_income_percentage]

@router.post("/net_income_before_tax")
async def get_net_income_before_tax(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_net_income_before_tax_text_get_grand_total_net_income_before_tax_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    net_income_before_tax = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_before_tax', 
        include_content=request.include_content,
        content_method_name='get_net_income_before_tax_text'
    )

    grand_total_net_income_before_tax = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income_before_tax', 
        include_content=request.include_content,
        content_method_name='get_grand_total_net_income_before_tax_text'
    )

    redis_connector.set(cache_key, json.dumps([net_income_before_tax, grand_total_net_income_before_tax]))  # Serialize data
    return [net_income_before_tax, grand_total_net_income_before_tax]

@router.post("/net_income_before_tax_percentage")
async def get_net_income_before_tax_percentage(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_net_income_before_tax_percentage_text_get_grand_total_net_income_before_tax_percentage_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    net_income_before_tax_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_before_tax_percentage', 
        include_content=request.include_content,
        content_method_name='get_net_income_before_tax_percentage_text'
    )

    grand_total_net_income_before_tax_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income_before_tax_percentage', 
        include_content=request.include_content,
        content_method_name='get_grand_total_net_income_before_tax_percentage_text'
    )

    redis_connector.set(cache_key, json.dumps([net_income_before_tax_percentage, grand_total_net_income_before_tax_percentage]))  # Serialize data
    return [net_income_before_tax_percentage, grand_total_net_income_before_tax_percentage]

@router.post("/get_net_income")
async def get_net_income(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_net_income_text_get_grand_total_net_income_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    net_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income', 
        include_content=request.include_content,
        content_method_name='get_net_income_text'
    )

    grand_total_net_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income', 
        include_content=request.include_content,
        content_method_name='get_grand_total_net_income_text'
    )

    redis_connector.set(cache_key, json.dumps([net_income, grand_total_net_income]))  # Serialize data
    return [net_income, grand_total_net_income]

@router.post("/net_income_percentage")
async def get_net_income_percentage(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_net_income_percentage_text_get_grand_total_income_percentage_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    net_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_percentage', 
        include_content=request.include_content,
        content_method_name='get_net_income_percentage_text'
    )

    grand_total_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_income_percentage', 
        include_content=request.include_content,
        content_method_name='get_grand_total_income_percentage_text'
    )

    redis_connector.set(cache_key, json.dumps([net_income_percentage, grand_total_income_percentage]))  # Serialize data
    return [net_income_percentage, grand_total_income_percentage]

@router.post("/EPS")
async def get_EPS(request: TickerRequest):
    cache_key = f"{request.ticker}:ProfitLoss_{request.include_content}_get_EPS_text_get_EPS_growth_text"
    cached_data = redis_connector.get(cache_key)

    if cached_data:
        return json.loads(cached_data)  # Deserialize cached data

    EPS = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_EPS', 
        include_content=request.include_content,
        content_method_name='get_EPS_text'
    )

    EPS_growth = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_EPS_growth', 
        include_content=request.include_content,
        content_method_name='get_EPS_growth_text'
    )

    redis_connector.set(cache_key, json.dumps([EPS, EPS_growth]))  # Serialize data
    return [EPS, EPS_growth]
