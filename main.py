import customtkinter

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import glob
import os

import openpyxl

def buscarEmail():
    # Load the Excel file
    dni = entry1.get()
    entry4.delete(0, len(entry4.get()))
    libro = openpyxl.load_workbook('file.xlsx')

    # Select the worksheet
    hoja = libro.active

    # Loop through all the rows in the worksheet

    email = "No existe un email asociado a ese DNI"
    for row in hoja.iter_rows(values_only=True):
        if(dni == str(row[0]).strip()):
            email = row[2].strip()
            break
    entry4.insert(0, email)
    libro.close()

def detectarArchivo():
    time.sleep(5)
                        # aca va a la direccion de la carpeta donde se descargan todos los archivos del buscador, ejemplo r'C:\Users\USUARIO\Downloads/*.pdf'
    list_of_files = glob.glob(r'CARPETADESTINO/*.pdf')  # *.pdf' siginfica que incluira todos los archivos pdf de ese destino
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file

def limpiar():
    entry1.delete(0,len(entry1.get()))
    entry2.delete(0, len(entry2.get()))
    entry3.delete(0, len(entry3.get()))
    entry4.delete(0, len(entry4.get()))

def enviarEmail(email, path):
    print(email)
    smtp_port = 587  # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server
    email = email.strip()
    email = email.strip(" ")


    print(email, len(email))
    # Set up the email lists
    email_from = "emailautomatico@mail.com" # INGRESAR EL MAIL QUE SE USARA PARA ENVIAR LSOCORREOS DE FORMA AUTOMATICA. RECORDAR GENERAL EL TOKEN DE APLICACION
    # es una array para el posible caso de enviar a multiples direcciones, de todas formas el programa fue hecho exclusivamente para recibir 1 sola direccion
    email_list = [email]

    # Define the password (better to reference externally)
    pswd = "TOKEN_APLICACION" #INGRESAR EL TOKEN DE APLICACION, LEER README PARA SABER COMO.

    # INGRESAR EL ASUNTO
    subject = "EMPRESA - Factura AFIP"

    # el bucle no es necesario porque siempre va a recibir 1 direccion, el algoritmo queda armado para un posible envio a varios emails diferentes en el futuro
    for person in email_list:
        # CUERPO DEL EMAIL
        body = f"""
        Este es un eMail automático con su factura de AFIP.
        
        Si hay algún error o tiene dudas por favor contáctese con LA EMPRESA.
        
        Muchas Gracias
        EMPRESA
        """
    # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "EMPRESA - Factura AFIP.pdf" #nombre random
        # Open the file in python as a binary
        attachment = open(path, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', f'attachment; filename="{filename}"')
        attachment_package.add_header('Content-Type', 'application/pdf')
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

        # Close the port
        TIE_server.quit()

def generar():
    dni = entry1.get()
    monto = entry2.get()
    descripcion = entry3.get()
    email = entry4.get()

    # config

    options = webdriver.ChromeOptions()  # stealth opt
    options.add_experimental_option('detach', True)  # normal opt
    options.add_argument('start-maximized')  # stealth opt
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # stealth opt
    options.add_experimental_option("useAutomationExtension", False)  # stealth opt

    #a veces ocurre que chromedriver no llega a actualizarse con respecto a la ultima version del buscador chrome
    #para eso utilizar: driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='x.x.x.x').install()), options=options)
    #un ejemplo de podria ser version='114.0.5735.90' o mas actual
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # stealth opt
    
    # stealth
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            )
    # main

    print("Bot AFIP")

    driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    wait = WebDriverWait(driver, 10)

    p = driver.current_window_handle
    parent = driver.window_handles[0]

    # cuitInput
    cuit = wait.until(EC.presence_of_element_located((By.ID, "F1:username")))
    cuit.send_keys("CUIL_FACTURANTE") #es EL USUARIO con el que se ingresa a pagina de AFIP

    # Siguiente
    siguiente = wait.until(EC.presence_of_element_located((By.ID, "F1:btnSiguiente")))
    siguiente.click()

    # claveInput
    clave = wait.until(EC.presence_of_element_located((By.ID, "F1:password")))
    clave.send_keys("CLAVE_AFIP") #LA CONTRASEÑA la que se ingresa a pagina de AFIP

    # Ingresar
    ingresar = wait.until(EC.presence_of_element_located((By.ID, "F1:btnIngresar")))
    ingresar.click()

    # Comprobantes en linea
    comprabantesDiv = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Comprobantes en línea")))
    comprabantesDiv.click()

    time.sleep(2)
    # SALTO DE PESTAÑA

    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    wait = WebDriverWait(driver, 10)

    # Empresa
    # ESTE ES EL CAMPO QUE MAS SE DEBERA PRESTAR ATENCION YA QUE SE DEBERA CAMBIAR SEGUN EL NOMBRE CON EL QUE APAREZCA LA EMPRESA EN LA WEB
    # se debe modificar la linea de abajo en la parte: "//input[@value='EMPRESA S.R.L.']")))
    #IMPORTANTE SOLO MODIFICAR EL CONTENIDO DENTRO DE LAS COMILLAS SIMPLES (' ')
    empresa = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='EMPRESA S.R.L.']")))
    empresa.click()

    # Generar Comprobantes
    generarComp = wait.until(EC.presence_of_element_located((By.ID, "btn_gen_cmp")))
    generarComp.click()

    # punto de venta
    puntoVenta = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='puntoDeVenta']")))
    puntoVenta.click()
    opcionColegio = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='1']")))
    opcionColegio.click()

    # continuar
    continuar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continuar >']")))
    continuar.click()

    # concepto
    concepto = wait.until(EC.presence_of_element_located((By.ID, "idconcepto")))
    concepto.click()

    # servicio
    servicio = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='2']")))
    servicio.click()

    # continuar2
    continuar2 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continuar >']")))
    continuar2.click()

    # condicion
    condicion = wait.until(EC.presence_of_element_located((By.ID, "idivareceptor")))
    condicion.click()

    # consumidorFinal
    consumidorFinal = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='5']")))
    consumidorFinal.click()

    # docReceptor
    docReceptor = wait.until(EC.presence_of_element_located((By.ID, "idtipodocreceptor")))
    docReceptor.click()

    # opcionDni
    opcionDni = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='96']")))
    opcionDni.click()

    # inputDni
    inputDni = wait.until(EC.presence_of_element_located((By.ID, "nrodocreceptor")))
    inputDni.send_keys(dni)

    # domicilioComercial
    domicilioComercial = wait.until(EC.presence_of_element_located((By.ID, "domicilioreceptor")))
    domicilioComercial.send_keys("DIRECCION FISCAL") #INGRESAR LA DIRECCION DE FACTURACION, EJ: CALLE FALSA 123

    # condicionVenta
    condicionVenta = wait.until(EC.presence_of_element_located((By.ID, "formadepago4")))
    condicionVenta.click()

    # continuar3
    continuar3 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continuar >']")))
    continuar3.click()

    # servicioDescripcion
    servicioDescripcion = wait.until(EC.presence_of_element_located((By.ID, "detalle_descripcion1")))
    servicioDescripcion.send_keys(descripcion)

    # UMedida
    UMedida = wait.until(EC.presence_of_element_located((By.ID, "detalle_medida1")))
    UMedida.click()

    # opcionUnidades
    opcionUnidades = wait.until(EC.presence_of_element_located((By.XPATH, "(//option[@value='7'])[2]")))
    opcionUnidades.click()

    # PrecUnitario
    PrecUnitario = wait.until(EC.presence_of_element_located((By.ID, "detalle_precio1")))
    PrecUnitario.send_keys(monto)

    # continuar4
    continuar4 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continuar >']")))
    continuar4.click()

    # confirmar
    confirmar = wait.until(EC.presence_of_element_located((By.ID, "btngenerar")))
    confirmar.click()

    alert = Alert(driver)
    alert.accept()

    # imprimir
    time.sleep(7)
    imprimir = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Imprimir...']")))
    imprimir.click()

    path = detectarArchivo()
    if len(email) >= 10:
        enviarEmail(email, path)


#######################MAIN UI########################################################

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("390x300")
root.resizable(False, False)
root.title("Facturas AFIP")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill = "both", expand = True)

frame.grid_rowconfigure(2, weight=0)
frame.grid_columnconfigure((0, 1), weight=0)

label = customtkinter.CTkLabel(master=frame, text="Datos del solicitante", font=("Roboto", 24, "bold"))
label.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky="nsew")

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Ingrese DNI")
entry1.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")

buscar_button = customtkinter.CTkButton(master=frame, text="Buscar Email", command=buscarEmail)
buscar_button.grid(row=1, column=1, padx=2, pady=5, sticky="nsew")

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Ingrese el monto" )
entry2.grid(row=2, column=0, columnspan=2, padx=2, pady=5, sticky="nsew")

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="descripcion: Ej: 2S TM  " )
entry3.grid(row=3, column=0, columnspan=2, padx=2, pady=5, sticky="nsew")

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Ingrese el mail" )
entry4.grid(row=4, column=0, columnspan=2, padx=2, pady=5, sticky="nsew")

button = customtkinter.CTkButton(master=frame, text="Empezar", command=generar)
button.grid(row=5, column=0, columnspan=1, padx=2, pady=20, sticky="nsew")

button2 = customtkinter.CTkButton(master=frame, text="Limpiar", command=limpiar)
button2.grid(row=5, column=1, padx=2, pady=20, sticky="nsew")

root.mainloop()