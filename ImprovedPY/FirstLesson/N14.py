# """Задание №1 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре."""
#
# import doctest
#
#
# def del_less(text):
#     """
#     Удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
#     >>> del_less('one two')
#     'one two'
#     >>> del_less('One Two')
#     'one two'
#     >>> del_less('one, two')
#     'one two'
#     >>> del_less('one two три')
#     'one two '
#     >>> del_less('one two три, FOUR%')
#     'one two  four'
#     """
#     new_text = ''
#     for letter in text:
#         if ord(letter) in range(97, 122) or ord(letter) in range(65, 91) or letter == ' ':
#             new_text += letter
#     return new_text.lower()
#
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)

# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
#
# import unittest
#
# import string
#
#
# class TestCaseName(unittest.TestCase):
#     def test_no_change(self):
#         self.assertEqual('one two', remove_symbols('one two'))
#
#     def test_lower(self):
#         self.assertEqual('one two', remove_symbols('One Two'))
#
#     def test_punctuation(self):
#         self.assertEqual('one two', remove_symbols('one, two'))
#
#     def test_languages(self):
#         self.assertEqual('one two ', remove_symbols('one two три'))
#
#     def test_all(self):
#         self.assertEqual('one two  four', remove_symbols('one two три, FOUR%'))
#
#
# def remove_symbols(text: str) -> str:
#     """
#     Удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
#     >>> remove_symbols('one two')
#     'one two'
#     >>> remove_symbols('One Two')
#     'one two'
#     >>> remove_symbols('one, two')
#     'one two'
#     >>> remove_symbols('one two три')
#     'one two '
#     >>> remove_symbols('one two три, FOUR%')
#     'one two  four'
#     """
#
#     return ''.join(letter for letter in text if letter in string.ascii_letters + " ").lower()
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import string
import pytest


def remove_symbols(text: str) -> str:
    return ''.join(letter for letter in text if letter in string.ascii_letters + " ").lower()


def test_no_change():
    assert 'one two' == remove_symbols('one two')


def test_lower():
    assert 'one two' == remove_symbols('One Two')


def test_punctuation():
    assert 'one two' == remove_symbols('one, two')


def test_languages():
    assert 'one two ' == remove_symbols('one two три')


def test_all():
    assert 'one two  four' == remove_symbols('one two три, FOUR%')


if __name__ == '__main__':
    pytest.main(['-vv'])
