
from conftest import page

class contact_page:

    def __init__(self, page):
        self.page = page

        self.contact=page.locator('(//a[text()="Contact us"])[1]')
    def cont_clicking(self):
        self.contact.click()
