from config import url
from pages.childpage import child_page

import pytest
@pytest.mark.smoke
def test_child(page):
    page.goto(url)
    chi=child_page(page)
    chi.child_click()
