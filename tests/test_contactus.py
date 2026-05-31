
from config import url
from pages.contact import contact_page

import pytest
@pytest.mark.smoke

def test_contactus(page):
    page.goto(url)
    cont=contact_page(page)
    cont.cont_clicking()
