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

Dentro de main.py se deberan ingresar las siguientes modificaciones para poder hacer uso del mismo. Esto se debe a que muchos campos requieren informacion sensible los cuales solo el usuario del script debera conocer.

**IMPORTANTE**:
   - Solo modificar lo que se encuentra dentro de las comillas dobles: (" ").
   - **Solo compartir este script desde este repositorio o asegurese de que no deja en ninguno de los siguientes campos algun dato personal al pasarselo a otra persona**.

### 1. Linea 46
esta es la direccion donde se guardan los archivos que se descargan de buscador de chrome muy comunmente llamada "descargas o downloads", ejemplo:

list_of_files = glob.glob(r'C:\Users\USUARIO\Downloads/*.pdf')

### 2. Linea 67
   
Agregar el mail que se usara para enviar los correos de forma automatica.

email_from = "emailautomatico@mail .com"

**IMPORTANTE**: Se recomienda usar un nuevo email y no uno que ya se utilice de forma personal ni empresarial.

### 3. Linea 72

Una vez creado el mail se debera generarle el token de aplicacion, [para esto se recomienda seguir los pasos de este tutorial.](https://www.youtube.com/watch?v=g_j6ILT-X0k&t=124s)

pswd = "TOKEN_APLICACION"

**IMPORTANTE**: Se debe saber que si una persona ajena contara con este token podria usarlo para enviar cualquier tipo de spam, asegurese de no compartirlo con nadie.

### 4. Linea 75

Este es mensaje en que aparecera en el asunto del correo, puede agregar lo que usted requiera.

subject = "EMPRESA - Factura AFIP"

### 5. Linea 81 a 86

Este es el mensaje en el cuerpo del correo que se enviara, puede agregar mas lineas si se desea siempre y cuando se encuentre dentro de: (f"""  """").

### 6. Linea 98

Es el nombre del archivo que de adjuntará al email, se recomienda no cambiar pero de hacerlo mantega el .pdf alfinal.

filename = "EMPRESA - Factura AFIP.pdf"

### 7. Linea 169

En este campo se debe ingresar el usuario con el que inicia sesion en la pagina del AFIP. Generalmente es un cuil.

**Importante**: Por favor, leer la seccion **Sobre la Seguridad**

### 8. Linea 177

En este campo se debe ingresar la contraseña con la que inicia sesion en la pagina del AFIP.

**Importante**: Por favor, leer la seccion **Sobre la Seguridad**

### 9. Linea 198

Es un campo muy tecnico ya que dependera de como se registro en el nombre de la sociedad o empresa en afip, por ejemplo:

   Si aparece con el nombre: EMPRESA S.R.L., debera poner: "//input[@value='EMPRESA S.R.L.']"
   Si aparece con el nombre: HERMANOS Y ASOCIADOS S.A, debera poner: "//input[@value='HERMANOS Y ASOCIADOS S.A']"

Es facil de saber ya que aparece cuando uno intenta hacer la facturacion manual, simplemente ingrese tal cual figura ahi.

### 10. Linea 249

Ingrese la direccion fiscal donde se encuentre la empresa, recuerde solo modificar lo que se encuntra dentro de las comillas dobles (" ").

## Aclaraciones importantes

### Sobre la linea 147
Hay ocaciones en que Google Chrome realiza actualizaciones de su buscador y ChromeDriverManager queda desactualizado dandonos un error que cierra el progreama,
en caso de que esto ocurra una solucion temporal puede ser reemplaazar la linea 147 por la siguiente:

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)

Esto fuerza utilizar una version vieja de Chrome, en este caso es: 114.0.5735.90.

### Porque no hay capturadores de errores en el Codigo

La idea de este script es mostrar el flujo principal tratando de mantenerlo lo mas sencillo posible para quien lo lea pueda comprenderlo lo mas rapido posible, ademas es una version de muestra y no de puesta en produccion.

### Sobre la seguridad

Al ser un script de muestra se señala donde deben ir los datos importantes, pero no estan resguardados en el caso de que se dejen ahi al guardar el archivo, es por esto que ademas de los pasos incluidos en "Configuracion" se reuga implementar alguno de los siguientes factores:

- **Usar variables de entorno**: Esto garantiza que las credenciales estén fuera del código fuente y sean menos susceptibles a exponerse accidentalmente.
- **Utiliza un archivo de configuración segura**: En lugar de variables de entorno, puedes almacenar las credenciales en un archivo de configuración que esté fuera del directorio raíz del proyecto y que no se incluya en el control de versiones. Luego, puedes leer las credenciales desde este archivo en tu script.
- **Restringe el acceso**: Limita quién puede acceder y modificar las credenciales. Esto es especialmente importante en entornos compartidos o colaborativos. Asegúrate de que solo las personas autorizadas tengan acceso a las credenciales y controla los permisos de acceso.
