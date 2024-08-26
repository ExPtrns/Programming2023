notes_list = list()


def get_notes_list():
    return notes_list


def add_notes_to_list(new_note):
    notes_list.append(new_note)


def printlist():
    for elements in notes_list:
        print(f"{elements[0]}. \tНазвание - {elements[1]}\n\t{elements[2]}\n\tСоздано/изменено - {elements[3]}")
