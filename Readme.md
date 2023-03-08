# Załorzenia projektu

Projekt stworzony został w języku "python", był on formą zaliczenia projektu na 4 roku studiów informatycznych. Działa on na zasadzie 2 zintegorwanych skryptów, z których to jeden działa jako "kamera ochrony" rozpoczynając nagrywanie w momencie gdy oko kamery wykryje ludzką sylwetke. Drugi rozpoznaje mnie jako autora aplikacji, co ma umożliwić nie włącznie nagrywania w momencie gdy to ja znajduję się w oku kamery. Sieć nauczona jest również rozpoznawać jednego z polskich aktorów (co umożliwiło lepsze testowanie aplikacji)

</br>
</br>
</br>

# instalcja projektu

pip upgrade

    python -m pip install --upgrade pip

pobierz github repo

    git clone https://github.com/PhilipMichvong/Detectioner

Przejdz do odpowiedniego katalogu

    cd {twój_katalog}

Zainstaluj wirtualne środowisko

    python -m pip install virtualenv

zainicjuj wirtualne środowisko

    python -m venv ./.venv

aktywuj

    ./.venv/Scripts/activate

zainstaluj wymagane moduły

    python -m pip install -r ./requirements

rozpocznij działanie programu

    python menu.py

</br>
</br>
</br>

# Wykorzystane biblioteki

## cv2

OpenCV jest biblioteką zawierającą wiele standardowych operacji wykorzystywanych przy przetwarzaniu obrazów. Jej niebywałą zaletą jest fakt, że implementacja jest bardzo wydajna i niektóre operacje potrafią być nawet 6x szybsze niż w innej popularnej bibliotece Pillow (PIL).

## Twilo.rest

Interfejs API REST firmy Twilio umożliwia wyszukiwanie i zarządzanie metadanymi dotyczącymi konta, numerów telefonów, użytkowania i tokenów dostępu. Jest to biblioteka którą wykorzystuje skrypt do wysłania sms’a użytkownikowi

## Numpy

Biblioteka NumPy, w Python, została stworzona, aby umożliwić szybkie i sprawne operacje na macierzach. Każdy element jest tego samego typu – zazwyczaj są to liczby. Na jej podstawie stworzono, między innymi bibliotekę Pandas. Jest to jedna z pierwszych bibliotek, z którymi chcemy się zaznajomić, pracując przy analizie danych oraz sztucznej inteligencji

## Pickle

Moduł pickle pozwala na serializację i deserializację obiektów Pythona. Uzyskany w ten sposób ciąg bajtów można zapisać do pliku lub przesłać przez sieć. Dane zapisane w pliku mogą później posłużyć do odtworzenia stanu programu przy jego kolejnym uruchomieniu.
</br>
</br>
</br>

# Opis skryptów w projekcie

## Face-train.py

Początkowo dane rozdzielane są na zdjęcie oraz katalog w którym się znajdują, a także zainicjowana zostaje zmienna recognizer wykorzystująca bibliotekę cv2 inicjalizuję w ten sposób przyszłe rozpoczęcie uczenia sieci algorytmem LBP (Local Binary Patterns) to jeden ze sposobów na wyodrębnienie charakterystycznych cech obiektu (może to być twarz, filiżanka do kawy lub cokolwiek, co ma swoją reprezentację). Algorytm LBP jest naprawdę prosty i może być wykonany ręcznie. (Progowanie pikseli + operacje arytmetyczne na poziomie pikseli).

Następnie dla wszystkich danych uczących w formacie „png” lub „jpg” wykonywana jest zamiana „znaków białych” (spacji) na „-„ w celu uniknięcia błędów, a także wszystkie litery zmieniane są na małe.

Następnie do danych uczących w osobnych katalogach przypisywane są odpowiednie niepowtarzalne id (np., katalog z moimi zdjęciami – 1, katalog ze zdjęciami aktora – 2, katalog ze zdjęciami innego studetna -3 etc.)

Następnie przy wykorzystaniu funkcji conver, zdjęcia konwertowane są na czarno białe, ponieważ na takich uzyskamy zdecydowanie bardziej miarodajne efekty.

A w kolejnym kroku skrypt zamienia obrazy na tablice liczbowe z wykorzystaniem funkcji array z biblioteki numpy.

Następnie wyznaczamy ROI naszych zdjęć (czyli region of intrest, region zainteresowania) jest to nam potrzebne aby nie analizować całości zdjęcia a tylko interesujący nas element, twarz.

Następnie wyznaczamy ROI naszych zdjęć (czyli region of intrest, region zainteresowania) jest to nam potrzebne aby nie analizować całości zdjęcia a tylko interesujący nas element, twarz.

Następnie wyznaczamy ROI naszych zdjęć (czyli region of intrest, region zainteresowania) jest to nam potrzebne aby nie analizować całości zdjęcia a tylko interesujący nas element, twarz.
</br>

## Face_Recognition.py

W tym skrypcie posługujemy się nauczonym przez nas plikiem w celu wykrycia na zdjęciu twarzy a następnie rozpoznania jej, wykorzystujemy takie funkcje jak:
</br>

### cv2.CascadeClassifier:

Do zaimplementowania modelu do rozpoznawania kontur twarzy z biblioteki cv2
</br>

### cv2.VideoCapture:

Do rozpoczęcia przechwytywania obrazu z kamery

</br>

### cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

Do analizy obrazu z kamery w obrazie czarno białym

</br>

### face_cascade.detectMultiScale

Do rozpoznawaniu wielu twarzy w jednym oku kameru a także do zdefiniowania współczynnika pewności ( im większy tym dokładniej rozpozna twarz, jednak może też częściej nie rozpoznać mniej wyraźnej)
</br>

### recognizer.predict

Funkcja do przewidywania dokładności rozpoznania twarzy z nauczonej przez nas sieci
</br>

### cv2.putText

Funkcja do wypisania tekstu w oknie kamery utworzonym przez bibliotekę cv2

# tokens.py

W celu poprawnego działania skryptu, należy wartości w pliku tokens.py uzupełnić własnym numerem telefonu, a także Tokenem wygenerowanym na stronie twórców API Twilo.rest
