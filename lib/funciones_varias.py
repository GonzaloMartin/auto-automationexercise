import allure       # Para reportería Allure
import oracledb     # Para conectar con Oracle
import pyodbc       # Para conectar con SQL Server
import re           # Para expresiones regulares
import os           # Para validar archivos
import json         # Para manejo de archivos JSON
import time         # Para manejo del tiempo
import datetime     # Para manejo de fechas y horas

from allure_commons.types import AttachmentType                     # Para reportería Allure
from selenium import webdriver                                      # Para manejo de Selenium
from selenium.webdriver.chrome.service import Service               # Para manejo de Chrome
from selenium.webdriver.common.by import By                         # Para manejo de localizadores
from selenium.webdriver.common.keys import Keys                     # Para manejo de teclas
from selenium.webdriver.support.ui import WebDriverWait             # Para manejo de Wait Explícitos
from selenium.webdriver.support import expected_conditions as EC    # Para manejo de Wait Explícitos
from selenium.webdriver.support.ui import Select                    # Para manejo de Select con listas
from selenium.common.exceptions import TimeoutException             # Para manejo de try-catch


def get_datos():
    """
    Obtiene los datos necesarios para las pruebas.

    :return: Diccionario con los datos necesarios.
    """

    datos = {
        "ambiente": "homo",
        "usr": "automation@automationexercise.com",
        "pwd": "automation9090",
        "url": "https://automationexercise.com/",
        "url_api_productos": "https://automationexercise.com/api/productsList",
        "url_api_buscar": "https://automationexercise.com/api/searchProduct",
        "nombre_tarjeta": "Python Automation Bootcamp",
        "numero_tarjeta": "4111111111111111",
        "cvc": "311",
        "venc_mes": "12",
        "venc_anio": "2030"
    }
    return datos

def get_so():
    """
    Obtiene el sistema operativo en el que se está ejecutando el script.
    Si es linux, devuelve True. Si es Windows, devuelve False.

    :return: Booleano indicando si el sistema operativo es Linux (True) o Windows (False).
    """
    return os.name != "nt"

def validar_regex(cadena, especie, flexible=None):
    """
    Dada una cadena y una especie, devuelve True si cumple con la expresión regular de la especie.
    Si no cumple, devuelve False.

    :param cadena: Cadena a validar.
    :param especie: Especie de la expresión regular a validar.
    :param flexible: Si es distinto de None, utiliza match en lugar de fullmatch.
    :return: Booleano indicando si la cadena cumple con la expresión regular.
    """

    regex = {  # Diccionario de expresiones regulares  "Especie: Expresión regular"
        'fecha': r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)',
        'hora': r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$',
        'numerico': '^[0-9]*$',
        'saldo': r'^(\d|-)?(\d|.)*\,?\d*$',
        'email': r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$',
        'cross': '(.+?)',
        'tipoQuery': '(insert|update|delete)'
    }
    if flexible is not None:
        resultado = re.match(regex[especie], cadena)
    else:
        resultado = re.fullmatch(regex[especie], cadena)
    return bool(resultado)

def get_fecha_de_hoy(tipo, desfase_atras=None, desfase_adelante=None):
    """
    Obtiene la fecha actual en el formato especificado, con la opción de aplicar un desfase.

    :param tipo: Formato de la fecha ("DDMMAAAA" o "AAMMDD").
    :param desfase_atras: Número de días a restar de la fecha actual (opcional).
    :param desfase_adelante: Número de días a sumar a la fecha actual (opcional).
    :return: Fecha en el formato especificado.
    """

    # fecha_5_dias_atras = (datetime.now() - timedelta(days=5)).strftime("%d/%m/%Y") # type: ignore
    formatos = {
        "DDMMAAAA": "%d%m%Y",
        "AAMMDD": "%y%m%d"
    }

    if tipo not in formatos:
        raise ValueError(f"Formato de fecha no válido: {tipo}. Use uno de {list(formatos.keys())}.")

    today = datetime.date.today()

    if desfase_atras:
        today -= datetime.timedelta(days=desfase_atras)
    if desfase_adelante:
        today += datetime.timedelta(days=desfase_adelante)

    return today.strftime(formatos[tipo])

def get_connection_strings_db(ambiente):
    """
    Devuelve los connectionstrings de una DB específica.
    Esta funcion es llamada por la funcion consultarOracle

    :param ambiente: Ambiente de la base de datos.
    :return: Diccionario con los connectionstrings.
    """

    connection_strings = {
        "Homo": {
            'hostPagarH': "AQUI VA EL HOST",
            'portPagarH': "AQUI VA EL PUERTO",
            'nomBasePagarH': "AQUI VA EL NOMBRE DE LA BASE",
            'userBasePagarH': "AQUI VA EL USUARIO",
            'passPagarH': "AQUI VA LA CONTRASEÑA",
            'tnsNamesHOM': "AQUI VA EL TNSNAMES DE LA BASE HOMOLOGACION"
        },
        "QA": {
            'hostPagarQ': "AQUI VA EL HOST",
            'portPagarQ': "AQUI VA EL PUERTO",
            'nomBasePagarQ': "AQUI VA EL NOMBRE DE LA BASE",
            'userBasePagarQ': "AQUI VA EL USUARIO",
            'passPagarQ': "AQUI VA LA CONTRASEÑA",
            'tnsNamesQA': "AQUI VA EL TNSNAMES DE LA BASE QA"
        }
    }
    return connection_strings.get(ambiente, None)

def consultar_oracle(query):
    """
    Ejecuta una consulta SQL en una base de datos Oracle y devuelve el resultado junto con los nombres de las columnas.
    Si sólo se quiere ver el resultado, se debe usar resultado[0]
    Si sólo se quiere ver el nombre de las columnas, se debe usar resultado[1]

    :param query: Consulta SQL a ejecutar.
    :return: Una tupla que contiene:
             - row: La primera fila del resultado de la consulta (o None si no hay resultados).
             - colNames: Lista con los nombres de las columnas en minúsculas (o None si no hay resultados).
    :raises AssertionError: Si la consulta no devuelve ningún valor.
    :raises TimeoutException: Si ocurre un problema de conexión con la base de datos.
    """

    dato = None
    row = None
    try:
        if get_datos()["ambiente"].lower() == "Homo":
            dicBase = get_connection_strings_db("Homo")  # Para querys de Homo.
            conn = oracledb.connect(user=dicBase['userBasePagarH'], password=dicBase['passPagarH'],
                                    dsn=dicBase['tnsNamesHOM'])
        else:
            dicBase = get_connection_strings_db("QA")  # Para querys de QA.
            conn = oracledb.connect(user=dicBase['userBasePagarQ'], password=dicBase['passPagarQ'],
                                    dsn=dicBase['tnsNamesQA'])

        c = conn.cursor()  # defino un cursor
        c.execute(query)  # con dicho cursor ejecuto la query
        if c.fetchvars is not None:  # si la query tiene resultado
            for row in c:  # iterancia sobre los resultados.
                dato = row[0]  # tomo el primer valor que encuentro (tiene que haber al menos 1)
            colNames = [i[0] for i in c.description]  # obtengo los nombres de las columnas
            colNames = [x.lower() for x in colNames]  # convierto los nombres de las columnas a minúsculas
            assert dato is not None, "La consulta Oracle no devolvió ningún valor.\n" + query
        else:
            row = None
            colNames = None
        c.close()
        conn.close()
        return row, colNames
    except TimeoutException as exc:
        print(exc.msg)
        print("Error: [Oracle] Problemas de conexión con la query: \n" + query)
        return None

def consultar_sql(query):
    """
    Ejecuta una consulta SQL en una base de datos SQL Server y devuelve el resultado.
    Si la consulta no tiene resultados, verifica si es un INSERT para realizar un commit.
    En caso de que la consulta tenga resultados, devuelve la primera fila obtenida.
    Si sólo se quiere ver el resultado, se debe usar resultado[0]
    Si sólo se quiere ver el nombre de las columnas, se debe usar resultado.cursor_description

    :param query: Consulta SQL a ejecutar.
    :return: La primera fila del resultado de la consulta o None si no hay resultados.
    :raises AssertionError: Si la consulta no devuelve ningún valor cuando se esperan resultados.
    :raises TimeoutException: Si ocurre un problema de conexión con la base de datos.
    """

    dato = None
    row = None
    es_una_query_sin_resultados = validar_regex(query, "tipoQuery", "flex")
    try:
        if os.name == "nt":  # Windows
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=AQUI_VA_EL_SERVIDOR;DATABASE=AQUI_VA_LA_BASE')
        else:  # Linux
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AQUI_VA_EL_SERVIDOR;DATABASE=AQUI_VA_LA_BASE;'
                                  'UID=AQUI_VA_EL_UID;PWD=AQUI_VA_LA_CLAVE')

        c = conn.cursor()  # defino un cursor
        c.execute(query)  # usando el cursor, ejecuto la query que recibo por parámetro.
        if not es_una_query_sin_resultados:  # si la query tiene resultados
            for row in c:  # voy iterando entre las filas que me haya devuelto la query.
                dato = row[0]  # tomo el primer valor de la fila
            assert dato is not None, "La consulta SQL no devolvió ningún valor. " + query
        else:   # si la query no tiene resultados
            if str(query).find("insert") != -1: c.commit()  # si la query es un INSERT, hago commit
            row = None
        c.close()
        conn.close()  # cierro la conexión y el cursor
        return row
    except TimeoutException as exc:
        print(exc.msg)
        print("Error: [SQL] Problemas de conexión con la query: \n" + query)
        return None


class FuncionesGenericas:
    def __init__(self, driver):
        """
        Inicializa la clase con el driver de Selenium.

        :param driver: Driver de Selenium.
        """
        self.driver = driver

    def get_screen_shot(self, nombre):
        """
        Toma un screenshot de la pantalla y lo adjunta al reporte de Allure.

        :param nombre: Nombre del screenshot.
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

    def trackear_trafico(self, trafico_buscado):
        """
        Trackea el tráfico de la página y busca un tráfico específico.
        Luego lo imprime en consola.
        :param trafico_buscado: Tráfico a buscar.
        :return: Valor del tráfico buscado.
        """

        valor = None
        r = self.driver.execute_script("return window.performance.getEntries();")
        for res in r:
            if str(res['name']).find(trafico_buscado) != -1:
                print(res['name'], res['responseStatus'])
                valor = str(res['responseStatus'])
        return valor


    def localizar_elemento(self, elemento):
        """
        Localiza un elemento en la página web utilizando diferentes tipos de localizadores (XPath, CSS Selector, ID).
        Esta función es la implementación de EXPLICIT WAITS.
        Se debe llamar a esta función cada vez que se quiera localizar un elemento de espera variable.

        :param elemento: Localizador del elemento (XPath, CSS Selector o ID).
        :return: Objeto del elemento localizado o None si no se pudo localizar.
        """

        tipo = elemento[0:1]
        try:
            valor = WebDriverWait(self.driver, 20)
            if tipo == "/" or tipo == "(":
                valor.until(EC.element_to_be_clickable((By.XPATH, elemento)))
                valor = self.driver.find_element(By.XPATH, elemento)
            elif tipo == "d":
                valor.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
            else:
                valor.until(EC.element_to_be_clickable((By.ID, elemento)))
                valor = self.driver.find_element(By.ID, elemento)

            print("Elemento localizado: " + elemento)
            return valor
        except TimeoutException as exc:
            print(exc.msg)
            print("Error: No se pudo localizar el Elemento: " + elemento)
            return None

    def localizar_elemento_click(self, elemento):
        """
        Localiza un elemento de tipo click en la página web utilizando diferentes tipos de localizadores (XPath, CSS Selector, ID).
        Pensada para objetos tipo click.  Posible pronta deprecación.

        :param elemento: Localizador del elemento (XPath, CSS Selector o ID).
        :return: Objeto del elemento localizado o None si no se pudo localizar.
        """

        tipo = elemento[0:1]
        try:
            if tipo == "/" or tipo == "(":
                valor = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, elemento)))
                # valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.XPATH, elemento)
            elif tipo == "d":
                valor = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
            else:
                valor = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, elemento)))
                valor = self.driver.find_element(By.ID, elemento)
            return valor
        except TimeoutException as exc:
            print(exc.msg)
            print("Error: No se pudo localizar el Elemento Click: " + elemento)
            return None

    def find_obj(self, elemento, valor=None):
        """
        Busca un elemento en la página y realiza una acción (clic o escritura) según el valor proporcionado.
        Para hacerlo, reconoce el tipo de locator que se le pasa.

        :param elemento: Localizador del elemento (XPath, CSS Selector o ID).
        :param valor: Valor a escribir en el elemento. Si es None, se realiza un clic en el elemento.
        :return: Objeto del elemento localizado o None si no se pudo localizar.
        :raises TimeoutException: Si no se encuentra el elemento.
        :raises Exception: Si no se identifica el valor del elemento.
        """

        try:
            objeto = None
            if valor is not None:
                # Es elemento para escritura
                objeto = self.localizar_elemento(elemento)
                objeto.clear()
                objeto.send_keys(valor)  # Escribo en el campo en cuestión
                print("Input: " + valor)
            elif valor is None:
                objeto = self.localizar_elemento_click(elemento)
                objeto.click()
                print("Click: " + elemento)
            else:
                print("No se identificó el valor del elemento: " + elemento)
            return objeto
        except TimeoutException as exc:
            print(exc.msg)
            print("Error: No se encontró el elemento: " + elemento)
            return None

    def procesar_pop_up(self, xpath_identificador, xpath_realizar=None):
        """
        Procesa un popUp que se abre en la página.
        Si el popUp tiene un botón para cerrarlo, se debe pasar el xpath del botón.

        :param xpath_identificador: XPath del elemento que identifica el pop-up.
        :param xpath_realizar: XPath del botón para cerrar el pop-up (opcional).
        :return: None
        """

        try:
            pop_up = WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, xpath_identificador))
            )
            texto = pop_up.text
            pop_up = self.driver.execute_script("arguments[0].scrollIntoView();", pop_up)
            self.get_screen_shot("Pop-Up")
            if texto != "" and xpath_realizar is not None:
                self.find_obj(xpath_realizar)
            else:
                print("No se encontró el pop-up.")
        except TimeoutException as exc:
            print(exc.msg)

    def select_combo(self, elemento, valor):  # Selecciona un valor de un combo.
        """
        Selecciona un valor de un combo en la página web.

        :param elemento: XPath del combo.
        :param valor: Valor a seleccionar en el combo.
        :return: None
        """

        try:
            Select(self.driver.find_element(By.XPATH, elemento)).select_by_visible_text(valor)
            print("Combo: " + valor)
        except TimeoutException as exc:
            print(exc.msg)
            print("Error: No se pudo seleccionar el valor del combo: " + valor)
