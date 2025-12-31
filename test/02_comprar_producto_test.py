from conftest import *
from src.pages.po_02_productos import *
from lib.funciones_varias import *

@pytest.fixture()
def chkError(request):
    yield
    if request.node.rep_call.failed: me.get_screen_shot("Error")
    
@pytest.fixture(scope="function")
def test_productos(fixture_login):
    global me, producto

    producto = PoProductos(fixture_login.driver)
    producto.ingresar_productos()

@pytest.mark.comprar_producto_ok
@pytest.mark.usefixtures("chkError", "test_productos")
def test_comprar_producto_ok():
    producto.filtrar_seleccion()
    producto.elegir_producto()
    item = producto.agregar_carrito()

    assert item == "Sleeves Printed Top - White", "El producto agregado al carrito no es el esperado."


#        pytest .\01_login_logout_test.py --alluredir="allure-results" --clean-alluredir
#        allure generate --single-file .\allure-results\