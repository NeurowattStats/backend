import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_get_finance_data():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/vitals/finance_data", json={"ticker": "2330"})
    assert response.status_code == 200
    data = response.json()
    assert "quarter" in data
    assert "operating_revenue" in data

@pytest.mark.asyncio
async def test_get_per_share():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/vitals/per_share", json={"ticker": "2330"})
    assert response.status_code == 200
    data = response.json()
    assert "revenue_per_share" in data
    assert "earnings_per_share_eps" in data

@pytest.mark.asyncio
async def test_get_ratios():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/vitals/ratios", json={"ticker": "2330"})
    assert response.status_code == 200
    data = response.json()
    assert "return_on_assets_roa" in data
    assert "gross_profit_margin" in data

@pytest.mark.asyncio
async def test_get_monthly_revenue():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/revenue/monthly", json={"ticker": "2330"})
    assert response.status_code == 200
    assert response.json()  # Confirm data is returned

@pytest.mark.asyncio
async def test_get_this_month_revenue():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/revenue/this_month", json={"ticker": "2330"})
    assert response.status_code == 200
    assert response.json()  # Confirm data is returned

@pytest.mark.asyncio
async def test_get_this_month_text():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/fundamental/revenue/this_month_text", json={"ticker": "2330"})
    assert response.status_code == 200
    assert response.json()  # Confirm data is returned

@pytest.mark.asyncio
async def test_get_valuation_overview():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/valuation/overview", json={"ticker": "2330"})
    assert response.status_code == 200
    data = response.json()
    assert "PE_Ratio" in data
    assert "PS_Ratio" in data

@pytest.mark.asyncio
async def test_get_valuation_table():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/neurostats/valuation/table", json={"ticker": "2330"})
    assert response.status_code == 200
    assert response.json()  # Confirm data is returned
