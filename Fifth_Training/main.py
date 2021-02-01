i = 0

# while i < 5: # pętla "while" - "dopóki" warunek po jej prawej stronie jest prawdziwy to wykonuj segment kodu. Jeżeli wpiszemy True zamiast i < 5 zawsze będzie nieskończone.
    # print(i)
    # i += 1 # dodajemy do i "1". Wyprintuje od 0-4. Ważne, żeby nie zrobić pętni nieskończonej. Bez tego wykonywało by się w nieskończoność. INKREMENTACJA - zwiększanie wartości zmiennej o jeden!
    # if i > 5:
        # break # "break" = "złam, przerwij" - przerywa pętle w której się znajdujemy.
# print("Koniec")

while True:
    i += 1
    if i % 2 == 1: # sprawdzenie czy reszta jest 1 lub 0: Znak "%" - reszta dzielenia. Jeżeli zostaje "1" - liczby niepażyste, "0" - liczby pażyste.
        continue # "continue" - "kontynuuj": z tego miejsca kodu skocz do kolejnego obiegu pętli, wykonaj kolejny obieg pętli z pominięciem wszystkiego co stoji po kodzie continue.
    print(i) # wydrukuje od 2 - 12, ponieważ 12 jest większe od 10! Nie drukowało 11 ponieważ nie drukowało liczb nieparzystych.
    if i > 10:
        break

print("Koniec")