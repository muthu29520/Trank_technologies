
from conftest import page

class portfolio_page:

    def __init__(self, page):
        self.page = page

        self.port=page.locator('//a[text()="Portfolio"]')
    def portf_clicking(self):
        self.port.click()
    
