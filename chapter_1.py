from copy import copy

zmienna = 'Hello World!'
zmienna_1 = 1
zmienna_314 = 3.14
moja_lista = []
moj_slownik = {}
moja_tupla = ()

zmienna_1 += 1
zmienna_314 = zmienna_314 % 3

nowy_string = 'Marcin Szymczyk Marcin'
nowy_string = nowy_string.replace(' ', '_')
nowa_lista = nowy_string.split('_')
nowy_string = '&'.join(nowa_lista)

imie = 'Marcin'
nazwisko = 'Szymczyk'
data = 2020
jeszcze_nowszy_string = 'Imie {} Nazwisko {} Data {}'.format(imie, nazwisko, data)
jeszcze_nowszy_string_2 = f'Imie {imie} Nazwisko {nazwisko} Data {data}'

if imie == 'Marcin':
    print(imie
          + nazwisko)
    print(imie)
    my_list = [1,
               2,
               3,]
elif imie == 'Michal':
    print(imie)
    kolejny_string = 'Ala' \
                     'ma' \
                     'kota'
else:
    print(imie)

while zmienna_1 == 1:
    zmienna_1 += 1

lista_3 = [2, 15.6, 3, 12, 18, 7]
lista_x = copy(lista_3)
print(lista_3)
print(lista_x)
lista_x.append(100)
print(lista_3)
print(lista_x)
for x in range(20):
    lista_3.append(x)

print(lista_3)
lista_3.extend(['A', 'B', 'C'])
print(lista_3)
# lista_3.sort()
# print(sorted(lista_3))
a = lista_3.pop(2)
print(lista_3)
print(lista_3[2:])
print(lista_3[-1])
print(lista_3[2:4])
print(lista_3[-4:])
print([1, 2, ] + [3, 4])
for x in lista_3:
    print(x)

for x in 'Ala ma kota':
    print(x)

for index, element in enumerate(lista_3):
    print(index)
    print(type(element))
"""
ctrl + /
ctrl + alt + l
"""
'''
ctrl + alt + o

'''

nowy_slownik = {'Anna': {'Praca': 'Programista', 'Wiek': 29},
                'Tomek': {'Praca': 'Tester', 'Wiek': 26},
                'Patryk': {'Praca': 'Kierowca', 'Wiek': 41}}


for x in nowy_slownik:
    nowy_slownik['Tomek'] = {'Praca': 'Tester Automatyk', 'Wiek': 30}
    nowy_slownik['Patryk']['Wiek'] = 50
    print(nowy_slownik)
    print(f'Imie {x} Praca {nowy_slownik[x]["Praca"]} Wiek {nowy_slownik[x]["Wiek"]}')


nowy_slownik.update({'Zofia': {'Praca': 'Student', 'Wiek': 21}})
print(nowy_slownik)



