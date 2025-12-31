from seleniumpagefactory.Pagefactory import PageFactory
from lib.funciones_varias import *

class PoPagar(PageFactory):
    def __init__(self, driver):
        global me
        self.driver = driver
        self.name = self.__class__.__name__
        me = FuncionesGenericas(driver)

    locators = {
        "lbl_pago": ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[@class='step-one']/h2[@class='heading']"),
        "txt_nombre_tarjeta": ("XPATH", "//label[normalize-space(text())='Name on Card']/following-sibling::input"),
        "txt_numero_tarjeta": ("XPATH", "//label[normalize-space(text())='Card Number']/following-sibling::input"),
        "txt_cvc": ("XPATH", "//label[normalize-space(text())='CVC']/following-sibling::input"),
        "txt_venc_mes": ("XPATH", "//label[normalize-space(text())='Expiration']/following::input[1]"),
        "txt_venc_anio": ("XPATH", "//label[normalize-space(text())='Expiration']/following::input[2]"),
        "btn_pagar": ("ID", "submit"),
        "lbl_compra_ok": ("XPATH", "//section[@id='form']/div[@class='container']/div[@class='row']/div[@class='col-sm-9 col-sm-offset-1']/h2[@class='title text-center']/b"),
    }

    def validar_ingreso_pago(self):
        self.lbl_pago.element_to_be_clickable()
        me.get_screen_shot(self.name)
        etiqueta = self.lbl_pago.get_text()
        return etiqueta

    def ingresar_datos_pago(self, nombre_tarjeta, numero_tarjeta, cvc, venc_mes, venc_anio):
        self.txt_nombre_tarjeta.wait_until_visible()
        self.txt_nombre_tarjeta.send_keys(nombre_tarjeta)
        self.txt_numero_tarjeta.send_keys(numero_tarjeta)
        self.txt_cvc.send_keys(cvc)
        self.txt_venc_mes.send_keys(venc_mes)
        self.txt_venc_anio.send_keys(venc_anio)
        me.get_screen_shot(self.name)
        self.btn_pagar.click()

    def validar_compra_ok(self):
        self.lbl_compra_ok.element_to_be_clickable()
        me.get_screen_shot(self.name)
        compra_ok = self.lbl_compra_ok.get_text()
        return compra_ok
