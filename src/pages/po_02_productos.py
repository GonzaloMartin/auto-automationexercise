from seleniumpagefactory.Pagefactory import PageFactory
from lib.funciones_varias import *

class PoProductos(PageFactory):
    def __init__(self, driver):
        global me, info
        self.driver = driver
        self.name = self.__class__.__name__
        me = FuncionesGenericas(driver)


    locators = {
        # Productos
        "btn_home":            ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[1]/a"),
        "btn_productos":       ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[2]/a"),
        "btn_kids":            ("XPATH", "//div[@id='accordian']/div[@class='panel panel-default'][3]/div[@class='panel-heading']/h4[@class='panel-title']/a[@class='collapsed']"),
        "btn_kids_sub_item":   ("XPATH", "//div[@id='Kids']/div[@class='panel-body']/ul/li[2]/a"),
        "lbl_kids_header":     ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/h2[@class='title text-center']"),
        "btn_ver_producto":    ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[@class='col-sm-4'][1]/div[@class='product-image-wrapper']/div[@class='choose']/ul[@class='nav nav-pills nav-justified']/li/a"),
        "lbl_producto_sel":    ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='product-details']/div[@class='col-sm-7']/div[@class='product-information']/h2"),
        "btn_agregar_carrito": ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='product-details']/div[@class='col-sm-7']/div[@class='product-information']/span/button[@class='btn btn-default cart']v"),
        "lbl_agregado_ok":     ("XPATH", "//div[@id='cartModal']/div[@class='modal-dialog modal-confirm']/div[@class='modal-content']/div[@class='modal-header']/h4[@class='modal-title w-100']"),
        "btn_continuar":       ("XPATH", "//div[@id='cartModal']/div[@class='modal-dialog modal-confirm']/div[@class='modal-content']/div[@class='modal-footer']/button[@class='btn btn-success close-modal btn-block']"),

        # Carrito
        "btn_carrito":         ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[3]/a"),
        "tabla_carrito":       ("XPATH", "//table[@id='cart_info_table']/thead/tr[@class='cart_menu']/td[@class='image']"),
        "item_carrito":        ("XPATH", "//tr[@id='product-11']/td[@class='cart_description']/h4/a"),
        "btn_checkout":        ("XPATH", "//section[@id='do_action']/div[@class='container']/div[@class='row']/div[@class='col-sm-6']/a[@class='btn btn-default check_out']"),
        "lbl_revisar_carrito": ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[@class='step-one'][2]/h2[@class='heading']"),
        "txt_comentario":      ("XPATH", "//div[@id='ordermsg']/textarea[@class='form-control']"),
        "btn_proceder":        ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[7]/a[@class='btn btn-default check_out']"),

        # Pago
        "lbl_pago":            ("XPATH", "//section[@id='cart_items']/div[@class='container']/div[@class='step-one']/h2[@class='heading']"),
        "txt_nombre_tarjeta":  ("XPATH", "//label[normalize-space(text())='Name on Card']/following-sibling::input"),
        "txt_numero_tarjeta":  ("XPATH", "//label[normalize-space(text())='Card Number']/following-sibling::input"),
        "txt_cvc":             ("XPATH", "//label[normalize-space(text())='CVC']/following-sibling::input"),
        "txt_venc_mes":        ("XPATH", "//label[normalize-space(text())='Expiration']/following::input[1]"),
        "txt_venc_anio":       ("XPATH", "//label[normalize-space(text())='Expiration']/following::input[2]"),
        "btn_pagar":           ("ID", "submit"),
        "lbl_compra_ok":       ("XPATH", "//section[@id='form']/div[@class='container']/div[@class='row']/div[@class='col-sm-9 col-sm-offset-1']/h2[@class='title text-center']/b"),
    }
    
    def ingresar_productos(self):
        self.btn_productos.click()
        self.btn_kids.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def filtrar_seleccion(self):
        self.btn_kids.click()
        self.btn_kids_sub_item.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.btn_kids_sub_item.click()
        self.lbl_kids_header.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def elegir_producto(self):
        self.btn_ver_producto.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.btn_ver_producto.click()
        self.lbl_producto_sel.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def agregar_al_carrito(self):
        producto = self.lbl_producto_sel.get_text()
        self.btn_agregar_carrito.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.btn_agregar_carrito.click()
        self.lbl_agregado_ok.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.btn_continuar.click()
        me.get_screen_shot(self.name)
        return producto
