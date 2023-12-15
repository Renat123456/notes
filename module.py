import datetime
import os

pathFile = 'notes.csv'

# Новая заметка
def addNote():
    print("Введите заголовок заметки")
    newNoteTitle = input()
    print("Введите заметку")
    newNote = input()
    nowTime = datetime.datetime.now()
    nowTime = nowTime.strftime("%Y-%m-%d")

    if os.path.isfile(pathFile):
        lines = sum(1 for line in open(pathFile))
        if lines != 0:
            with open(pathFile, 'r', encoding='utf-8') as data:
                last_line = data.readlines()[-1]
                last_line = last_line.split(';')
                id =  str(int(last_line[0]) + 1)
        else:
            id = '1'
    else:
        id = '1'

    with open(pathFile, '+a', encoding='utf-8') as data:
        data.writelines(id + ';' + nowTime + ';' + newNoteTitle + ';' + newNote + "\n")
        print('Заметка добавлена') 

# Чтение заметок
def readNotes():
    if os.path.isfile(pathFile):
        lines = sum(1 for line in open(pathFile))
        if lines != 0:
            data = open(pathFile, 'r', encoding='utf-8')
            for line in data:
                note = line.split(';')
                print(*note[:-1])
                print(*note[-1:])
            data.close()
        else:
            print('Заметок нет')
    else:
        print('Заметок нет')

# Редактирование заметок
def updateNote():
    print("Введите номер заметки для редактирования")
    idNote = input()
    print("Введите заголовок заметки")
    upNoteTitle = input()
    print("Введите заметку")
    upNote = input()
    nowTime = datetime.datetime.now()
    nowTime = nowTime.strftime("%Y-%m-%d")

    if os.path.isfile(pathFile):
        lines = sum(1 for line in open(pathFile))
        if lines != 0:
            oldData = ''
            data = open(pathFile, 'r', encoding='utf-8')
            for line in data:
                oldDataSplit = line.split(';')
                if idNote == oldDataSplit[0]:
                    oldData = line
            data.close()
            if oldData != '':
                newData = idNote + ';' + nowTime + ';' + upNoteTitle + ';' + upNote + "\n"
                with open (pathFile, 'r', encoding='utf-8') as data:
                    old_data = data.read()
                    new_data = old_data.replace(oldData, newData)
                with open (pathFile, 'w', encoding='utf-8') as f:
                    f.write(new_data)
                    print('Заметка изменена') 
            else:
                print('Такой заметки нет')         
        else:
            print('Заметок нет')
    else:
        print('Заметок нет')

# Удаление заметок
def delNote():
    print("Введите номер заметки для удаления")
    idNote = input()

    if os.path.isfile(pathFile):
        lines = sum(1 for line in open(pathFile))
        if lines != 0:
            oldData = ''
            data = open(pathFile, 'r', encoding='utf-8')
            for line in data:
                oldDataSplit = line.split(';')
                if idNote == oldDataSplit[0]:
                    oldData = line
            data.close()
            if oldData != '':
                newData = ''
                with open (pathFile, 'r', encoding='utf-8') as data:
                    old_data = data.read()
                    new_data = old_data.replace(oldData, newData)
                with open (pathFile, 'w', encoding='utf-8') as f:
                    f.write(new_data)
                    print('Заметка удалена') 
            else:
                print('Такой заметки нет') 
        else:
            print('Заметок нет')
    else:
        print('Заметок нет')