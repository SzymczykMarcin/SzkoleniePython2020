# from random import choice
#
# b = 10
# c = choice([0, 2])
# try:
#     a = b / c
#     print(a)
#     choice(13)
# except ZeroDivisionError as e:
#     print('Nie dziel przez zero!')
#     print(e)
# except TypeError:
#     print('Zły typ danych!')
# finally:
#     b = 0
#
# print(b)

def func(a=0):
    if a > 0:
        return a
    else:
        raise ValueError
