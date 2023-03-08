import numpy as mp
import cv2
import pickle

face_cascade = cv2.CascadeClassifier(  # default
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainner.yml')

labels = {
    "person_name": 1
}

with open("labels.pickle", 'rb') as f:
    # podobnie jak przy uczeniu, tylko w tym momencie odczytujemy plik z nazwami dla nauczonych danych
    original_labels = pickle.load(f)
    #  dane w pickle zapisywane sa w sposb specyficzny, do poprawnego
    # wypisania rozpoznanej osoby, rekordy musimy "odwrocic", to
    # wlasnie wykonuje ta petla
    labels = {v: k for k, v in original_labels.items()}


def Recognition():
    cap = cv2.VideoCapture(0)

    while (True):
        _, frame = cap.read()
        # zamiana kolorw z kamery na czarno biale, poniewaz na takich latwiej
        # jest mi rozpoznawac i uczyc
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            # testowanie otrzymanych wartosci polozenia twarzy
            # print(x, y, w, h)
            # ustawiamy roi, czyli regiom of intrest,
            # przez co nie bedzie nam zapisywalo calosci zdjecia
            # kamery, a jedynie interesujaca nas czesc, twarz
            roi_gray = gray[y:y+h, x:x+w]  # (y_cord_start, ycord_end)cle
            # to samo co powyzej, ale w kolorze
            roi_color = frame[y:y+h, x:x+w]
            # przypisanie "pewnosci" (conf) przy rozpoznawaniu (od 0-100)
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45 and conf <= 85:
                # print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1,
                            color, stroke, cv2.LINE_AA)
            img_item = f'my-image{w}.png'
            # zapisanie obrazka do testow
            cv2.imwrite(img_item, roi_gray)

            # BGR, dziwny zapis koloru w tej bibliotece, poniewaz zazwyczaj jest to RGB
            color = (255, 0, 0)

            stroke = 2  # grubosc lini
            end_cord_x = x + w
            end_cord_y = y + h
            # rysowanie kwadratu dookola mojej twarzy

            # deep learning model, do rozpoznawania, nauczony przeze mnie

            cv2.rectangle(frame, (x, y), (end_cord_x,
                          end_cord_y), color, stroke)

        cv2.imshow('Face_recognite', frame)

        # mozliwosc wyjscia z kamery po wcisnieciu "q"
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
