import os
from PIL import Image
import numpy as np
import cv2
import pickle

# funckja do nauczenia rozpoznawania osob, na podstawie ich zdjec
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MY_image_dir = os.path.join(BASE_DIR, "Faces_to_Learn")

recognizer = cv2.face.LBPHFaceRecognizer_create()

face_cascade = cv2.CascadeClassifier(  # default
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
current_id = 0
label_ids = {

}
y_labels = []
x_train = []
# funckja umozliwiajaca nam uczenie, przypisana do zmiennej recognizer


# przejscie petla przez wszystkie obrazy dla mnie
for root, dirs, files in os.walk(MY_image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)

            label = os.path.basename(root).replace(" ", "-").lower()
            # label - nazwa katalogu, path- nazwa pliku
            # print(label, path)
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            # print(label_ids)
            # przekonwertowanie obrazow na czarno biale
            pil_image = Image.open(path).convert("L")
            # zapisanie obrazow do numpy tablicy, bierze ona kazdy pixel
            # i zamienia go na pewien numer mu odpowaidajacy, wiec pod tymi numerami
            # kryje sie obraz
            image_array = np.array(pil_image, "uint8")
            # print(image_array)
            faces = face_cascade.detectMultiScale(
                image_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                # roi (region of intrest)
                roi = image_array[y:y+h, x:x+w]
                # "wlozenie" danych uczacych do tablicy x_train
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print("====================")
# print(x_train)
# zapisywanie id zdjec do osobnego pliku do uczenia
with open("labels.pickle", 'wb') as f:
    # w tym pliku do id, przypisane bedzie imie osoby na ktorej siec sie uczyla
    pickle.dump(label_ids, f)
# rozpoczynanie nauki
recognizer.train(x_train, np.array(y_labels))
# koniec uczenia, zapisanie do pliku
recognizer.save("trainner.yml")
