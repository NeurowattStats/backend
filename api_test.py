import pytest
from httpx import AsyncClient, ASGITransport
from main import app

# Function to send POST request and check response
async def test_api(endpoint: str, payload: dict):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(endpoint, json=payload)
    assert response.status_code == 200
    data = response.json()
    return data

# List of all API URLs
api_urls = [
    # Vitals
    "/neurostats/fundamental/vitals/overview",
    "/neurostats/fundamental/vitals/per_share",
    "/neurostats/fundamental/vitals/profitability",
    "/neurostats/fundamental/vitals/growth_momentum",
    "/neurostats/fundamental/vitals/operating_indicators",
    "/neurostats/fundamental/vitals/financial_resilience",
    "/neurostats/fundamental/vitals/balance_sheet",

    # Revenues
    "/neurostats/fundamental/revenue/monthly",
    "/neurostats/fundamental/revenue/this_month",
    "/neurostats/fundamental/revenue/this_month_text",

    # BalanceSheet
    "/neurostats/fundamental/balance_sheet/full_table",
    "/neurostats/fundamental/balance_sheet/total_asset",
    "/neurostats/fundamental/balance_sheet/current_asset",
    "/neurostats/fundamental/balance_sheet/non_current_asset",
    "/neurostats/fundamental/balance_sheet/current_debt",
    "/neurostats/fundamental/balance_sheet/non_current_debt",
    "/neurostats/fundamental/balance_sheet/equity",

    # Cashflow
    "/neurostats/fundamental/cashflow/full_table",
    "/neurostats/fundamental/cashflow/operation",
    "/neurostats/fundamental/cashflow/investment",
    "/neurostats/fundamental/cashflow/fundraising",

    # Valuation
    "/neurostats/valuation/overview",
    "/neurostats/valuation/table",

    # Tech
    "/neurostats/tech/vitals",
    "/neurostats/tech/daily",
    "/neurostats/tech/weekly",
    "/neurostats/tech/monthly",
    "/neurostats/tech/quarterly",
    "/neurostats/tech/yearly",
]

# Test data
payload = {
    "ticker": "2330"  # Replace with the ticker you want to test
}

# Run tests for each URL
@pytest.mark.asyncio
async def test_all_apis():
    for url in api_urls:
        data = await test_api(url, payload)
        
        # You can add additional assertions for each API response here
        # Example:
        # assert "some_key" in data

        # Optional: print out the response for debugging
        print(f"Tested URL: {url}")
        print(f"Response: {data}")
        print("-" * 50)
