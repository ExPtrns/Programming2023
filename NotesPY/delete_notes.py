from get_notes import get_notes_list


def delete_choise_note(choise):
    get_notes_list().pop(choise - 1)
    counter = 1
    for element in get_notes_list():
        element[0] = counter
        counter += 1


def delete_all_notes():
    get_notes_list().clear()
