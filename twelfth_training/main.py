# Obsługa wyjątków try,except
x = 12
y = 2
# print(x / y) # powstanie ZeroDivisionError
try:
    lista = []
    print(lista[0]) # powstanie IndexError
    print(x / y)
    print(x + "!") # powstanie TypeError
    print("Linjka po operacji")
except (ZeroDivisionError, TypeError): # podanie nazwy błędu lub nazw(wtedy używamy nawiasów okrąłych)
    print("Wystąpił jeden z dwóch błędów!")
except: # poprzez ":" przechwytuje wszystkie błędy.
    print("Inny błąd")
finally: # dodawany na samym końcu blok finally - służy do kończenia zadania niezależnie od bloku "try" czy złapie wyjątek czy nie.
    print("Finally: Wykonam się i tak!")
# except TypeError:
    # print("Błąd typów danych")
# Dzięki temu możemy wykonać dalesze instrukjce, podając użytkownikowi o przyczynie błedu.

print("Dalsze instrukcje ...")
