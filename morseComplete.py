class MorseTranslator:
    def __init__(self):
        self.samohlasky = ['A', 'Á', 'E', 'É', 'Ě', 'I', 'Í', 'O', 'Ó', 'U', 'Ú', 'Ů', 'Y', 'Ý']

    def morse_znak(self, slovo):
        je_samohlaska = slovo[0].upper() in self.samohlasky
        return '.' if je_samohlaska else '-'

    def nahradit_interpunkci(self, s):
        interpunkce = [',', '.', '!', '?', ';', ':']

        for znak in interpunkce:
            s = s.replace(znak, ',')

        oddeleny_text = s.split(',')
        oddeleny_text = [cast.strip() for cast in oddeleny_text if cast.strip()]

        return ', '.join(oddeleny_text)

    def prelozit_do_morse(self, vstup):
        vstup = self.nahradit_interpunkci(vstup)

        slova = []
        aktualni_slovo = ""

        for znak in vstup:
            if znak.isalpha() or znak in ['A', 'Á', 'E', 'É', 'Ě', 'I', 'Í', 'O', 'Ó', 'U', 'Ú', 'Ů', 'Y', 'Ý']:
                aktualni_slovo += znak
            elif znak in [',', '.', '!', '?', ';', ':']:
                if aktualni_slovo:
                    morse_pro_slovo = self.morse_znak(aktualni_slovo)
                    slova.append(morse_pro_slovo)
                    slova.append(' ')
                    aktualni_slovo = ""
            elif znak.isspace():
                if aktualni_slovo:
                    morse_pro_slovo = self.morse_znak(aktualni_slovo)
                    slova.append(morse_pro_slovo)
                    aktualni_slovo = ""

        if aktualni_slovo:
            morse_pro_slovo = self.morse_znak(aktualni_slovo)
            slova.append(morse_pro_slovo)

        vysledek = "".join(slova)
        return vysledek

class MorseTranslator2:
    def __init__(self):
        self.morse_abeceda = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z',
        }

    def prelozit_z_morse(self, vstup):
        vstup = vstup.split(' ')
        prelozeny_text = ""

        for znak in vstup:
            if znak in self.morse_abeceda:
                prelozeny_text += self.morse_abeceda[znak]
            elif znak == '':
                prelozeny_text += ' '

        return prelozeny_text


def main():
    translator = MorseTranslator()
    vstup = input("Zadejte text: ")
    vysledek = translator.prelozit_do_morse(vstup)
    print(f"Výsledek: {vysledek}")

    translator2 = MorseTranslator2()
    prelozeny_text = translator2.prelozit_z_morse(vysledek)
    print(f"Prelozeny text: {prelozeny_text}")


if __name__ == "__main__":
    main()

