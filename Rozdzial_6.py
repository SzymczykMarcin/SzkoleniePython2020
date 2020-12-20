import os


# for content in os.listdir('C:\projects\SzkoleniePython2020'):
#     if content.endswith('.txt'):
#         file_to_open = content
#
# #Po nowemu
# with open(file_to_open, 'w') as some_file:
#     content = some_file.write('To jest szkolenie z Pythona!!!')
#
# with open(file_to_open, 'r') as some_file:
#     content = some_file.read()
#
# print(content)
#
# #Po staremu
# some_file = open('test.txt', 'r')
# content = some_file.read()
# some_file.close()

# for root, dirs, files in os.walk('C:\projects\SzkoleniePython2020'):
#     print(f'Those are directories {dirs}')
#     print(f'Those are files {files}')
#     print(f'#####################')


# for root, dirs, files in os.walk('C:\projects\SzkoleniePython2020'):
#     for f in files:
#         if f.endswith('.pyc'):
#             path_to_file = os.path.join(root,f)
#             print(path_to_file)

if os.path.isfile('C:\projects\SzkoleniePython2020\other.txt'):
    with open('other.txt', 'r') as some_file:
         content = some_file.read()
else:
    print('Sorry, nie ma pliku!')

if os.path.isdir(r'C:\projects\SzkoleniePython2020\test'):
    print('Folder istnieje')
else:
    print('Folder nie istnieje')
    os.mkdir(r'C:\projects\SzkoleniePython2020\test')

