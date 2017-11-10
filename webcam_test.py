import cv2
import numpy as np

camara = cv2.VideoCapture(0) # Cero es la webcam local

while(True): # Si no esta dentro de un loop solo tomara una foto
    
    _, cuadro = camara.read() # Confirmar que si existe un input
    
    gray = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY) # Blanco y negro
    
    retval, threshold = cv2.threshold(gray, 68, 255, cv2.THRESH_BINARY) # Convertir a version simplificada
    
    cv2.imshow('65', threshold) # Mostrar la imagen
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
camara.release() # Si no pones esto la camara seguira usandose