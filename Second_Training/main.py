print("Kolejność:")
print(2 + 2 * 2) # Python zna kolejność działań matematycznych.
print((2 + 2) * 2) # Poprzez nawiasy możemy zmienić kolejność działania - zawsze używamy nawiasów okrągłych!
print("Dzielenie:")
print(5 / 2) # float - zmiennioprzecinowe np. 2.5.
print(5 // 2) # int (intiger) - ile w całości jest liczb! Bez przecinka!
print("Mnożenie:")
print(2 * 3)
print(2 ** 3) # Potęgowaie poprzez "**".
print("Skrócone:")
x = 5 # Tworzenie zmiennej.
x = x + 1 # Zwiększnie operatora o 1.
print(x)
x += 1 # Skrócona wersja dodawania do wartości "x".
print(x) # CTRL + D (kopiowanie) CTRL + SHIFT + STRZAłKA (przeniesienie np. w dół)
# x++ - błąd implementacji
# x-- - błąd dekramentacji
print("Konwersja:") # Kowersja typów - zmienne nie są typowane.
# int - liczby całkowite, str - ciąg znakowy (łańcuch)
a = input("Podaje 1 liczbę: ") # input to co zwraca jest jako typ string domyślnie! Tzn. w zadaniu wyjdzie "55" zamiast "10".
b = input("Podaje 2 liczbę: ")
print(a + b)
print(int(a) + int(b))
print(float(a) + float(b)) # Do odzielania wartości używamy "."  a nie ",".
y = 2
z = 2
print(str(y) + str((z)) # Zmiana na stringa!
# del y # usuwanie zmiennej "del" - delete.
# print(str(y) + str((z)) # Zmiana na stringa!