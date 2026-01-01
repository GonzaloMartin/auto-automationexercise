import json
import requests
from lib.funciones_varias import *
from conftest import *

def srv_buscar_productos(item):
    """
    Automatización de la API Pública de Automation Exercise, para buscar productos.

    :return: response, response_json
    """

    dato = get_datos()
    url = dato['url_api_buscar'] if dato['ambiente'] != "dev" else None  # No hay endpoint dev para esta API pública

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    body = {
        'search_product': item,
    }

    try:
        ignorar_warnings()
        # body = json.dumps(prebody)
        response = requests.post(url, headers=headers, data=body, verify=False)
        response_json = response.json()

        print("Response:\n", json.dumps(response_json, indent=4))
        return response, response_json
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error: {e}")
        return None, None
    except ValueError:
        print("La respuesta no es un JSON válido.")
        return None, None
