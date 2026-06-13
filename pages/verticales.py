
from conftest import page


class vertical_page:

    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.trading = page.locator('(//strong[text()="Trading"])')
        self.stock_trading= page.locator('(//a[text()="Stock Trading"])[1]')
        self.paper_trading= page.locator('//a[text()="Paper Trading"]')
        self.cfd= page.locator('(//a[text()="CFD Trading"])[1]')
        self.trading_app= page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo= page.locator('(//a[text()="Algo Trading"])[1]')
        self.custom_trading= page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.web_portal= page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.stock_page=page.locator('//li[text()="Stock Trading"]')
        self.paper_page=page.locator('//a[text()="Paper Trading"]')
        self.cfd_page=page.locator('//li[text()="CFD Trading"]')
        self.trading_page=page.locator('//li[text()="Trading in Massachusetts"]')
        self.algo_page=page.locator('//li[text()="Algo Trading"]')
        self.custom_page=page.locator('//li[text()="Custom Trading"]')
        self.web_page=page.locator('//li[text()="Trading Web Portal"]')

        #retail
        self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        #self.ecomm_web=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecomm_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.ecomm_webapp_page=page.locator('//h1[contains(text(),"eCommerce App Development")]')

        # #Healthcare
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.diet_nutritions=page.locator('(//a[contains(text(),"Diet &")])[1]')  
        self.diet_page=page.locator('//h1[text()="Top Dieting & Nutrition App Development Company"]')
        self.health_track=page.locator('(//a[text()="Health tracking App"])[1]')
        self.health_page=page.locator('//h1[text()="Leading Health Tracking App Development Company"]')

        #Fintech
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.pos_soft_develop=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[text()="Crypto"])[1]')

        self.pos_soft_page=page.locator('//li[text()="POS Software Development"]')
        self.crypto_page=page.locator('//li[text()="Crypto"]')
        
        #custom
        self.custom=page.locator('//strong[text()="Custom App"]')
        self.desktop_app=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.deskapp_page=page.locator('//h1[@class="cm-section-h"]')
        self.hrm_develop=page.locator('(//a[text()="HRM Development"])[1]')
        self.hrm_develop_page=page.locator('//h1[@class="cm-section-h"]')
        self.travel=page.locator('(//a[text()="Travel"])[1]')
        self.travel_page=page.locator('//h1[@class="aos-init aos-animate"]')
        self.Date_app=page.locator('(//a[text()="Dating App Development"])[1]')
        self.Date_page=page.locator('Dating App Development Company')
        self.crm_develop=page.locator('(//a[text()="CRM Development USA"])[1]')
        self.crm_page=page.locator('//h2[@class="mb-15"]')
        self.crm_development=page.locator('(//a[text()="CRM Development"])[1]')
        self.crm_develop_page=page.locator('//h1[@class="aos-init aos-animate"]')
        self.erp_app=page.locator('(//a[text()="ERP App Development"])[1]')
        self.erp_page=page.locator('//h1[@class="aos-init aos-animate"]')
        self.e_learn=page.locator('(//a[text()="E-Learning"])[1]')
        self.e_learn_page=page.locator('//li[text()="E-Learning"]')
        self.real_estate=page.locator('(//a[text()="Real Estate"])[1]')
        self.real_estate_page=page.locator('//li[text()="Real Estate"]')

    def vertical_mouseHover(self):
        self.vertical.hover()
    def tranding_mouseHover(self):
        self.trading.hover()
    
    def trading_clicking(self):
        self.li_vertical=[self.stock_trading,self.paper_trading,self.cfd,self.trading_app,self.algo,self.custom_trading,self.web_portal]
        for x in self.li_vertical:
            self.vertical_mouseHover()
            self.tranding_mouseHover()
            x.click()
    
            if self.stock_page.is_visible():
                print("navigate to stock trading page")
            elif self.paper_page.is_visible():
                print("navigate to paper trading page") 
            elif self.cfd_page.is_visible():
                print("navigate to cfd trading page")   
            elif self.trading_page.is_visible():
                print("navigate to trading_app page")
            elif self.algo_page.is_visible():
                print("navigate to algo page")
            elif self.custom_page.is_visible():
                print("navigate to custom page")
            elif self.web_page.is_visible():
                print("navigate to web portal page")
            else:
                print("failed to navigate the correct page")

    def retail_mouseHover(self):
         self.retail.hover()
    
    def retail_ecomm_clicking(self):
        self.li_retail=[self.ecomm_app]
        for y in self.li_retail:
            self.vertical_mouseHover()
            self.retail_mouseHover()
            y.click()

            if self.ecomm_webapp_page.is_visible():
                print("navigated to ecommerce web page")
            else:
                print("failed to navigate the correct page")
    
    def healthcare_mouseHover(self):
        self.healthcare.hover()
    def healthcare_clicking(self):
        self.li_health=[self.diet_nutritions,self.health_track]
        for i in self.li_health:
            self.vertical_mouseHover()
            self.healthcare_mouseHover()
            i.click()   

            if self.diet_page.is_visible():
                print("navigated to diet and nutrition page")   
            elif self.health_page.is_visible():
                print("navigated to health tracking page")
            else:
                print("failed to navigate the correct page")

    def fintech_mouseHover(self):
        self.fintech.hover()
    def fintech_clicking(self):
        self.fintech_li=[self.pos_soft_develop,self.crypto]    
        for j in self.fintech_li:
            self.vertical_mouseHover()
            self.fintech_mouseHover()
            j.click()

            if self.pos_soft_page.is_visible():
                print("navigated to pos software development page")
            elif self.crypto_page.is_visible():
                print("navigated to crypto page")
            else:
                print("failed to navigate the correct page")    
    

    def custom_mouseHover(self):
        self.custom.hover()
    def custom_clicking(self):
        self.custom_li=[self.desktop_app,self.hrm_develop,self.travel,self.Date_app,self.crm_develop,self.crm_development,self.erp_app,self.e_learn,self.real_estate]
        for k in self.custom_li:
            self.vertical_mouseHover()
            self.custom_mouseHover()
            k.click()

            if self.deskapp_page.is_visible():
                print("navigated to desktop app page")  
            elif self.hrm_develop_page.is_visible():
                print("navigated to hrm development page")
            elif self.travel_page.is_visible(): 
                print("navigated to travel page")
            elif self.Date_page.is_visible():
                print("navigated to dating app development page")
            elif self.crm_page.is_visible():
                print("navigated to crm development page")
            elif self.crm_develop_page.is_visible():    
                print("navigated to crm development page")
            elif self.erp_page.is_visible():    
                print("navigated to erp app development page")
            elif self.e_learn_page.is_visible():    
                print("navigated to e-learning page")
            elif self.real_estate_page.is_visible():    
                print("navigated to real estate page")
            else:
                print("failed to navigate the correct page")