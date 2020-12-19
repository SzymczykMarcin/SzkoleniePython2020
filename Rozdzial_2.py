import string

import random

my_tup = [1, 2, 3, 4]
print(random.randint(0, 100))
print(random.choice(my_tup))

# def func_func(imie, zwierze):
#     print('{} ma {}.'.format(imie, zwierze))
#
#
# func_func('Ala', 'kota')


# def next_func(imie='Ala', zwierze='kota'):
#     print('{} ma {}.'.format(imie, zwierze))
#
# next_func()
# next_func('Adam', 'psa')

# def adding(var_one, var_two):
#     return var_one + var_two
#
#
# result = adding(1, 1)
# print(result)
# print(adding('Adam', 'psa'))


my_list = ['Marcin', 'Jakub', 'Taras', 'Michal']


# def cwiczenie(name_list=None):
# #     if name_list is not None:
# #         for name in name_list:
# #             print(f'Witaj serdecznie {name}. Miło, że jesteś na szkoleniu.')
# #     else:
# #         name = input('Jak masz na imie nieznajoma osobo?: ')
# #         if name.endswith('a'):
# #             print('Witaj serdecznie {}. Miło, że do nas dołączyłaś'.format(name.capitalize()))
# #         else:
# #             print('Witaj serdecznie {}. Miło, że do nas dołączyłeś'.format(name.capitalize()))
# #
# #
# # cwiczenie(my_list)

def func(a=2, **kwargs):  # lub *args
    if 'argument_1' in kwargs:
        print(kwargs['argument_1'])


func(a=13, argument_2='b')
