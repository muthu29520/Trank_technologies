
from conftest import page

class about_page:

    def __init__(self, page):
        self.page = page

        self.about=page.locator('(//a[text()="About us"])[1]')

    def aboutus_clicking(self):
        self.about.click()