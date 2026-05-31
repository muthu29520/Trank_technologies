
from config import url
from pages.technologies import techno_page
import pytest

@pytest.mark.smoke
def test_technologies(page):
    page.goto(url)
    tech=techno_page(page)
    tech.eComm_cllicking()
    tech.mobile_app_clicking()
    tech.ai_click()