# Rzucanie wyjątków raise, assert
def dzielenie(x, y):
    assert y != 0, "Y == 0" # Zwraca swój typ wyjątku "AssertError" wtedy jak warunek jest nieprawdziwy, przerywa program. Po przecinku jako drugi warunek podajemy info w konsoli.
    if y == 0:
        raise ZeroDivisionError("Dzielnie przez 0") # przechwytywanie samemu błędu poprzez "raise"
    print(x / y)
try:
    dzielenie(2,0)
except ZeroDivisionError:
    print("Nie dziel przez '0' cholero!")
    raise # dzięki czemu najpierw wyświetli sie linijka błędu a później wywoła się błąd