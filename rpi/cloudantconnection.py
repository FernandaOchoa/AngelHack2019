# 1.  Conectar con la instancia de servicio.

# Habilitar las bibliotecas de Python necesarias.

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# Variables útiles
serviceUsername = "25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix"
servicePassword = "ea29328064d8eae35cb8b1adc153c9e284f4de9422ddba89a1014a60f5dabe67"
serviceURL = "https://25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix:ea29328064d8eae35cb8b1adc153c9e284f4de9422ddba89a1014a60f5dabe67@25656ee7-7379-47cd-9ba0-7180a1a2495e-bluemix.cloudantnosqldb.appdomain.cloud"

# Este es el nombre de la base de datos con la que trabajamos.
databaseName = "databasedemo"

# Esta es una sencilla colección de datos
# que guardaremos en la base de datos.
sampleData = [
[1, "one", "boiling", 100],
[2, "two", "hot", 40],
[3, "three", "warm", 20],
[4, "four", "cold", 10],
[5, "five", "freezing", 0]
]

# Iniciar la demo.
print ("===\n")

# Utilizar la biblioteca de IBM Cloudant para crear un cliente de IBM Cloudant.
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)

# Conectar con el servidor
client.connect()

# 2.  Crear una base de datos dentro de la instancia de servicio.

# Crear una instancia de la base de datos.
myDatabaseDemo = client.create_database(databaseName)

# Comprobar que ahora la base de datos existe.
if myDatabaseDemo.exists():
    print ("'{0}' successfully created.\n".format(databaseName))
    
    # Separar los resultados.
    print ("----\n")
    
    # 3.  Almacenar una pequeña colección de datos como documentos dentro de la base de datos.
    
    # Crear documentos utilizando los datos de ejemplo.
    # Examinar cada fila de la matriz para el documento en sampleData:
    # Recuperar los campos de cada fila.
    number = document[0]
    name = document[1]
    description = document[2]
    temperature = document[3]
    
    # Crear un documento JSON que represente todos
    # los datos de la fila.
    jsonDocument = {
    "numberField": number,
    "nameField": name,
    "descriptionField": description,
    "temperatureField": temperature
    }
    
    # Crear un documento utilizando la API de la base de datos.
    newDocument = myDatabaseDemo.create_document(jsonDocument)
    
    # Comprobar que el documento existe en la base de datos.
    if newDocument.exists():
        print ("Document '{0}' successfully created.").format(number)
        
        # Separar los resultados.
        print ("----\n")
        
        # 4.  Recuperar una lista completa de documentos.
        
        # Recuperación sencilla y mínima del primer
        # documento de la base de datos.
        result_collection = Result(myDatabaseDemo.all_docs)
        print ("Retrieved minimal document:\n{0}\n").format(result_collection[0])
        
        # Recuperación sencilla y completa del primer
        # documento de la base de datos.
        result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)
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
        
        # 5.  Suprimir la base de datos.
        
        # Suprimir la base de datos de prueba.
        try :
            client.delete_database(databaseName)
        except CloudantException:
            print ("There was a problem deleting '{0}'.\n").format(databaseName)
        else:
            print ("'{0}' successfully deleted.\n").format(databaseName)
            
            # 6.  Cerrar la conexión con la instancia de servicio.
            
            # Desconectar del servidor
            client.disconnect()
            
            # Finalizar la demo.
            print ("===\n")
            
            # Decir adiós.
            exit()
