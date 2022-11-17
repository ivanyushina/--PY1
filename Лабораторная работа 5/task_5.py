import random  # импортируем инструмент для получения случайного значения


def get_unique_list_numbers() -> list[int]:
    '''
    This is a function that returns a list of 15 elements filled
    with random and unique integers from -10 to 10
    :return:
    list
    '''

    list_ = list()  # создаем рабочий список
    while len(set(list_)) < 15:  # задаем условие для списка: состоит из 15 уникальных элементов
        list_.append(random.randint(-10, 10))  # заполняем список случайными значениями
    return list(set(list_))  # возвращаем список, состоящий из уникальных случайных значений
