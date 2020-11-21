import os

# for root, dirs, files in os.walk('C:\projects\SzkoleniePython2020'):
#     print(root, dirs, files)
#
# print(os.path.isfile('C:\projects\SzkoleniePython2020\chapter_1.py'))
# print(os.path.isdir('C:\projects\SzkoleniePython2020'))
# print(os.path.exists(r'C:\projects\SzkoleniePython2020\new_test'))
# print(os.path.join('C:\projects', 'SzkoleniePython2020'))
# os.mkdir(r'C:\projects\SzkoleniePython2020\new_test')
# print(os.path.exists(r'C:\projects\SzkoleniePython2020\new_test'))
#
# with open(r'C:\projects\SzkoleniePython2020\testowy\text.txt', 'w') as nasz_plik:
#     nasz_plik.write('To jest testowy plik!')
#
# with open(r'C:\projects\SzkoleniePython2020\testowy\text.txt', 'r') as nasz_plik:
#     c = nasz_plik.read()
#     print(c)
#
# nasz_plik = open(r'C:\projects\SzkoleniePython2020\testowy\text.txt', 'w')
# ...
# nasz_plik.close()
# for root, dirs, files in os.walk('C:\projects\SzkoleniePython2020'):
#     for f in files:
#         if f.endswith('.csv'):
#             print(os.path.join(root, f))

# print(os.path.abspath(__file__))