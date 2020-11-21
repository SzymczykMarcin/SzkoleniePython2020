def moja_funkcja(x, y=1):
    if type(x) is int and type(y) is int:
        return x + y
    elif type(x) is str and type(y) is str:
        return f'{x} + {y}'


# x = 1
# print(type(x) is not int)

# moja_funkcja(1)
# moja_funkcja('Ula')
# moja_funkcja([1, 2, 3])

# print(moja_funkcja(2))
# print(moja_funkcja('Inne'))

print(moja_funkcja(2))

"""
Funkcja przyjmuje jakiś int, liczy aż do tej wartości.
Jeżeli liczba jest podzielna przez 3 to funkcja zwraca Fizz
Jeżeli liczba jest podzielna przez 5 to Buzz
Jeżeli przez obie to FizzBuzz
A w pozostałych wypadkach liczbę
"""