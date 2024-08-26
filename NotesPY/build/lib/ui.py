import datetime

from add_note import add_new_note, format_date
from delete_notes import delete_choise_note
from get_notes import get_notes_list, printlist
from save_N_load_notes import save, load


def menu_exit():
    print("Завершение работы программы.")
    return False


def read_notes():
    if not get_notes_list():
        print("\nСписок пуст\n")
    else:
        printlist()


def add_note():
    temp = list()
    temp.append(len(get_notes_list()))
    temp.append(input("Введите название заметки: "))
    lines = []
    print("Добавьте содержание заметки (многострочный ввод)")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n\t'.join(lines)
    temp.append(text)
    add_new_note(temp)
    print("Заметка успешно добавлена!\n")


def make_change(command):
    temp = get_notes_list()[command - 1]
    lines = []
    print("Введите новое содержание для заметки (многострочный ввод - окончание ввода пустая строка)")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n\t'.join(lines)
    temp[2] = text
    temp[3] = format_date(datetime.datetime.now())
    get_notes_list()[command - 1] = temp
    print("Заметка отредактирована.\n")


def change_note():
    read_notes()
    try:
        command = int(input("Укажите номер заметки, которую хотите изменить: "))
        if command < 1 or command > len(get_notes_list()):
            print("Заметка не найдена.")
            raise ValueError
        else:
            make_change(command)
    except ValueError:
        print("Нужно указать номер заметки из списка.\n")


def delete_note():
    read_notes()
    try:
        command = int(input("Укажите номер заметки, которую хотите удалить: "))
        if command < 1 or command > len(get_notes_list()):
            print("Заметка не найдена.")
            raise ValueError
        else:
            delete_choise_note(command)
            print("Заметка удалена.\n")
    except ValueError:
        print("Нужно указать номер заметки из списка.\n")


def save_notes():
    save()

def load_notes():
    load()

def main_menu():
    flag = True
    while flag:
        try:
            command = int(input("Укажите номер действия:\n"
                                "1. Добавить заметку.\n"
                                "2. Посмотреть заметки.\n"
                                "3. Изменить заметку.\n"
                                "4. Удалить заметку.\n"
                                "5. Сохранить заметки в файл.\n"
                                "6. Загрузить файл с заметками.\n"
                                "7. Выход.\n"))
            if command == 1:
                add_note()
            elif command == 2:
                read_notes()
            elif command == 3:
                change_note()
            elif command == 4:
                delete_note()
            elif command == 5:
                save_notes()
            elif command == 6:
                load_notes()
            elif command == 7:
                flag = menu_exit()
            else:
                raise ValueError
        except ValueError:
            print("Такой команды не существует! Повторите ввод.")
