lista = ["Subskrybuj", "Kanał", "o", "Wszystkim", ]

i = 0 #zmienna pomocnicza, pomaga iterować po indexach listy. Dlaczego 0 ponieważ nr. indexu zaczyna się od 0
while i < len(lista):
    print(lista[i])
    i += 1 #pomoc w iterowaniu po kolejnych indexach. +1 - jeżeli tego nie damy pętla będzie się wykonywać bez końca

for x in lista: #for - przez / podajemy nową zmienną np. "x" - przyjmuje argumenty z kolekcji. Przez to może wykonywać element po elemencie.
    print(x)

print(list(range(10)))#funkcja range - przechowuje kolekcje, buduje liste i uzyskujemy listę która stara się osiągnać 10 ale nigdy jej nie osiągnie / funkcja list wyświetla listę elementów.

for y in range(10): # Wykona pętla się razy 10 - "0-9"
    print(y +1) #jak dodamy 1 to wydrukuje od 1-10 tzn. print(y + 1)

for z in range(1, 10): # tutaj zacznie od drugiego argumentu wydrukuje 1-10
    print(z)

for v in range(1, 11, 2): # zacznin od argumenty od 1 do 11 z przeskokiem o 2 argumenty. Wydrukuje wartości nieparzyste
    print(v)