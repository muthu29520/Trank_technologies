from config import url
from pages.blogs import blogs_page
import pytest

@pytest.mark.smoke
def test_blog(page):
    page.goto(url)
    blo=blogs_page(page)
    blo.blog_clicking()