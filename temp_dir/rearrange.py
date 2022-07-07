#!/usr/bin/env python3

import re

# меняет местами имя и фамилию
def rearrange_name(name):
    result = re.search(r"^([\w.]*), ([\w.]*)$", name)
    if result is None: # это добавили после теста с пустым параметром чтоб убрать ошибку
        # return "" - заменили после теста с одним именем на
        return name
    return "{} {}".format(result[2], result[1])

