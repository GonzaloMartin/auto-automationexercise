from seleniumpagefactory.Pagefactory import PageFactory
from lib.funciones_varias import *

class PoProductos(PageFactory):
    def __init__(self, driver):
        global me, info
        self.driver = driver
        self.name = self.__class__.__name__
        me = FuncionesGenericas(driver)


    locators = {
        "btn_home":            ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[1]/a"),
        "btn_productos":       ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[2]/a"),
        "txt_buscar":          ("ID", "search_product"),
        "btn_buscar":          ("XPATH", "//button[@id='submit_search']/i[@class='fa fa-search']"),
        "btn_kids":            ("XPATH", "//div[@id='accordian']/div[@class='panel panel-default'][3]/div[@class='panel-heading']/h4[@class='panel-title']/a[@class='collapsed']"),
        "btn_kids_sub_item":   ("XPATH", "//div[@id='Kids']/div[@class='panel-body']/ul/li[2]/a"),
        "lbl_kids_header":     ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/h2[@class='title text-center']"),
        "btn_ver_producto":    ("XPATH", "/html/body/section[2]/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[@class='col-sm-4']/div[@class='product-image-wrapper']/div[@class='choose']/ul[@class='nav nav-pills nav-justified']/li/a"),
        "lbl_producto_sel":    ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='product-details']/div[@class='col-sm-7']/div[@class='product-information']/h2"),
        "btn_agregar_carrito": ("XPATH", "/html/body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='product-details']/div[@class='col-sm-7']/div[@class='product-information']/span/button[@class='btn btn-default cart']"),
        "lbl_agregado_ok":     ("XPATH", "//div[@id='cartModal']/div[@class='modal-dialog modal-confirm']/div[@class='modal-content']/div[@class='modal-header']/h4[@class='modal-title w-100']"),
        "btn_continuar":       ("XPATH", "//div[@id='cartModal']/div[@class='modal-dialog modal-confirm']/div[@class='modal-content']/div[@class='modal-footer']/button[@class='btn btn-success close-modal btn-block']"),
    }
    
    def ingresar_productos(self):
        self.btn_productos.click()
        self.txt_buscar.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def filtrar_seleccion(self, filtro):
        self.txt_buscar.set_text(filtro)
        me.get_screen_shot(self.name)
        self.btn_buscar.click()
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
