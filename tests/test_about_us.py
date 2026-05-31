
from config import url
from pages.aboutus import about_page
import pytest

@pytest.mark.smoke
def test_about_us(page):
    page.goto(url)
    abo=about_page(page)
    abo.aboutus_clicking()