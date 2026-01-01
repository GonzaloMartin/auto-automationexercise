import json
import requests
from lib.funciones_varias import *
from conftest import *

def srv_productos():
    """
    Automatización de la API Pública de Automation Exercise, endpoint All Products.

    :return: response, response_json
    """

    dato = get_datos()
    url = dato['url_api_productos'] if dato['ambiente'] != "dev" else None  # No hay endpoint dev para esta API pública

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    prebody = {
    }

    try:
        ignorar_warnings()
        body = json.dumps(prebody)
        response = requests.get(url, headers=headers, verify=False)
        response_json = response.json()

        print("Response:\n", json.dumps(response_json, indent=4))
        return response, response_json
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error: {e}")
        return None, None
    except ValueError:
        print("La respuesta no es un JSON válido.")
        return None, None
