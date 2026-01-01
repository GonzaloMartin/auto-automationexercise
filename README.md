# Automation Exercise con Framework de Automatización 

Aquí se encuentra el desarrollo de la automatización a modo de ejemplo de la web de "Automation Exercise" junto con su API expuesta.
Para su corrida, los scripts necesitan tener un set de datos de usuario acorde a la funcionalidad que se esté probando.
Tecnologías aplicadas:  Python + Selenium + API.

## Comenzando 🚀

_¿Qué es Python?_

En palabras fáciles, es un lenguaje de programación interpretado de alto nivel, por lo cual su aprendizaje es muy rápido dado que su sintaxis es sencilla, aprovechándose su legibilidad y portabilidad.  Tiene muy pocas dependencias y se apoya en bibliotecas de código que ya vienen integradas.
Para el testeo de las automatizaciones se usará _Pytest_, un framework que facilita la buena práctica de pruebas de cualquier desarrollo.

_¿Qué es Selenium?_

Es un framework de automatización que facilita la creación de scripts para pruebas funcionales basadas en aplicaciones web. Interactúa con el navegador en cuestión mediante métodos que proporciona el propio framework.

### Pre-Requisitos 📋

A bien de poder correr las automatizaciones correctamente:

1. Tener instalado [PyCharm.](https://www.jetbrains.com/pycharm/download/)
2. Tener instalado [Python.](https://www.python.org/downloads/)
3. Tener instalado [Allure Report.](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/) [Descargar el último zip. Ej: allure-commandline-2.xx.xx.zip]
4. Agregar la carpeta bin de Allure en la Variable de entorno PATH (Sistema): (Carpeta_Allure)\bin

## Instalación y manos a la obra 🖥️

* Clonar el proyecto completo:

`> git clone https://github.com/GonzaloMartin/auto-automationexercise.git`

* Abrir el proyecto con PyCharm:

`File -> Open... -> [Carpeta del Proyecto]`

* Hacer magia codeando ⭐

## Requisitos finales 🤖️

Desde la terminal o línea de comandos, ejecutar el siguiente comando para instalar las dependencias necesarias del proyecto:

`> pip install -r requirements.txt`


## Ejecutando las Pruebas ⚙️

[Alternativa 1] Desde local:

    pytest -v --alluredir="allure-results" --clean-alluredir
	
_Luego..._
	
	allure generate --single-file .\allure-results\
	
[Alternativa 2] Desde Pipeline:

* Pronto.


### Pruebas 🔩

_Lista de tests._

1. Estructura Básica.
WIP


## Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje de programación.
* [Pytest](https://docs.pytest.org/) - Framework de pruebas de Automatización.
* [Selenium](https://www.selenium.dev/documentation/webdriver/) - Framework de Automatización.
* [Allure](https://docs.qameta.io/allure/) - Herramienta de Reportería.

## Dudas o consultas 👥

* Gonzalo Montalvo | [@GonzaloMartin](https://github.com/GonzaloMartin)

-Fin del documento.
