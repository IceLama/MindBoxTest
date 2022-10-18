# import random
import numpy as np


def first(n_customers):
    """В функции first создается список строк (data) из id клиентов, начиная с 00001 и до n_customers -- строки 13 - 15.
    Затем мы проходимся по этому списку, считаем номер группы для каждого id и записываем их в словарь, где ключ - это
    номер группы, а значение - количество id в этой группе -- строки 17 - 23"""
    data = []
    answer = {}
    id_len = 5

    for i in range(1, n_customers + 1):
        # id_len = random.choice([5, 6, 7])  # если раскомментировать, то в данных будут id разной длины
        data.append(str(i).zfill(id_len))

    for i in range(n_customers):
        group_num = sum(map(int, data[i]))
        if group_num not in answer:
            answer.update({group_num: 1})
        else:
            answer[group_num] += 1
    return answer

# print(first(n_customers=500))


# Во втором задании не понял одного момента. Как id может быть целым числом, если он может начинаться с 0?


def second(n_customers, n_first_id):
    """В функции second создается список строк (data) из id клиентов,
    начиная с n_first_id и до n_first_id + n_customers -- строки 36 - 37.
    Дальнейшие расчеты такие же, как в функции first."""
    answer = {}
    id_s = np.arange(n_first_id, n_first_id + n_customers)
    data = [str(i) for i in id_s]

    for i in range(n_customers):
        group_num = sum(map(int, data[i]))
        if group_num not in answer:
            answer.update({group_num: 1})
        else:
            answer[group_num] += 1
    return answer


# print(second(n_customers=100, n_first_id=99500))


# Это мой первоначальный вариант решения второй задачи, когда я подумал, что известная первая цифра id.
# Решил оставить
# def second2(n_customers, n_first_id):
#     data = []
#     answer = {}
#     id_len = 5
#
#     for i in range(1, n_customers + 1):  # создаем список id-строк с заранее указанной первой цифрой n_id
#         # id_len = random.choice([5, 7])  # если раскомментировать, то в данных будут id разной длины
#         zeros_between = id_len - (len(str(i)) + 1)
#         data.append(f"{n_first_id}{'0' * zeros_between}{i}")
#     print(data)
#
#     for i in range(n_customers):
#         group_num = sum(map(int, data[i]))  # считаем сумму всех цифр, т.е. находим номер группы
#         if group_num not in answer:  # если группы с таким номером в словаре нет,
#             answer.update({group_num: 1})  # то создаем такой ключ, и присваиваем значение 1
#         else:
#             answer[group_num] += 1  # если такая группа уже есть, то увеличиваем значение по этому ключу на 1
#     return answer  # результат - это словарь, где в качестве ключей номера групп, а в качестве значений количество id
#     # в этой группе
#
#
# print(second2(10, 5))
