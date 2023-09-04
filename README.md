# Facturacion Automatizada de AFIP

Este proyecto consiste en un script Python que automatiza la generación y envío de facturas de AFIP (Administración Federal de Ingresos Públicos) utilizando el módulo Selenium para interactuar con el sitio web de AFIP.

## Requisitos

- Python 3.x
- Bibliotecas Python: selenium, openpyxl, smtplib, email, glob, os, customtkinter, selenium_stealth
- Navegador Chrome instalado

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/TU_USUARIO/automatizacion-facturas-afip.git

2. Instala las dependencias Python:

   ```
   pip install -r requirements.txt


## Uso

![Menu Principal](https://github.com/Nicko25/Facturacion-Automatizada/blob/master/menu.png)

1. Ejecuta el script principal:

   ```bash
   python main.py

2. Se abrirá una ventana de interfaz gráfica que te permite ingresar los detalles necesarios para generar la factura de AFIP.
3. Completa los campos requeridos, como el DNI del solicitante, el monto, la descripción y la dirección de correo electrónico.
4. Haz clic en el botón "Empezar" para generar la factura de AFIP automáticamente en el sitio web de AFIP.
5. Si se proporciona una dirección de correo electrónico válida, el script enviará automáticamente la factura como archivo adjunto por correo electrónico.

## Configuración

Dentro de main.py se deberan ingresar las siguientes modificaciones para poder hacer uso del mismo.

IMPORTANTE:
   Solo modificar lo que se encuentra dentro de las comillas "MODFICAR".

1. ### Linea 46
esta es la direccion donde se guardan los archivos que se descargan de buscador de chrome muy comunmente llamada "descargas o downloads", ejemplo:

list_of_files = glob.glob(r'C:\Users\USUARIO\Downloads/*.pdf')

2. ### Linea 67
   
Agregar el mail que se usara para enviar los correos de forma automatica.

email_from = "emailautomatico@mail.com"

IMPORTANTE:
   - Se recomienda usar un nuevo email y no uno que ya se utilice de forma personal ni empresarial.
   - Una vez creado el mail se debera generarle el token de aplicacion, [para esto se recmiendo ver este tutorial.]([https://www.markdownguide.org/](https://www.youtube.com/watch?v=g_j6ILT-X0k&t=124s)
