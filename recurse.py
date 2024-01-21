seznam1 = [1, 2, 3]
seznam2 = [1, 2, 3, 4, 5]
seznam3 = [2, 3, 4, 5]
seznam4 = [3, 4, 5]
seznam5 = [4, 5]


def zpracuj_seznamy(data1, data2):
    while data1:
        kopie_seznamy = data1.copy()
        for seznam in kopie_seznamy:
            if all(x in data2 for x in seznam[1:]):
                data2.append(seznam[0])
                data1.remove(seznam)


def porovnej_seznam1(seznam1, ziskana_data):
    if all(x in ziskana_data for x in seznam1):
        print("seznam1 obsahuje stejná data jako ziskana_data.")
    else:
        print("seznam1 neobsahuje stejná data jako ziskana_data.")


def ziskej_nejvyssi_cislo(data):
    vsechny_pole = [0]
    for pole in data:
        vsechny_pole.extend(pole)

    nejvyssi_cislo = max(vsechny_pole)

    hodnoty = [nejvyssi_cislo]

    return hodnoty


seznamy = [seznam2, seznam3, seznam4, seznam5]
ziskana_data = ziskej_nejvyssi_cislo(seznamy)

zpracuj_seznamy(seznamy, ziskana_data)
porovnej_seznam1(seznam1, ziskana_data)
print(ziskana_data)
