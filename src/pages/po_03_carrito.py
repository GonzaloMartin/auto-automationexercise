from seleniumpagefactory.Pagefactory import PageFactory
from lib.funciones_varias import *

class PoCarrito(PageFactory):
    def __init__(self, driver):
        global me, info
        self.driver = driver
        self.name = self.__class__.__name__
        me = FuncionesGenericas(driver)

    locators = {
        "btn_carrito":         ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[3]/a"),
        "tabla_carrito":       ("XPATH", "//table[@id='cart_info_table']/thead/tr[@class='cart_menu']/td[@class='image']"),
        "item_carrito":        ("XPATH", "//tr[@id='product-11']/td[@class='cart_description']/h4/a"),
        "btn_checkout":        ("XPATH", "//section[@id='do_action']/div[@class='container']/div[@class='row']/div[@class='col-sm-6']/a[@class='btn btn-default check_out']"),
        "lbl_revisar_carrito": ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[@class='step-one'][2]/h2[@class='heading']"),
        "txt_comentario":      ("XPATH", "//div[@id='ordermsg']/textarea[@class='form-control']"),
        "btn_proceder":        ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[7]/a[@class='btn btn-default check_out']"),
    }

    def ingresar_carrito(self):
        self.btn_carrito.click()
        self.tabla_carrito.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def validar_item(self):
        self.item_carrito.element_to_be_clickable()
        item = self.item_carrito.get_text()
        me.get_screen_shot(self.name)
        return item

    def proceder_checkout(self, comentario):
        self.btn_checkout.click()
        self.lbl_revisar_carrito.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.txt_comentario.set_text(comentario)
        me.get_screen_shot(self.name)
        self.btn_proceder.click()
        me.get_screen_shot(self.name)
