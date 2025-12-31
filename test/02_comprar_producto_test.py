from conftest import *
from src.pages.po_02_productos import *
from src.pages.po_03_carrito import *
from lib.funciones_varias import *

@pytest.fixture()
def chkError(request):
    yield
    if request.node.rep_call.failed: me.get_screen_shot("Error")
    
@pytest.fixture(scope="function")
def test_productos(fixture_login):
    global me, producto, carrito

    producto = PoProductos(fixture_login.driver)
    carrito = PoCarrito(producto.driver)
    producto.ingresar_productos()

@pytest.mark.comprar_producto_ok
@pytest.mark.usefixtures("chkError", "test_productos")
def test_comprar_producto_ok():
    producto.filtrar_seleccion()
    producto.elegir_producto()
    item = producto.agregar_carrito()
    assert item == "Sleeves Printed Top - White", "El producto agregado al carrito no es el esperado."

    carrito.ingresar_carrito()
    item_carrito = carrito.validar_item()
    assert item_carrito == item, "El producto en el carrito no es el esperado."
    carrito.proceder_checkout(comentario="Compra de prueba automatizada OK.")
