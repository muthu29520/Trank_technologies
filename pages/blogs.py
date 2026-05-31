
from conftest import page

class blogs_page:

    def __init__(self, page):
        self.page = page

        self.blog=page.locator('(//a[text()="Blog"])[1]')
        self.app_develop=page.locator('(//a[text()="App Development"])[3]')
        self.artifical=page.locator('(//a[text()="Artificial Intelligence"])[3]')
        self.content=page.locator('//a[text()="Content Marketing"]')
        self.crm_devolepment=page.locator('(//a[text()="CRM Development"])[3]')
        self.digital=page.locator('(//a[text()="Digital Marketing"])[2]')
        self.ecomm_develop=page.locator('(//a[text()="ECommerce Development"])[5]')
        self.Email_market=page.locator('(//a[text()="Email Marketing"])[2]')
        self.graphic=page.locator('(//a[text()="Graphic Design"])[3]')
        self.it_software=page.locator('//a[text()="Software & IT Company"]')
        self.software_develop=page.locator('(//a[text()="Software Development"])[2]')
        self.ux_design=page.locator('(//a[text()="UI UX Design"])[6]')
        self.web_develop=page.locator('(//a[text()="Web Development"])[6]')

        self.app_develop_page=page.locator('//span[text()="App Development"]')
        self.artifical_page=page.locator('//span[text()="Artificial Intelligence1"]')
        self.content_page=page.locator('//span[text()="Content Marketing"]')
        self.crm_devolepment_page=page.locator('//span[text()="CRM Development"]')
        self.digital_page=page.locator('//span[text()="Digital Marketing"]')
        self.ecomm_develop_page=page.locator('//span[text()="ECommerce Development"]')
        self.Email_market_page=page.locator('//span[text()="Email Marketing"]')
        self.graphic_page=page.locator('//span[text()="Graphic Design"]')
        self.it_software_page=page.locator('//span[text()="Software & IT Company"]')
        self.software_develop_page=page.locator('//span[text()="Software Development"]')
        self.ux_design_page=page.locator('//span[text()="UI UX Design"]')
        self.web_develop_page=page.locator('//span[text()="Web Development"]')
    

    def blog_mouseHover(self):
        self.blog.click()
    def blog_clicking(self):
        self.blog_list=[self.app_develop,self.artifical,self.content,self.crm_devolepment,self.digital,self.ecomm_develop,self.Email_market,self.graphic,self.it_software,self.software_develop,self.ux_design,self.web_develop]
        for c in self.blog_list:
            self.blog_mouseHover()
            c.click()

            if self.app_develop_page.is_visible():
                print("navigate to app development page")     
            elif self.artifical_page.is_visible():
                print("navigate to artifical intelligence page")
            elif self.content_page.is_visible():
                print("navigate to content marketing page")
            elif self.crm_devolepment_page.is_visible():
                print("navigate to crm development page")
            elif self.digital_page.is_visible():    
                print("navigate to digital marketing page")
            elif self.ecomm_develop_page.is_visible():
                print("navigate to ecommerce development page")
            elif self.Email_market_page.is_visible():   
                print("navigate to email marketing page")
            elif self.graphic_page.is_visible():    
                print("navigate to graphic design page")
            elif self.it_software_page.is_visible():    
                print("navigate to software and it company page")
            elif self.software_develop_page.is_visible():
                print("navigate to software development page")
            elif self.ux_design_page.is_visible():
                print("navigate to ui ux design page")     
            elif self.web_develop_page.is_visible():
                print("navigate to web development page")   
            else:
                print("failed to navigate the correct page")            