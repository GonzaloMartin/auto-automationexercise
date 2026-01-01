import pytest, allure
from src.apis.auto_productos import *


@pytest.mark.productos
@allure.feature("Productos")
@allure.parent_suite("Todos los Productos")
@allure.story("Ver todos los productos disponibles")
@allure.description("Función que me permite ver todos los productos de la API.")
@allure.severity(allure.severity_level.CRITICAL)
def test_productos():
    with allure.step("Realizar Solicitud de Login"):
        response = srv_productos()
        allure.attach(json.dumps(response[1], indent=4), name="Respuesta del servicio", attachment_type=allure.attachment_type.JSON)

    with allure.step("Validar Respuesta del Servicio"):
        assert response[0] is not None, "No se recibió respuesta del servicio."
        assert response[0].status_code == 200, "El servicio no se ejecutó correctamente. Error: " + str(response[0].status_code)

    with allure.step("Validar si Existe al manos UN Producto"):
        item = response[1].get("products")
        if item is not None:
            assert len(item) > 0, "El accessToken está vacío."
        else:
            pytest.fail("No existe el campo 'accessToken' en la respuesta.")