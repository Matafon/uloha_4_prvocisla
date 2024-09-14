
def rozklad(zadane_cislo):
    i = 2
    mezera = True
    while zadane_cislo > 1:
        if zadane_cislo % i == 0:
            if mezera:
                print(i, end='')
                mezera = False
            else:
                print(' *', i, end='')
            zadane_cislo = zadane_cislo // i
        else:
            i = i + 1

zadane_cislo = int(input("Zadejte celé číslo: "))
rozklad(zadane_cislo)