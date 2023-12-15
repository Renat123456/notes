import module as m

# Меню
flag = True
while flag:
    print("Введите 1 чтобы добавить заметку")
    print("Введите 2 чтобы прочитать заметки")
    print("Введите 3 чтобы редактировать заметку")
    print("Введите 4 чтобы удалить заметку")
    print("Введите 5 чтобы выйти из программы")
    command = input()
    if command == '1':
        m.addNote()
    elif command == '2':
        m.readNotes()
    elif command == '3':
        m.updateNote()
    elif command == '4':
        m.delNote()
    elif command == '5':
        flag = False
    else:
        print("Некорректная команда")
