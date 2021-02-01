wiek = 19
kasa = 10

# if wiek >= 18:
    # if kasa >= 35: # zagnieżdżanie instrukcji warunkowych. Wykonuje się tylko, jeżeli pierwszy "if" się zgadza.
        # print("Może wejść")
# if wiek >= 18 and kasa >= 35: # używamy operatora logicznego który wie jak to połączyć. Tutaj używamy operatora "and" - "i"! Zwraca wartośc jeżeli wszystko jest prawdziwe.
    # print("Może wejść")
# if wiek <= 12 or kasa >= 30: # Bilet dla dzieci darmowy poniżej lub równy 12 lat. Inni płacą 30pln. Tutaj używamy operatora "or" - "lub"!
    # print("Może wejść")
# if not wiek > 12 or kasa >= 30:  # Operator jednowarunkowy: działa on na pojedyńczeń wartości logicznej True i False. Możemy wartośći zanegować. Operator negacji! "not" zawsze zmienia wartość zamiast False True, zamiast True - False!
    # print("Może wejść")
# else:
    # print("Nie może wejść")

if (True or False) and not False: # Wagi operatorów: "and" - logiczne mnożenie, "or" - logiczne sumowanie. Wykomuje się jako pierwsze "and" a jako drugie "or"! Możemy przeciążać - zmieniać poprzez nawiasy.
    print("Prawda")
else:
    print("Fałsz")