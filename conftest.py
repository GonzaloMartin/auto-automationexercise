import warnings
import pytest
import chromedriver_binary
import urllib3
from selenium import webdriver
from src.pages.po_01_login_logout import PoLoginLogout
from lib.funciones_varias import *


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

def web_driver_setup():
    es_linux = get_so()
    options = webdriver.ChromeOptions()

    options.add_argument("--no-proxy-server")
    options.add_argument("--window-size=1920,1080")

    if es_linux:
        options.add_argument('--headless=new')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")

    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)
    warnings.simplefilter('ignore', ResourceWarning)
    urllib3.disable_warnings()
    # print(chromedriver_binary.chromedriver_filename)
    return driver

def ignorar_warnings():
    warnings.simplefilter('ignore', ResourceWarning)
    urllib3.disable_warnings()

@pytest.fixture(scope="function")
def fixture_login():
    global driver, me, login_logout
    driver = web_driver_setup()

    # Relevamiento de Información
    me = FuncionesGenericas(driver)
    datos = get_datos()

    # Ingreso
    login_logout = PoLoginLogout(driver)
    login_logout.entrada_sitio(url=datos['url'])
    login_logout.login(nombre_usuario=datos['usr'], clave=datos['pwd'])

    yield login_logout

    # Teardown
    login_logout.logout()
    etiqueta = login_logout.home.get_text()
    assert etiqueta == "Home", "No se cerró sesión correctamente."
    driver.close()
