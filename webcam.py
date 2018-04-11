import cv2
import numpy

# initialisiere Webcam
cam = cv2.VideoCapture(0)
mode = "normal"

#Anweisung in Konsole anzeigen
print "Druecke: \nNormal = n \nProtanopia = p \nDeuteranopia = d \nTritanopia = t \nAchromatopsia = a \nKatarakt = k"

# zeige Stream von WebCam an
while cam.isOpened():
    # lese frame von WebCam
    ret, frame = cam.read()

    # Anweisung anzeigen
    cv2.putText(frame, "Druecke: Normal = n | Protanopia = p | Deuteranopia = d | Tritanopia = t | Achromatopsia = a | Katarakt = k" , (20, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # warte auf Tastendruck (sonst sieht man das Fenster nicht)
    key = cv2.waitKey(1)

    # Tastenabfrage
    if key == 112:
        mode = "protanopia"
    if key == 100:
        mode = "deuteranopia"
    if key == 116:
        mode = "tritanopia"
    if key == 97:
        mode = "achromatopsia"
    if key == 107:
        mode = "katarakt"
    if key == 110:
        mode = "normal"

    # Farbeffekte
    if mode == "protanopia":
        bgr = numpy.asarray([[0, 0.558, 0.567],
                            [0.242, 0.442, 0.433],
                            [0.758, 0, 0]])
        frame = cv2.transform(frame, bgr)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if mode == "deuteranopia":
        bgr = numpy.asarray([[0, 0.70, 0.625],
                            [0.30, 0.30, 0.375],
                            [0.70, 0, 0]])
        frame = cv2.transform(frame, bgr)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if mode == "tritanopia":
        bgr = numpy.asarray([[0, 0, 0.95],
                            [0.475, 0.433, 0.05],
                            [0.525, 0.567, 0]])
        frame = cv2.transform(frame, bgr)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if mode == "achromatopsia":
        frame = cv2.blur(frame, (10,10))
        bgr = numpy.asarray([[0.299, 0.587, 0.114],
                            [0.299, 0.587, 0.114],
                            [0.299, 0.587, 0.114]])
        frame = cv2.transform(frame, bgr)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Gruener Star
    if mode == "katarakt":
        frame = cv2.blur(frame, (20,20))
        h, s, v = cv2.split(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
        s = numpy.clip(s,0,95)
        frame = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)

    # zeige Frame an
    cv2.imshow("Webcam", frame)

    # wenn ESC gedrueckt, beende Programm
    if key == 27:
        break
