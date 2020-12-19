my_list_1 = [1, 2, 3, 4]
# print(my_list_1)
# print(my_list_1[1])
# my_list_1[1] = 8
# print(my_list_1[1])
# print(my_list_1)

# my_touple_1 = (1, 2, 3, 4)
# print(my_touple_1)
# print(my_touple_1[1])
# my_touple_1[1] = 8
# print(my_touple_1[1])
# print(my_touple_1)

# my_list = [1, '2', 3.3, [3, 2, 1]]
#
# # print(my_list)
#
# for x in my_list:
#     print(x)

# my_list_1.append(16)
# print(my_list_1)
#
# my_list_1.extend([13,14,15])
# print(my_list_1)
#
# print(13 in my_list_1)

my_dict = {'Imie': 'Marcin', 'Wiek': 32}


# print(my_dict)

# for x in my_dict:
#     print(x)
#
# for k in my_dict:
#     print(my_dict[k])

# my_dict.update({'Nazwisko': 'Szymczyk'})
# print(my_dict.keys())
# my_dict.keys()
# for x in range(2):
#     if 'Zawód' not in my_dict.keys():
#         my_dict.update({'Zawód': ['Tester']})
#     else:
#         my_dict['Zawód'].append('Trener')
#
# print(my_dict)

def func_1():
    print(1)


def func_2():
    print(2)


def func_3():
    print(3)


swich_dict = {1: func_1, 2: func_2, 3: func_3}

swich_dict[2]()
