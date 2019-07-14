"""
Press Ctrl+C to quit.

2017-02-02 13:45:25.233400
Sensor - F4:A5:74:89:16:57
Temperature: 10
Humidity:    28
Pressure:    689
"""
# RuuviTag Libraries
import os
from datetime import datetime
from ruuvitag_sensor.ruuvi import RuuviTagSensor

# Cloudant Libraries
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# Sleep
from time import sleep

# Cloudant Credentials
serviceUsername = "25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix"
servicePassword = "ea29328064d8eae35cb8b1adc153c9e284f4de9422ddba89a1014a60f5dabe67"
serviceURL = "https://25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix:ea29328064d8eae35cb8b1adc153c9e284f4de9422ddba89a1014a60f5dabe67@25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix.cloudantnosqldb.appdomain.cloud"

# RuuviTag Beacon mac
mac = 'F7:36:31:B2:5F:F9'

# RuuviTag Global variables
line_sen = ""
line_tem = ""
line_hum = ""
line_pre = ""

# Db Name
databaseName = "dbRuuviTag"

# RuuviTag Begings to Scan
print('Starting')
def print_data(received_data):
    Sleep(1)
    received_mac = received_data[0]
    data = received_data[1]

    # Save Data in variables
    line_sen = str.format('Sensor - {0}', received_mac)
    line_tem = str.format('Temperature: {0} C', data['temperature'])
    line_hum = str.format('Humidity:    {0}', data['humidity'])
    line_pre = str.format('Pressure:    {0}', data['pressure'])

    # Clear screen and print sensor data
    os.system('clear')
    print('Press Ctrl+C to quit.\n\r')
    print('Team Bravers \n\r\n\r')
    print(str(datetime.now()))
    print(line_sen)
    print(line_tem)
    print(line_hum)
    print(line_pre)
    print('\n\r\n\r.......')

    # 3.  Almacenar una pequena coleccion de datos como documentos dentro de la base de datos
    # Crear documentos utilizando los datos de ejemplo.
    # Examinar cada fila de la matriz para el documento en sampleData:
    # Recuperar los campos de cada fila.
    sensor = received_mac
    temperature = data['temperature']
    humidity = data['humidity']
    pressure = document['pressure']

    # Crear un documento JSON que represente todos
    # los datos de la fila.
    jsonDocument = {
    "sensorMac": sensor,
    "temp": temperature,
    "hum": humidity,
    "press": pressure
    }
    print(jsonDocument)
    # Crear un documento utilizando la API de la base de datos.
    newDocument = myDBeacon.create_document(jsonDocument)
    # Comprobar que el documento existe en la base de datos.
    if newDocument.exists():
        print ("Document '{0}' successfully created.").format(number)
        # Separar los resultados.
        print ("----\n")
        # 4.  Recuperar una lista completa de documentos.

        # Recuperación sencilla y mínima del primer
        # documento de la base de datos.
        result_collection = Result(myDBeacon.all_docs)
        print ("Retrieved minimal document:\n{0}\n").format(result_collection[0])

        # Recuperación sencilla y completa del primer
        # documento de la base de datos.
        result_collection = Result(myDBeacon.all_docs, include_docs=True)
        print ("Retrieved full document:\n{0}\n").format(result_collection[0])

        # Separar los resultados.
        print ("----\n")

        # Utilizar un punto final de API de IBM Cloudant para recuperar
        # todos los documentos de la base de datos,
        # incluido su contenido.

        # Definir el punto final y los parámetros
        end_point = '{0}/{1}'.format(serviceURL, databaseName + "/_all_docs")
        params = {'include_docs': 'true'}

        # Emitir la solicitud
        response = client.r_session.get(end_point, params=params)

        # Mostrar el contenido de la respuesta
        print ("{0}\n").format(response.json())

        # Separar los resultados.
        print ("----\n")

        # Todo finalizado.
        # Ha llegado el momento de limpiar.
        # 6.  Cerrar la conexión con la instancia de servicio.

        # Desconectar del servidor
        client.disconnect()

        # Finalizar la demo.
        print ("===\n")

        # Decir adiós.
        exit()


# Use IBM librarie to create an IBM Cloudant client.
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)

# Connect with server
client.connect()

# Create an DB instance.
dbRuuviTag = client.create_database(databaseName)

# Verify if db exists.
if dbRuuviTag.exists():
    print ("'{0}' successfully create.\n".format(databaseName))
    # Split Results.
    print ("----\n")
    RuuviTagSensor.get_datas(print_data, mac)
