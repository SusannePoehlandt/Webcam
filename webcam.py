import cv2
import numpy

# initialisiere Webcam
cam = cv2.VideoCapture(0)
color = "normal"

# zeige Stream von WebCam an
while cam.isOpened():
    # lese frame von WebCam
    ret, frame = cam.read()

    # Anweisung anzeigen
    cv2.putText(frame, "Druecke: Schwarz/Weiss = w", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # warte auf Tastendruck (sonst sieht man das Fenster nicht)
    key = cv2.waitKey(1)

    # Tastenabfrage
    if key == 119:
        color = "sw"
    if key == 115:
        color = "sepia"
    if key == 110:
        color = "normal"

    # Farbeffekt
    if color == "sw":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if color == "sepia":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # zeige Frame an
    cv2.imshow("Webcam", frame)

    # wenn ESC gedrueckt, beende Programm
    if key == 27:
        break
    # Ausgabe Tastenwert
    elif key == -1:
        continue
    else:
        print key
