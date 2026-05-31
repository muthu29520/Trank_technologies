
from conftest import page

class foot_page:

    def __init__(self, page):
        self.page = page

        self.web_developm=page.locator('//a[text()="Web Development"]')
        self.cms_website=page.locator(' //a[text()="CMS Website Development"]')
        self.cms_page=page.locator('//h1[text()="CMS Website Development Company "]')
        #self.ecommerece_development=page.locator('//a[text()="eCommerce Development"]')
       
        #self.custom_web=page.locator('//a[text()="Custom Web Portal Development"]')
        #self.ui_ux=page.locator('//a[text()="UI UX Design"]')
        self.mobile_app=page.locator('//a[text()="Mobile App Design"]')  
        self.mobile_page=page.locator('//h1[text()="Mobile App Design Company "]')
        self.responsive=page.locator('//a[text()="Responsive Web Design"]')
        self.responsive_page=page.locator('//h1[text()="Responsive Web Design Company "]')
        self.brand_identity=page.locator('//a[text()="Brand Identity Design"]') 
        self.brand_page=page.locator('//h1[text()="Brand Identity"]')

        self.app_develop=page.locator('(//a[text()="App Development"])[1]')
        self.app_develp_page=page.locator('//h1[text()="App Development Services "]')
        self.ios_app=page.locator('(//a[text()="iOS App Development"])[1]')
        self.ios_page=page.locator('//li[text()="iOS App Development"]')
        self.android_app=page.locator('(//a[text()="Android App Development"])[1]')
        self.android_page=page.locator('//li[text()="Android Development"]')
        self.hybrid_app=page.locator('(//a[text()="Hybrid Mobile App Development"])[1]') 
        self.hyprid_page=page.locator('//li[text()="Hybrid App Development"]')   
        self.cross_platform=page.locator('//a[text()="Cross-Platform App Development"]')
        self.cross_page=page.locator('//li[text()="Cross Platform Development"]')
        self.progressive_app=page.locator('//a[text()="Progressive Web App Development"]')
        self.progressive_page=page.locator('//li[text()="Progressive App Development"]')

        self.graphic_design=page.locator('//a[text()="Graphic Design"]')
        self.graphic_page=page.locator('//li[text()="Graphic Design"]')
        self.logo=page.locator('//a[text()="Logo Design"]')
        self.logo_page=page.locator('//h1[text()="Logo Design Company"]')
        self.banner=page.locator('//a[text()="Banner Design"]')
        self.banner_page=page.locator('//h1[text()="Banner Design Company"]')
        self.packing=page.locator('//a[text()="Packaging Design"]')
        self.packing_page=page.locator('//h1[text()="Package Designing Company"]')
        self.busniess_card=page.locator('//a[text()="Business cards Design"]')
        self.busniess_page=page.locator('//h1[text()="Business Card Design"]')


    def footers_clicking(self):
        self.li_footer=[self.web_developm,self.cms_website,self.mobile_app,self.responsive,self.brand_identity,self.app_develop,self.ios_app,self.android_app,self.hybrid_app,self.cross_platform,self.progressive_app,self.graphic_design,self.logo,self.banner,self.packing,self.busniess_card]
        for a in self.li_footer:
            a.click()

            if self.cms_page.is_visible():
                print("navigate to cms website page")
            elif self.mobile_page.is_visible():
                print("navigate to mobile app design page")
            elif self.responsive_page.is_visible():
                print("navigate to responsive web design page")
            elif self.brand_page.is_visible():
                print("navigate to brand identity page")
            elif self.app_develp_page.is_visible():
                print("navigate to app development page")   
            elif self.ios_page.is_visible():
                print("navigate to ios app development page")
            elif self.android_page.is_visible():
                print("navigate to android app development page")
            elif self.hyprid_page.is_visible():
                print("navigate to hybrid app development page")
            elif self.cross_page.is_visible():
                print("navigate to cross platform development page")
            elif self.progressive_page.is_visible():
                print("navigate to progressive web app development page")
            elif self.graphic_page.is_visible():
                print("navigate to graphic design page")
            elif self.logo_page.is_visible():
                print("navigate to logo design page")
            elif self.banner_page.is_visible():
                print("navigate to banner design page")
            elif self.packing_page.is_visible():
                print("navigate to packing design page")
            elif self.busniess_page.is_visible():
                print("navigate to business card design page")
            else:
                print("failed to navigate the correct page")
        
