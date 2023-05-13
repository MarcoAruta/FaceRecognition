import cv2

# Crea un oggetto VideoCapture per acquisire il video dalla webcam
cap = cv2.VideoCapture(0)

# Crea un oggetto CascadeClassifier per la rilevazione dei volti
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')

while True:
    # Legge un frame dal video
    ret, frame = cap.read()

    # Rileva i volti nel frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    # Disegna un rettangolo intorno ai volti rilevati
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostra il frame con i volti rilevati
    cv2.imshow('frame', frame)

    # Interrompe il ciclo se viene premuto il tasto 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia le risorse
cap.release()
cv2.destroyAllWindows()