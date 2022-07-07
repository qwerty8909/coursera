#!/usr/bin/env python3

# указываем что будем тестировать
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self): # базовый тест
        # вводим тестовые случаи ввода и ожидаемого вывода
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        # убеждаемся соответствии ожудаемого результата
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self): # тест с пустым параметром будет с ошибкой
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)
        # поэтому вносим изменения в основной файл

    def test_double_name(self): # проверка двойного имени
        testcase = 'Hopper, Grace M.'
        expected = 'Grase M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self): # проверка одного имени выдаст ошибку
        testcase = 'Voltaire'
        expected = 'Voltaire'
        self.assertEqual(rearrange_name(testcase), expected)
        # опять вносим изменения в файл

unittest.main()