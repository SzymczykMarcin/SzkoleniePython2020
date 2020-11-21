__all__ = ['Osoba', 'statystyczny_kowalski']

class Osoba:

    def __init__(self, imie, nazwisko, wiek, praca):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.praca = praca
        self._stan_konta = 0
        self.hobby = ['literatura', 'film', 'szachy']

    def wyplata(self, kwota):
        self._stan_konta += kwota

    def zakupy(self, kwota):
        self._stan_konta -= kwota


def statystyczny_kowalski():
    kowalski = Osoba('Jan', 'Kowalski', 43, 'Policjant')
    return kowalski

class Smieci:

    def __init__(self, waga):
        self.waga_smieci_w_kg = waga

    def podaj_wage(self):
        print(self.waga_smieci_w_kg)

if __name__ == '__main__':
    s = Smieci(15)
    s.podaj_wage()
