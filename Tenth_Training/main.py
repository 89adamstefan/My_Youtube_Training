def func(x):
    return x * x


zmienna = func  # podawanie bez nawiasu po funkcji, zmienna przejumje ta funkcje
print(zmienna(5))


def func2(f1, x):
    return f1(x) * x  # jako argument musimy posłać drugą funcje.


print(func2(func, 5))  # jako argument podajemy pierwszą funcję, bez nawiasów okrągłych.


# rekurencja wewnątrz funkcji
# silnia z !3 = 3 * 2 * 1 = 6 (wykrzyknik i liczba to silnia)
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1) # funkcja silnia wywołuje jeszcze raz funkcje silnia

print(silnia(5))
print(silnia(4))
print(silnia(2))
print(silnia(1))
print(silnia(9))