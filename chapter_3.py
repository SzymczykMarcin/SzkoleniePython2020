class DzikiZierz:
    kończyny = ['Łapa', 'Łapa', 'Łapa', 'Łapa']

    def __init__(self, nowe_imie='Pimpek', *args, **kwargs):
        self.imie = nowe_imie
        self.pokarm = ['Trawa', 'Liście']
        self._gatunek = 'Ryś'

    def podaj_gatunek(self):
        print(self._gatunek)
        print(self.kolor_siersci)

    def _dodaj_pokarm(self, nowy_pokarm):
        self.pokarm.append(nowy_pokarm)

    def poznaj_nowy_pokarm(self, nazwa_pokarmu, czy_zatruty=False):
        if not czy_zatruty:
            self._dodaj_pokarm(nazwa_pokarmu)


kot = DzikiZierz('Fafik')
pies = DzikiZierz('Azor')


# kot.podaj_gatunek()
# kot._gatunek = 'Żubr'
# print(kot.kończyny)
# kot.kończyny[2] = 'Kopyto'
# print(kot.kończyny)
# print(kot.pokarm)
# kot.pokarm[0] = 'Myszy'
# print(kot.pokarm)
# print(pies.kończyny)

# print(kot.imie)
# print(pies.imie)
# print(kot._gatunek)
# kot.podaj_gatunek()

class Wielokat:

    def __init__(self, *args):
        self.ilosc_boków = len(args)
        self.obwod = 0
        for a in args:
            self.obwod += a

    def podaj_kolor(self):
        print('Czerwony')


class Kwadrat(Wielokat):
    def __init__(self, bok1):
        super().__init__(bok1, bok1, bok1, bok1)

    def podaj_kolor(self):
        print('Niebieski')


class Trojkat(Wielokat):
    def __init__(self, bok1, bok2, bok3):
        Wielokat.__init__(self, bok1, bok2, bok3)


w = Wielokat(4, 4, 4, 4, 5)
w.podaj_kolor()
print(f'Ilość boków {w.ilosc_boków} Obwód {w.obwod}')
k = Kwadrat(3)
print(f'Ilość boków {k.ilosc_boków} Obwód {k.obwod}')
k.podaj_kolor()
t = Trojkat(1, 2, 3)
print(f'Ilość boków {t.ilosc_boków} Obwód {t.obwod}')
t.podaj_kolor()
