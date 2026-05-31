
from config import url
from pages.footer import foot_page
import pytest

@pytest.mark.smoke
def test_footer(page):
    page.goto(url)
    foot=foot_page(page)
    foot.footers_clicking()