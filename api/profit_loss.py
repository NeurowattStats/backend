from fastapi import APIRouter

from models import (
    TickerRequest,
    TitleArray
)

from services import (
    ProfitLoss
)

from utils import handle_request

router = APIRouter()

@router.post("/profit_lose")
async def get_profit_lose(request: TickerRequest):

    profit_lose = handle_request(
        ticker = request.ticker, 
        service_class =ProfitLoss, 
        method_name ='get_profit_lose', 
        include_content=False
    )

    grand_total_profit_lose = handle_request(
        ticker =request.ticker, 
        service_class =ProfitLoss, 
        method_name ='get_grand_total_profit_lose', 
        include_content=False
    )

    return [profit_lose, grand_total_profit_lose]

@router.post("/revenue")
async def get_revenue(request: TickerRequest):

    revenue = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_revenue', 
        include_content=request.include_content,
        content_method_name = 'get_revenue_text'
    )

    grand_total_revenue = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_revenue', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_revenue_text'
    )

    return [revenue, grand_total_revenue]


@router.post("/gross_profit")
async def get_gross_profit(request: TickerRequest):

    gross_profit = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_gross_profit', 
        include_content=request.include_content,
        content_method_name = 'get_gross_profit_text'
    )

    grand_total_gross_profit = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_gross_profit', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_gross_profit_text'
    )

    return [gross_profit, grand_total_gross_profit]

@router.post("/gross_profit_percentage")
async def get_gross_profit_percentage(request: TickerRequest):

    gross_profit_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_gross_profit_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_gross_profit_percentage_text'
    )

    grand_total_gross_profit_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_gross_profit_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_gross_profit_percentage_text'
    )

    return [gross_profit_percentage, grand_total_gross_profit_percentage]

@router.post("/operating_income")
async def get_operating_income(request: TickerRequest):

    operating_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_operating_income', 
        include_content=request.include_content,
        content_method_name = 'get_operating_income_text'
    )

    grand_total_operating_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_operating_income', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_operating_income_text'
    )

    return [operating_income, grand_total_operating_income]

@router.post("/operating_income_percentage")
async def get_operating_income_percentage(request: TickerRequest):

    operating_income_percentage =  handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_operating_income_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_operating_income_percentage_text'
    )

    grand_total_operating_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_operating_income_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_operating_income_percentage_text'
    )

    return [operating_income_percentage, grand_total_operating_income_percentage]

@router.post("/net_income_before_tax")
async def get_net_income_before_tax(request: TickerRequest):

    net_income_before_tax = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_before_tax', 
        include_content=request.include_content,
        content_method_name = 'get_net_income_before_tax_text'
    )

    grand_total_net_income_before_tax = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income_before_tax', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_net_income_before_tax_text'
    )

    return [net_income_before_tax, grand_total_net_income_before_tax]

@router.post("/net_income_before_tax_percentage")
async def get_net_income_before_tax_percentage(request: TickerRequest):

    net_income_before_tax_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_before_tax_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_net_income_before_tax_percentage_text'
    )

    grand_total_net_income_before_tax_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income_before_tax_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_net_income_before_tax_percentage_text'
    )

    return [net_income_before_tax_percentage, grand_total_net_income_before_tax_percentage]

@router.post("/get_net_income")
async def get_net_income(request: TickerRequest):

    net_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income', 
        include_content=request.include_content,
        content_method_name = 'get_net_income_text'
    )

    grand_total_net_income = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_net_income', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_net_income_text'
    )

    return [net_income, grand_total_net_income]

@router.post("/net_income_percentage")
async def get_net_income_percentage(request: TickerRequest):

    net_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_net_income_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_net_income_percentage_text'
    )

    grand_total_income_percentage = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_grand_total_income_percentage', 
        include_content=request.include_content,
        content_method_name = 'get_grand_total_income_percentage_text'
    )

    return [net_income_percentage, grand_total_income_percentage]

@router.post("/EPS")
async def get_EPS(request: TickerRequest):

    EPS = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_EPS', 
        include_content=request.include_content,
        content_method_name = 'get_EPS_text'
    )

    EPS_growth = handle_request(
        request.ticker, 
        ProfitLoss, 
        'get_EPS_growth', 
        include_content=request.include_content,
        content_method_name = 'get_EPS_growth_text'
    )

    return [EPS, EPS_growth]