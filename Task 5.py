#Реализовать программу, позволяющую осуществлять управление файлами: копирование, создание, удаление, переименование.
#Необходимо предусмотреть возможность смен директории. Изначально используется текущий каталог запуска скрипта программы.
import os
import shutil
patch = os.getcwd()
print('Your directory is ', patch)

def change_directory():
    patch = os.getcwd()
    while True:
        question = input("Do you want change your directory? \n (enter 'y' if Yes or 'n' if No): ")
        if question == 'n':
            print('Your current directory is ', patch)
            break
        elif question == 'y':
            patch = os.listdir(input('Enter new directory - '))
            for i in patch:
                print(i)
        else:
            break


def copy():
    while True:
        question = input("Do you want copy file? \n (enter 'y' if Yes or 'n' if No): ")
        if question == 'n':
            break
        elif question == 'y':
            file = input('Enter file name for copy - ')
            dir = input('Enter directory for new copy - ')
            copys = shutil.copy(file, dir)
            patch = os.listdir(dir)
            print('\nCopy is done! \n\t Directory tree:')
            for i in patch:
                print('\t', i)
        else:
            break

def create():
    while True:
        question = input("Do you want creat file? \n (enter 'y' if Yes or 'n' if No): ")
        if question == 'n':
            break
        elif question == 'y':
            file = input('Enter file for create: ')
            f = open(file, 'tw', encoding='utf-8')
            f.close()
            patch = os.listdir()
            print('File creat! \nDirectory tree:')
            for i in patch:
                print('\t',i)
        else:
            break

def delete():
    while True:
        question = input("Do you want delete file? \n (enter 'y' if Yes or 'n' if No): ")
        if question == 'n':
            break
        elif question == 'y':
            file = input('Enter file what you want delete: ')
            f = os.remove(file)
            patch = os.listdir()
            print('File deleted! \nDirectory tree:')
            for i in patch:
                print('\t',i)
        else:
            break

def rename():
    while True:
        question = input("Do you want rename file? \n (enter 'y' if Yes or 'n' if No): ")
        if question == 'n':
            break
        elif question == 'y':
            file = input('Enter file what you want rename: ')
            new_name = input('Enter new file name: ')
            f = os.renames(file, new_name)
            patch = os.listdir()
            print('File rename! \nDirectory tree:')
            for i in patch:
                print('\t',i)
        else:
            break


while True:
    answer = input("Do you whant work with directory? \n(enter 'y' if Yes or 'n' if No): ")
    if answer == 'n':
        print('You chose NO. Have a nice day!')
        break
    elif answer == 'y':
        change_directory()
        copy()
        create()
        delete()
        rename()
    else:
        print('You enter something wrong! \nThe Program end.')
        break
