# Facturación Automatizada de AFIP

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

Dentro de main.py se deberán ingresar las siguientes modificaciones para poder hacer uso del mismo. Esto se debe a que muchos campos requieren información sensible los cuales solo el usuario del script deberá conocer.

**IMPORTANTE**:
   - Solo modificar lo que se encuentra dentro de las comillas dobles: (" ").
   - **Solo compartir este script desde este repositorio o asegurarse de que no deja en ninguno de los siguientes campos algún dato personal al pasárselo a otra persona.**.

### 1. Línea  46
Esta es la dirección donde se guardan los archivos que se descargan del buscador de Chrome, muy comúnmente llamada "descargas o downloads", ejemplo:

list_of_files = glob.glob(r'C:\Users\USUARIO\Downloads/*.pdf')

### 2. Línea  67
   
Agregar el correo electrónico que se usará para enviar los correos de forma automática.

email_from = "emailautomatico@mail .com"

**IMPORTANTE**: Se recomienda usar un nuevo correo electrónico y no uno que ya se utilice de forma personal ni empresarial.

### 3. Línea  72

Una vez creado el correo electrónico se deberá generarle el token de aplicación, [para esto se recomienda seguir los pasos de este tutorial.](https://www.youtube.com/watch?v=g_j6ILT-X0k&t=124s)

pswd = "TOKEN_APLICACION"

**IMPORTANTE**: Se debe saber que si una persona ajena contara con este token podría usarlo para enviar cualquier tipo de spam, asegúrese de no compartirlo con nadie.

### 4. Línea  75

Este es el mensaje que aparecerá en el asunto del correo, puede agregar lo que usted requiera.

subject = "EMPRESA - Factura AFIP"

### 5. Línea  81 a 86

Este es el mensaje en el cuerpo del correo que se enviará, puede agregar más líneas si se desea siempre y cuando se encuentre dentro de: (f""" """).

### 6. Línea  98

Es el nombre del archivo que se adjuntará al correo electrónico, se recomienda no cambiar pero de hacerlo mantenga el .pdf al final.

filename = "EMPRESA - Factura AFIP.pdf"

### 7. Línea  169

En este campo se debe ingresar el usuario con el que inicia sesión en la página del AFIP. Generalmente es un CUIL.

**Importante**: Por favor, leer la sección  **Sobre la Seguridad**

### 8. Línea  177

En este campo se debe ingresar la contraseña con la que inicia sesión en la página del AFIP.

**Importante**: Por favor, leer la sección **Sobre la Seguridad**

### 9. Línea  198

Es un campo muy técnico ya que dependerá de cómo se registró el nombre de la sociedad o empresa en AFIP, por ejemplo:

   Si aparece con el nombre: EMPRESA S.R.L., deberá poner: "//input[@value='EMPRESA S.R.L.']"
   Si aparece con el nombre: HERMANOS Y ASOCIADOS S.A, deberá poner: "//input[@value='HERMANOS Y ASOCIADOS S.A']"

Es fácil de saber ya que aparece cuando uno intenta hacer la facturación manual, simplemente ingréselo tal cual figura ahí.

### 10. Línea  249

Ingrese la dirección fiscal donde se encuentre la empresa, recuerde solo modificar lo que se encuentra dentro de las comillas dobles (" ").

## Aclaraciones importantes

### Sobre la línea  147

Hay ocasiones en que Google Chrome realiza actualizaciones de su buscador y ChromeDriverManager queda desactualizado dándonos un error que cierra el programa, en caso de que esto ocurra una solución temporal puede ser reemplazar la línea 147 por la siguiente:

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)

Esto fuerza utilizar una versión vieja de Chrome, en este caso es: 114.0.5735.90.

### Por qué no hay capturadores de errores en el Código

La idea de este script es mostrar el flujo principal tratando de mantenerlo lo más sencillo posible para quien lo lea pueda comprenderlo lo más rápido posible, además es una versión de muestra y no de puesta en producción.

### Sobre la seguridad

Al ser un script de muestra se señala dónde deben ir los datos importantes, pero no están resguardados en el caso de que se dejen ahí al guardar el archivo, es por esto que además de los pasos incluidos en "Configuración" se ruega implementar alguno de los siguientes factores:

- **Usar variables de entorno**: Esto garantiza que las credenciales estén fuera del código fuente y sean menos susceptibles a exponerse accidentalmente.
- **Utiliza un archivo de configuración segura**: En lugar de variables de entorno, puedes almacenar las credenciales en un archivo de configuración que esté fuera del directorio raíz del proyecto y que no se incluya en el control de versiones. Luego, puedes leer las credenciales desde este archivo en tu script.
- **Restringe el acceso**: Limita quién puede acceder y modificar las credenciales. Esto es especialmente importante en entornos compartidos o colaborativos. Asegúrate de que solo las personas autorizadas tengan acceso a las credenciales y controla los permisos de acceso.
