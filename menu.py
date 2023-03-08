import cv2
import time
import datetime
import os
from Detection import Detection
import signal
import sys
import readchar
from Face_Recognition import Recognition

# function to delte .mp4 files


def mp4_Deleter():
    for f in os.listdir():
        if f.endswith(".mp4"):
            os.remove(f)
    print("pliki usuniete")


# function to detect crtl + c


def handler(signum, frame):
    res = input(
        "Ctrl-c zostalo klikniete, czy jestes pewien ze chcesz wyjsc? y/n")
    if res == 'y':
        exit(1)


print("GUI IN PROGRES ...")
time.sleep(2)
os.system("cls")
while (True):

    signal.signal(signal.SIGINT, handler)

    print("""
    ###########################################################
    ###########################################################
                            MOZLIWE OPCJE
        1 - USUN WSZYSTKIE PLIKI MP4
        2 - WLACZ KAMERE (WYKRYWANIE TWARZY + NAGRYWANIE )
        3 - Rozpoznawanie twarzy na wlasnorecznie nauczonym modelu
    ###########################################################
    ###########################################################
    """)

    opcja = input("wybrana opcja (q- aby wyjsc): ")

    if opcja == "1":
        mp4_Deleter()
        # print(mp4_Deleter)
        time.sleep(2)
        os.system('cls')

    elif opcja == "2":
        Detection()
        time.sleep(2)
        os.system('cls')

    elif opcja == "3":
        Recognition()
        time.sleep(2)
        os.system('cls')

    elif opcja == "q":
        quit()

    else:
        print("wybrana opcja nie istnieje")
        time.sleep(1)
        os.system('cls')
