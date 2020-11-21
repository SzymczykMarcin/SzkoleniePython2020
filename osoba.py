imie = ''
nazwisko = ''
wiek = 0
praca = ''
global _stan_konta
_stan_konta = 0
hobby = ['literatura', 'film', 'szachy']


def wyplata(kwota):
    _stan_konta += kwota


def zakupy(kwota):
    _stan_konta -= kwota