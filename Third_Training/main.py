# x = True
# y = False
# True i False - tryb logiczny, zerojedynkowy
# print(x)
# print(y)
print(5 == 1) # operator równania "==". Zwraca typ logiczny albo True albo False.
print(5 != 1) # operator różnicy "!-".
print(5 > 5) # operator porównania - większe ">".
print(5 < 1) # operator porównania - mniejsze "<".
print(5 <= 5) # operator mniejsze, bądź równe "<=".
print(5 >= 1) # operator większe, bądź równe "<=".
# if - instrukcje warkunkowe. ("Czy? lub Jeżeli")
if 5 == 5: # instrukcje warunkową if. Definiuje czy posiada wartość True czy False.
    print("Prawda") # Jeżeli, będzie False nie zadziała print!
print("Koniec") # Bez wcięcia czterospacjowego jest już osobną instrukcją.
x = 15
y = 15
if x > y: # Pierwszy warunek!
    print(("X Większe Y"))
elif x < y: # Instrukcja "elif" - sprawdza w razie czego jeżelu pierwszy warunek "if" nie zostanie wykonany!
    print("X Mniejsze Y")
elif x == 10:
    print("X Równe 10")
else: # Instrucja "else" ("w przeciwnym razie") - nie sprawdza żadnego warunku. Zawsze na koću warunków "if"!
    print("X Równe Y")