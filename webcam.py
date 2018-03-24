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
    cv2.putText(frame, "Druecke: Schwarz/Weiss = w | Sepia = s", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # warte auf Tastendruck (sonst sieht man das Fenster nicht)
    key = cv2.waitKey(1)

    # Tastenabfrage
    if key == 119:
        color = "sw"
    if key == 115:
        color = "sepia"
    if key == 110:
        color = "normal"

    # Farbeffekte
    if color == "sw":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if color == "sepia":
        sepia = numpy.asarray([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
        frame = cv2.transform(frame, sepia)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

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
