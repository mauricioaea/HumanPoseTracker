# hola, en esta oportunidad dejare el codigo que te permitira ejecutar ESTIMACIÓN DE POSE

1. activamos el entorno virtual en instalamos las librias que se requiere para este proyecto
- python-opencv
- mediapipe

pip install opencv-python mediapipe

2. Importamos 
import cv2
import mediapipe as mp

3. Inicializar los módulos de MediaPipe


import cv2
import mediapipe as mp

# Inicializar MediaPipe Pose y herramientas de dibujo
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Configurar captura de video
cap = cv2.VideoCapture(0)

# Iniciar estimación de pose con parámetros de confianza ajustados
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

- mp.solutions.pose: MediaPipe ofrece una serie de soluciones para diferentes tareas de visión por computadora, como la detección de manos, caras, y en este caso, la detección de pose. Al escribir mp.solutions.pose, estamos accediendo a la solución específica que se encarga de la detección de pose humana.

- mp_pose: Estamos asignando esta solución de MediaPipe a la variable mp_pose. Esto nos permite utilizar mp_pose más adelante en el código para trabajar con las funcionalidades relacionadas con la estimación de pose.

- mp_drawing = mp.solutions.drawing_utils
Esta línea hace lo siguiente:

- mp.solutions.drawing_utils: MediaPipe no solo proporciona herramientas para detectar poses, sino que también incluye utilidades para dibujar esas poses y los puntos clave en una imagen o video. drawing_utils es un módulo de utilidades que facilita este proceso de dibujo.

- mp_drawing: Asignamos este módulo a la variable mp_drawing, lo que nos permitirá utilizar las funciones de dibujo de MediaPipe en nuestro código.

En resumen, esta línea nos permite acceder a las herramientas que nos ayudan a dibujar en la imagen o video las poses humanas detectadas, mostrando visualmente los puntos clave y las conexiones entre ellos.


Así, mp_pose se encarga del "pensamiento" (la detección de la pose), y mp_drawing del "arte" (dibujar la pose en la imagen o video).

4. ## Capturamos la entrada de video

cap = cv2.VideoCapture(0)

5. ## d. Procesar cada fotograma para la estimación de pose
Aquí procesaremos cada fotograma del video para detectar y estimar las poses:



Recuerda, si necesitas ayuda en tus proyectos no dudes en contactarme [mauricioandreserazo@outlook.com] tel [+57 3102482881]

- SIMPLER 
- SMARTER
- FUTHER

