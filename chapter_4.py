__all__ = ['Osoba', 'statystyczny_kowalski']


class Osoba:

    def __init__(self, imie, nazwisko, wiek, praca):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.praca = praca
        self._stan_konta = 0
        self.hobby = ['literatura', 'film', 'szachy']

    @property
    def praca(self):
        with open(r'C:\projects\SzkoleniePython2020\testowy\text.txt', 'r') as nasz_plik:
            self.__praca = nasz_plik.read()
        return self.__praca

    @praca.setter
    def praca(self, praca):
        with open(r'C:\projects\SzkoleniePython2020\testowy\text.txt', 'w') as nasz_plik:
            nasz_plik.write(praca)
        self.__praca = praca


    def __str__(self):
        return f'Imię: {self.imie}\nNazwisko: {self.nazwisko}'

    def __repr__(self):
        return f'Imię: {self.imie}\nNazwisko: {self.nazwisko}\nWiek: {self.wiek}'

    def __getitem__(self, item):
        return self.hobby[item]

    def __add__(self, other):
        self._stan_konta += other._stan_konta

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
    o = statystyczny_kowalski()
    # o._stan_konta = 2
    #     # o2 = Osoba('Maria', 'Kowalska', 37, 'Malarka')
    #     # o2._stan_konta = 10
    #     # print(o._stan_konta)
    #     # o+o2
    #     # print(o._stan_konta)
    o.praca = 'Tytu'
    print(o.praca)
