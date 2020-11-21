def moja_funkcja(x, y=1):
    if type(x) is int and type(y) is int:
        return x + y
    elif type(x) is str and type(y) is str:
        return f'{x} + {y}'


x = 1
print(type(x) is not int)

moja_funkcja(1)
moja_funkcja('Ula')
moja_funkcja([1, 2, 3])

print(moja_funkcja(2))
print(moja_funkcja('Inne'))

print(moja_funkcja(2))

"""
Funkcja przyjmuje jakiś int, liczy aż do tej wartości.
Jeżeli liczba jest podzielna przez 3 to funkcja zwraca Fizz
Jeżeli liczba jest podzielna przez 5 to Buzz
Jeżeli przez obie to FizzBuzz
A w pozostałych wypadkach liczbę
"""


def fizz_buzz(counter):
    for c in range(counter):
        licz_string = ''
        if c % 3 == 0:
            licz_string += 'Fizz'
        if c % 5 == 0:
            licz_string += 'Buzz'
        if not licz_string:
            licz_string = str(c)
        print(licz_string)


fizz_buzz(30)

def metoda_na_a(x):
    print('a')
    print(x)

def metoda_na_b(x):
    print('b')
    print(x)

def metoda_na_c(x):
    print('c')
    print(x)

swich_case = {'a': metoda_na_a,
              'b': metoda_na_b,
              'c': metoda_na_c,}

jakas_zmienna = 'b'
swich_case[jakas_zmienna](12)

def przyklad(x, y=10, **kwargs):
    z = 0
    if 'z' in kwargs:
        z = kwargs['z']
    return x+y+z


print(przyklad(x=1, y=2, z=3))

def przyklad_2(x, y=10, *args):
    result = x + y
    for a in args:
        result += a
    return result


print(przyklad_2(1, 2, 3, 4, 20, 10))

def przyklad_3(*args):
    res = 0
    for a in args:
        res +=a
    return res

print(przyklad_3(1,2,1,2,1,2))

def przyklad_4(x: int) -> (str, int):
    return str(x)


print(przyklad_4([1, 2, 2]))
