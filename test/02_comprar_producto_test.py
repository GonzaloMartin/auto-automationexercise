from src.pages.po_02_productos import *
from src.pages.po_03_carrito import *
from src.pages.po_04_pagar import *
from lib.funciones_varias import *
from conftest import *

@pytest.fixture()
def chkError(request):
    yield
    if request.node.rep_call.failed: me.get_screen_shot("Error")
    
@pytest.fixture(scope="function")
def test_productos(fixture_login):
    global me, producto, carrito, pago, datos

    datos = get_datos()
    producto = PoProductos(fixture_login.driver)
    carrito = PoCarrito(fixture_login.driver)
    pago = PoPagar(fixture_login.driver)
    producto.ingresar_productos()

@pytest.mark.comprar_producto_ok
@pytest.mark.usefixtures("chkError", "test_productos")
def test_comprar_producto_ok():
    nombre_producto = "Sleeves Printed Top - White"
    producto.filtrar_seleccion(filtro=nombre_producto)
    producto.elegir_producto()
    item = producto.agregar_al_carrito()
    assert item == nombre_producto, "El producto agregado al carrito no es el esperado."

    carrito.ingresar_carrito()
    item_carrito = carrito.validar_item()
    assert item_carrito == item, "El producto en el carrito no es el esperado."
    carrito.proceder_checkout(comentario="Compra de prueba automatizada OK.")

    landing_ok = pago.validar_ingreso_pago()
    assert landing_ok == "Payment", "No se ingresó a la sección de pago correctamente."
    nombre = datos['nombre_tarjeta']
    numero = datos['numero_tarjeta']
    pin = datos['cvc']
    mes = datos['venc_mes']
    anio = datos['venc_anio']

    # El pago de momento queda en pausa porque la página de prueba no expone bien XPATHS funcionales.

    # pago.ingresar_datos_pago(nombre_tarjeta=nombre, numero_tarjeta=numero, cvc=pin, venc_mes=mes, venc_anio=anio)
    # compra_ok = pago.validar_compra_ok()
    # assert compra_ok == "Order Placed!", "La compra no se confirmó correctamente."
