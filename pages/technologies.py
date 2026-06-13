
from conftest import page

class techno_page:

    def __init__(self, page):
        self.page = page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.eComm_develop=page.locator('//strong[text()="eCommerce Development"]')
        self.mengento=page.locator('//a[text()="Magento Development"]')
        self.opencart=page.locator('(//a[text()="Opencart Development"])[1]')
        self.codeigniter=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.wordpress=page.locator('(//a[text()="WordPress Development"])[1]')
        self.Big_commerce=page.locator('(//a[text()="Big Commerce"])[1]')
        self.shopify=page.locator('(//a[text()="Shopify Development"])[1]')
        self.cs_cart=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.Node_js=page.locator('(//a[text()="Node JS Development"])[1]')
        self.nop_commerece=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woo_commerce=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.laverl=page.locator('(//a[text()="Laravel Development"])[1]')
        self.presteashop=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.drupal=page.locator('(//a[text()="Drupal Development"])[1]')
        self.wix_develop=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.joomla=page.locator('(//a[text()="Joomla Development"])[1]')
        self.react_js=page.locator('(//a[text()="React JS Development"])[1]')
        self.express_js=page.locator('(//a[text()="Express JS Development"])[1]')

        self.mengento_page=page.locator('//h1[text()="Magento Development Company"]')
        self.opencart_page=page.locator('//h2[text()="OpenCart Website Development Services"]')
        self.codeigniter_page=page.locator('//h2[text()="All-Encompassing CodeIgniter Development Services for Industries"]')
        self.wordpress_page=page.locator('//li[text()="Wordpress Development"]')
        self.Big_commerce_page=page.locator('//li[text()="Big Commerce Development"]')
        self.shopify_page=page.locator('//h4[text()="Cost-Efficient Integration"]')
        self.cs_cart_page=page.locator('//li[text()="CS-Cart Development"]')
        self.Node_js_page=page.locator('//li[text()="Node JS Development"]')
        self.nop_commerece_page=page.locator('//li[text()="Nop Commerce Development"]')
        self.woo_commerce_page=page.locator('//h2[text()="Custom WooCommerce Development Services"]')
        self.laverl_page=page.locator('//li[text()="Laravel Development"]')
        self.presteashop_page=page.locator('//li[text()="Prestashop Development"]')
        self.drupal_page=page.locator('//li[text()="Drupal Development"]')
        self.wix_develop_page=page.locator('//li[text()="Wix Development"]')
        self.joomla_page=page.locator('//li[text()="Joomla Development"]')
        self.react_js_page=page.locator('//li[text()="React JS Development"]')
        self.express_js_page=page.locator('//li[text()="Express JS Development"]')
        
        #Mobile_App
        self.mobile_app=page.locator('//strong[text()="Mobile App Development"]')
        self.react_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_app=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarian=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appointment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.react_page=page.locator('//h2[text()="React Native Mobile App Development Services"]')
        self.enterprise_app_page=page.locator('//li[text()="Enterprise Development"]')
        self.xamarian_page=page.locator('//li[text()="Xarmin Development"]')
        self.kotlin_pge=page.locator('//li[text()="Kotlin Development"]')
        self.flutter_page=page.locator('//li[text()="Flutter Development"]')
        self.ionic_page=page.locator('//li[text()="Iconic Development"]')
        self.swift_mobile_page=page.locator('//li[text()="Swift Development"]')
        self.appointment_page=page.locator('//li[text()="Appointment Development"]')
        
        self.ai = page.locator('//strong[text()="Artificial Intelligence"]')
        self.ai_page=page.locator('//span[text()="AI Development Company"]')

    def technology_mouseHover(self):
        self.technology.hover()
    def eComm_mouseHover(self):
        self.eComm_develop.hover()
    def eComm_cllicking(self):
        self.eComm_li=[self.mengento,self.opencart,self.codeigniter,self.wordpress,self.Big_commerce,self.shopify,self.cs_cart,self.Node_js,self.nop_commerece,self.woo_commerce,self.laverl,self.presteashop,self.drupal,self.wix_develop,self.joomla,self.react_js,self.express_js ]
        for a in self.eComm_li:
            self.technology_mouseHover()
            self.eComm_mouseHover()
            a.click()

            if self.mengento_page.is_visible():
                print("navigate to mengento page")
            elif self.opencart_page.is_visible():
                print("navigate to opencart page")
            elif self.codeigniter_page.is_visible():
                print("navigate to codeigniter page")   
            elif self.wordpress_page.is_visible():
                print("navigate to wordpress page")
            elif self.Big_commerce_page.is_visible():
                print("navigate to big commerce page")
            elif self.shopify_page.is_visible():
                print("navigate to shopify page")
            elif self.cs_cart_page.is_visible():
                print("navigate to cs_cart page")
            elif self.Node_js_page.is_visible():
                print("navigate to node js page")
            elif self.nop_commerece_page.is_visible():
                print("navigate to nop commerce page")
            elif self.woo_commerce_page.is_visible():
                print("navigate to woo commerce page")
            elif self.laverl_page.is_visible():
                print("navigate to laverl page")
            elif self.presteashop_page.is_visible():
                print("navigate to presteashop page")
            elif self.drupal_page.is_visible():
                print("navigate to drupal page")
            elif self.wix_develop_page.is_visible():    
                print("navigate to wix develop page")
            elif self.joomla_page.is_visible():
                print("navigate to joomla page")
            elif self.react_js_page.is_visible():
                print("navigate to react js page")  
            elif self.express_js_page.is_visible():
                print("navigate to express js page")
            else:
                print("failed to navigate the correct page")


    def mobile_app_mouses_hover(self):
        self.mobile_app.hover()
    def mobile_app_clicking(self):
        self.mobile_app_li=[self.react_native,self.enterprise_app,self.xamarian,self.kotlin,self.flutter,self.ionic,self.swift_mobile,self.appointment]
        for b in self.mobile_app_li:
            self.technology_mouseHover()
            self.mobile_app_mouses_hover()
            b.click()

            if self.react_page.is_visible():
                print("navigate to react native page") 
            elif self.enterprise_app_page.is_visible():
                print("navigate to enterprise app page")
            elif self.xamarian_page.is_visible():
                print("navigate to xamarian page")
            elif self.kotlin_pge.is_visible():
                print("navigate to kotlin page")
            elif self.flutter_page.is_visible():
                print("navigate to flutter page")
            elif self.ionic_page.is_visible():  
                print("navigate to ionic page")
            elif self.swift_mobile_page.is_visible():
                print("navigate to swift mobile page")
            elif self.appointment_page.is_visible():
                print("navigate to appointment page")
            else:
                print("failed to navigate the correct page")

    def ai_click(self):
        self.technology_mouseHover()
        self.ai.hover()
        self.ai.click()
        if self.ai_page.is_visible():
            print("navigate to ai page")
        else:
            print("failed to navigate the correct page")
      



