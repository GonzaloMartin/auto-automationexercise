from seleniumpagefactory.Pagefactory import PageFactory
from lib.funciones_varias import *

class PoLoginLogout(PageFactory):
    def __init__(self, driver):
        global me
        self.driver = driver
        self.name = self.__class__.__name__
        me = FuncionesGenericas(driver)

    locators = {
        "home":        ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[1]/a"),
        "logo":        ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-4']/div[@class='logo pull-left']/a/img/@src"),
        "btn_login":   ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[4]/a"),
        "usuario":     ("XPATH", "//section[@id='form']/div[@class='container']/div[@class='row']/div[@class='col-sm-4 col-sm-offset-1']/div[@class='login-form']/form/input[2]"),
        "password":    ("XPATH", "//section[@id='form']/div[@class='container']/div[@class='row']/div[@class='col-sm-4 col-sm-offset-1']/div[@class='login-form']/form/input[3]"),
        "boton_login": ("XPATH", "//section[@id='form']/div[@class='container']/div[@class='row']/div[@class='col-sm-4 col-sm-offset-1']/div[@class='login-form']/form/button[@class='btn btn-default']"),
        "titulo_home": ("XPATH", "//div[@id='slider-carousel']/div[@class='carousel-inner']/div[@class='item active']/div[@class='col-sm-6'][1]/h1/span"),
        "btn_salir":   ("XPATH", "//header[@id='header']/div[@class='header-middle']/div[@class='container']/div[@class='row']/div[@class='col-sm-8']/div[@class='shop-menu pull-right']/ul[@class='nav navbar-nav']/li[4]/a"),
    }

    def entrada_sitio(self, url):
        driver = self.driver
        driver.get(url)
        self.home.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def login(self, nombre_usuario, clave):
        self.btn_login.element_to_be_clickable()
        self.btn_login.click()
        self.usuario.set_text(nombre_usuario)
        self.password.element_to_be_clickable()
        self.password.set_text(clave)

        me.get_screen_shot(self.name)
        self.boton_login.click()

        self.btn_salir.element_to_be_clickable()
        me.get_screen_shot(self.name)

    def logout(self):
        self.home.click()
        self.btn_salir.element_to_be_clickable()
        me.get_screen_shot(self.name)
        self.btn_salir.click()
        self.home.element_to_be_clickable()
        me.get_screen_shot(self.name)
