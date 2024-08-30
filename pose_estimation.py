"""
Script de estimación de pose utilizando OpenCV y MediaPipe.

Este script captura video en tiempo real desde la cámara del dispositivo y
utiliza MediaPipe para estimar y visualizar la pose humana en la imagen.
 
Presiona 'q' para salir del programa.

Requisitos:
- Python 3.x
- OpenCV
- MediaPipe
"""
# Importar librerías necesarias
import cv2
import mediapipe as mp
import time

# Inicializar MediaPipe Pose y herramientas de dibujo
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Configurar captura de video
cap = cv2.VideoCapture(0)

# Definir codec y crear un objeto VideoWriter para grabar el video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Iniciar estimación de pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break

        start_time = time.time()  # Iniciar tiempo de procesamiento

        # Convertir el frame a RGB para MediaPipe
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Procesar la imagen para detectar poses
        results = pose.process(image)

        # Restaurar la imagen a BGR para OpenCV
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Dibujar las landmarks y las conexiones en la imagen si se detecta una pose
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, 
                results.pose_landmarks, 
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),  # Rojo para los puntos
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)   # Verde para las líneas
            )
        
        # Calcular el tiempo de procesamiento
        processing_time = time.time() - start_time

        # Añadir texto de instrucciones e información adicional en la imagen
        cv2.putText(image, 'Human Pose Estimation', (100, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'mauricioaea/github.com', (10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, f'Time: {processing_time:.2f}s', (10, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        # Escribir el frame procesado en el archivo de video
        out.write(image)

        # Mostrar la imagen procesada
        cv2.imshow('Pose Estimation', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Liberar los recursos
cap.release()
out.release()  # Liberar el VideoWriter
cv2.destroyAllWindows()
