# Funkcje
def funckja_test():
    print("Funkcja...")


funckja_test()  # Wywolanie funkcji
funckja_test()  # Mozna wywolywac ja wiele razy, CTRL + D - kopiowanie wiersza


def dodaj(x):  # W nawiasie podajemy argumenty
    print(x + 1)


zmienna = dodaj(2)
print(zmienna) # wydrukuje None, poniewaz nie ma skoku "return"

def dodaj(x,
          y=1,
          z=0):  # Kolejne argumenty podajemy po przecinku, jezeli uzyjemy znaku "=" nie przeciazymy funkcji mimo nadpisania jej, argument ze znakiem "=" musi byc zawsze na koncu!
    return x + y + z
    # print("Czy ja istnieje") # po return kazda kolejna linijka kodu jest nieosiagalna!


dodaj(5, 2)
dodaj(2)  # przeciazenie funkcji "dodaj"
dodaj(2, 3, 5)
print(dodaj(2, 4, 5))  # jezeli zamykamy funkcje z return, musimy ja na koncu wyprintowac
wynik = dodaj(1, 5, 7)  # dodanie funkcji do zmiennej
print(wynik)
