from config import url
from pages.portfolio import portfolio_page
import pytest

@pytest.mark.smoke
def test_portfolio(page):
    page.goto(url)
    portfo=portfolio_page(page)
    portfo.portf_clicking()