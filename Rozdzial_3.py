class MojaClasa:

    def __init__(self, opis, opis2=''):
        inicjalizacyjna_wartosc = 1
        self.zmienna_1 = inicjalizacyjna_wartosc
        self.opis = opis
        self._dodatkowy_opis = opis2

    def moja_metoda(self):
        self.zmienna_1 += self.inna_metoda()

    @staticmethod #To jest dekorator
    def inna_metoda():
        return 1

    def __str__(self):
        return self.opis + ' ' + self._dodatkowy_opis

    def __add__(self, other):
        return self.zmienna_1 + other.zmienna_1


x = MojaClasa('To jest moja klasa!!!', 'Nic')
y = MojaClasa('To jest inna klasa!!!', 'Cos')
# x.opis = ''
# print(x.opis)
# x._dodatkowy_opis = ''
# print(x._dodatkowy_opis)
# print(x.__dict__)
#
# x.nazwa = 'Adam'
# print(x.nazwa)
# print(x.__dict__)

# print(y.__dict__)
# print(isinstance(x, MojaClasa))

# print(x.zmienna_1)
# x.moja_metoda()
# print(x.zmienna_1)
# print(y.zmienna_1)
# print(x+y)
# a = x+y
# print(x.zmienna_1)
#
# skrot = x.moja_metoda
#
# print(x.zmienna_1)
# skrot()
# print(x.zmienna_1)
print(x)

