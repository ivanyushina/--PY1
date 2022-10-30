def get_count_char(str_):
    dict_ = {}
    for a in str_.lower():
        if a.isalpha():
            if a in dict_:
                dict_[a] += 1
            else:
                dict_[a] = 1
    dolya(dict_, str_)
    return dict_


def dolya(dict_, str_):
    dict2 = {}
    for k, v in dict_.items():
        dict2[v] = round(v / len(str_) * 100, 2)

        # print(k, "-", v, end='%  ')
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
