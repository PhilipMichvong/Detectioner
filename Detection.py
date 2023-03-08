import cv2
import time
import datetime
#import cascades as cas
from twilio.rest import Client
import tokens as TOKENS


def Send_MSG(SID, TOKEN, PHONE_NUMBER, MSG):
    client = Client(SID, TOKEN)
    client.messages.create(body=MSG, from_="+15627847757", to=PHONE_NUMBER)


limit = 0

# TODO rewrite this function


def Detected_part():
    global face_info, eye_info, face_info
    if len(eyes) > 0 and len(eyes) == 0:
        face_info = "wykryto twarz"
        return face_info
    elif len(eyes) > 0 and len(faces) == 0:
        eye_info = "wyrkyto oczy"
    elif len(eyes) + len(eyes) > 0:
        face_info = "wykryto twarz"
        return face_info
    else:
        return 0


def Detection():
    cap = cv2.VideoCapture(0)

    detection = False

    detection_stop_time = None

    timer_started = False

    SECONDS_TO_RECORD_AFTER_DETECTION = 2

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_fullbody.xml")

    eyes_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

    frame_size = (int(cap.get(3)), int(cap.get(4)))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:

        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        global faces, eyes, body

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)

        body = body_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) + len(eyes) > 0:

            if detection:
                timer_started = False
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(
                    f"{current_time}.mp4", fourcc, 30, frame_size)
                # cv2.imwrite()
                msg = "UWAGA, KAMERA WYKRYLA RUCH CZLOWIEKA"
                print("Rozpoznano czlowieka")
                print("Rozpoczynam Nagrywanie")
                #liczba = 0
                global limit
                limit += 1
                if limit == 1:
                    #Send_MSG(TOKENS.SID, TOKENS.TOKEN, TOKENS.PHONENUMBER, msg)
                    pass
                else:
                    print("sms zostal wyslany")

        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    detection = False
                    timer_started = False
                    out.release()
                    print('Czlowiek zniknal z pola widzenia')
                    print('Koniec Nagrywania')
            else:
                timer_started = True
                detection_stopped_time = time.time()

        if detection:
            out.write(frame)
        for (x, y, width, height) in faces:

            center = (x+width//2, y + height//2)

            cv2.ellipse(frame, center, (width//2, height//2),
                        0, 0, 360, (255, 0, 0), 3)
            cv2.putText(frame, "FACE", (x, height-y+10),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        for (x, y, width, height) in eyes:
            center = (x+width//2, y + height//2)

            cv2.ellipse(frame, center, (width//2, height//2),
                        0, 0, 360, (255, 0, 0), 3)

        for (x, y, width, height) in body:
            cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 3)

        cv2.imshow("Detection_Szpregiel", frame)

        if cv2.waitKey(1) == ord("q"):
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()
