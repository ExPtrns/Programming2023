import datetime

from get_notes import add_notes_to_list


def add_new_note(notes_list):
    note_id = notes_list[0] + 1
    note_title = notes_list[1]
    note_body = notes_list[2]
    create_date = datetime.datetime.now()
    new_note = [note_id, note_title, note_body, format_date(create_date)]
    add_notes_to_list(new_note)


def format_date(date_for_convert):
    if date_for_convert.month < 10:
        return (
            f"{date_for_convert.day}/0{date_for_convert.month}/{date_for_convert.year}, {date_for_convert.hour}:"
            f"{date_for_convert.minute}:{date_for_convert.second}")
    else:
        return (
            f"{date_for_convert.day}/{date_for_convert.month}/{date_for_convert.year}, {date_for_convert.hour}:"
            f"{date_for_convert.minute}:{date_for_convert.second}")
