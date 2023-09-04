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
1. Ejecuta el script principal:

   ```bash
   python main.py

2. Se abrirá una ventana de interfaz gráfica que te permite ingresar los detalles necesarios para generar la factura de AFIP.
3. Completa los campos requeridos, como el DNI del solicitante, el monto, la descripción y la dirección de correo electrónico.
4. Haz clic en el botón "Empezar" para generar la factura de AFIP automáticamente en el sitio web de AFIP.
5. Si se proporciona una dirección de correo electrónico válida, el script enviará automáticamente la factura como archivo adjunto por correo electrónico.

## Configuración

