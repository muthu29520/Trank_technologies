
from config import url
from pages.verticales import vertical_page
import pytest

@pytest.mark.smoke
def test_vertical(page):
    page.goto(url)
    ver = vertical_page(page)
    ver.trading_clicking()
    ver.retail_ecomm_clicking()
    ver.healthcare_clicking()
    ver.fintech_clicking()
    ver.custom_clicking()
    
