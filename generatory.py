from random import randint
# import itertools as it
#
# num_iterations = int(input('How many? '))
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         b = a+b
#         yield b
#         a = a+b
#
# for x in it.islice(fib(), num_iterations):
#     print(x)
#     answ = input('Continue? ')
#     if answ == 'N':
#         break

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

# print(list(range(10)))

a = [[randint(3, 15) for x in range(100)] for x in range(100)]
# for _ in range(100):
#     a.append(randint(3, 15))
for i in a:
    print(i)