from ibm_watson import VisualRecognitionV3
import json
import cv2
import time
import math

visual_recognition = VisualRecognitionV3(
    '2019-07-10',
    iam_apikey='p9i3A4rnsSzhGacf8iThcKmdvSPC5WqdjEddEdPz2dq8')

    
#Inicializar la camara

while True:
   
    capture = cv2.VideoCapture(1)
    frameRate = capture.get(1) #frame rate
    #Capturar un frame
    val, frame = capture.read()
    capture.release()
    
    cv2.imwrite("frame.jpg", frame)
    with open('./frame.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0',
            classifier_ids='DefaultCustomModel_1863503387').get_result()

    print(json.dumps(classes, indent=2))

    #Mostrar la imagen
    cv2.imshow('Imagen', frame)
    #Salir con 'ESC'
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    time.sleep(5)
