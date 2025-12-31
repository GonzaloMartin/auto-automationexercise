from conftest import *
from src.pages.po_01_login_logout import *
from lib.funciones_varias import *

@pytest.fixture()
def chkError(request):
    yield
    if request.node.rep_call.failed: me.get_screen_shot("Error")

@pytest.fixture(scope="function")
def test_entrada_login():
    global driver, me, info_login, login_logout
    driver = web_driver_setup()

    # Relevamiento de Información
    me = FuncionesGenericas(driver)
    datos = get_datos()

    # Ingreso
    login_logout = PoLoginLogout(driver)
    login_logout.entrada_sitio(url=datos['url'])
    login_logout.login(nombre_usuario=datos['usr'], clave=datos['pwd'])

def teardown_function():
    login_logout.logout()
    etiqueta = login_logout.home.get_text()
    assert etiqueta == "Home", "No se cerró sesión correctamente."
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("chkError", "test_entrada_login")
def test_login():
    login_logout.home.click()
    etiqueta = login_logout.btn_salir.get_text()
    assert "Logout" in etiqueta, "No se pudo ingresar a la web."


#        pytest .\01_login_logout_test.py --alluredir="allure-results" --clean-alluredir
#        allure generate --single-file .\allure-results\
