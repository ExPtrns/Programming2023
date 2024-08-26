import csv

from get_notes import get_notes_list


def save():
    with open("Notes.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";")
        for element in get_notes_list():
            file_writer.writerow(element)
    print("Заметки сохранены в файл.")


def load():
    get_notes_list().clear()
    try:
        with open("Notes.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            for row in file_reader:
                if len(row) > 1:
                    get_notes_list().append(row)
        for row in get_notes_list():
            row[0] = int(row[0])
        print("Данные загружены из файла.")
    except FileNotFoundError:
        print("Файл не найден.")
