
from conftest import page

class child_page:

    def __init__(self, page):
        self.page = page
        #self.ecommerece_development=page.locator('//a[text()="eCommerce Development"]')
        self.website_develop=page.locator('//a[text()="Website Development"]')
        self.android_app=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.android_page=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_development=page.locator('//a[text()="App Development" and contains(@href,"app-development-company")]')
        self.eComm_dropdown=page.locator('(//span[@class="toggle-btn"])[1]')
        self.android_dropdown=page.locator('(//span[@class="toggle-btn"])[2]')
        self.hybrid_app=page.locator('(//a[text()="Hybrid Mobile App Development"])[1]') 
       
     
    def child_click(self):
        def _open_link(locator):
            cur_url = self.page.url
            target = locator.get_attribute('target')
            # If link opens in a new tab/window
            if target == '_blank':
                with self.page.context.expect_page() as new_page_info:
                    locator.click()
                new_page = new_page_info.value
                new_page.wait_for_load_state()
                new_page.close()
            else:
                locator.click()
                self.page.wait_for_load_state()
                # if navigation occurred in same page, go back to original
                try:
                    if self.page.url != cur_url:
                        self.page.go_back()
                except Exception:
                    pass

        self.eComm_dropdown.scroll_into_view_if_needed()
        self.eComm_dropdown.click()
        self.website_develop.wait_for(state='visible')
        _open_link(self.website_develop)

        self.android_dropdown.scroll_into_view_if_needed()
        self.android_dropdown.click()
        self.android_page.wait_for(state='visible')
        self.android_app.wait_for(state='visible')
        for j in [self.android_page, self.android_app]:
            _open_link(j)

        self.hybrid_app.scroll_into_view_if_needed()
        _open_link(self.hybrid_app)
