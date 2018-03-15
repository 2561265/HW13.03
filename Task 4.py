#Реализовать программу, которая выводит содержимое каталога в файловой системе. Путь к каталогу запрашивается у пользователя.
import os
dir = os.listdir(input('Enter adress file: '))
for i in dir:
    print('List of files in your directiry: ', i)
