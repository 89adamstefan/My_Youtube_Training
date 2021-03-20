# Moduły(Module) - biblioteki
# import random # poprzez import dodajemy biblioteki już zainstalowane
from random import randint # importowanie odpowiedniego pakietu z np. random
from math import pi # funkcja kółeczko czerwone "f", stała kółeczko żółte "v"
from math import sqrt as pierwiastek # importowanie i nadawanie własnej nazwy poprzez dodanie na końcu "as"!


# print(random.randint(1, 10)) # korzystanie z opcji w random - po kropce podajemy czego chcemy użyć. randit wybiera losowe liczbę z przedziałóu jaki podamy np. (1, 10)
print(randint(1, 10))
print(pi)
print(int(pierwiastek(16)))