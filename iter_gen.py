from random import randint

# def my_gen_1():
#     n = 1
#     print('Po raz pierwszy!')
#     yield n
#     print('Po raz drugi!')
#     n += 1
#     yield n
#     print('Po raz trzeci!')
#     n += 1
#     yield n
# item = my_gen_1()
# print(next(item))
# print(next(item))
# print(next(item))
# print(next(item))
# for item in my_gen_1():
#     print(item)

my_list = []
for x in range(0, 10):
    my_list.append([])
    for y in range(0, 10):
        my_list[x].append(randint(0, 100))

print(my_list)

my_list_2 = [[randint(0, 100) for x in range(0, 10)] for y in range(0, 10)]

print(my_list_2)

print(len(my_list), len(my_list_2))