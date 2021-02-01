# lista - w odróżnieniu od zmiennej może przechować więcej wartości.
zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "d", "e", ]
print(lista)
print(lista[4]) # odwłoanie do konkretnego elementu poprzez "[]", numerowane są od wartości "0" tzn. 1 jest nr. 0 a "e" nr. 4
lista[2] = 3 #modyfikowanie danego elementu z listy
print(lista)
tekst = "Hello World"
print(tekst[0]) # drukowanie konkretnego elementu |"H"|
print(lista + ["f", "g"]) # dodawanie do listy nowych elementów
print(lista * 3) # mnożenie listy wydrukuje" [1, 2, 3, 'd', 'e', 1, 2, 3, 'd', 'e', 1, 2, 3, 'd', 'e']
print("Ilość elementów: ", len(lista)) # mierzenie ilości elementów poprzez "len"
lista.append("f") #metoda i funkcja prawie jedno i to samo. Operator "." pozwala się odłować do elemtów które są zawarte w obiekcie "lista".
# append - dołącz. Append dołacza do listy jeszcze jeden element na końcu listy.
print(lista)
lista.append(["g", "h"]) # poprzez append dodawanie kolejnej listy. Lista w liście,
print(lista)
print(lista[6][1]) # trzeba podać dwa indexy: pierwszy nawias określa początek listy w liscie drugi nawias index wartości w liście w liście... :)
lista.insert(3, 3) # insert dołącza element we wskazanym przez nas miejscy(indexie) - jako pierwsze w nawiasie nr. indexu a po przecinku wartość.
print(lista)
print("Ilość:", lista.count(3)) # metoda count zlicza ilośc wystąpień danego znaku np. w całej liście.
print("Index:", lista.index(3)) # metoda podaje numer indexu obiektu którego ma zwrócić. Pierwsze wystąpienie podaje! Tzn. jak są dwie "3" poda index pierwszej napotkanej.
lista.remove("f") # metoda usuwa dany element z listy.
print(lista)
lista2 = [1, 20, 35, -5, 0] # funcje na samych liczbach.
print("Min: ", min(lista2)) # metoda "min" podaje minimalną wartość w liście.
print("Max: ", max(lista2)) # metoda "max" podaje maksymalną wartość w liście.
lista2.sort() # sortuje elementy od najmniejszego do największego.
print(lista2)
lista2.reverse() # Odwracanie elementów w liście.
print(lista2)
lista2.clear() # metoda czyszczenia listy - wszystkie elementy zostaja usunięta z listy, pozostaje pusta lista.
print(lista2)