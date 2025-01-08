temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24,
    23
]


# def add_value(x):
#     i = -1
#     if x > 28:
#         i -= 1
#         return x
#     else:
#         temperatures.pop(i)
#
#
# hot_days = map(add_value, reversed(temperatures))
# print(list(hot_days))
#
# ничего не вышло с map
# вверху один из промежуточных вариантов, к которым я приходил, но он не отрабатывает корректно


# def is_hot(x):
#     if x > 28:
#         return True


# def is_hot(x):
#     return x > 28
#
#
# hot_days = filter(is_hot, temperatures)
# print(list(hot_days))


# hot_days = filter(lambda x: x > 28, temperatures)
# print((list(hot_days)))
#
# закомментил другие валидные варианты решения задачи


hot_days = filter(lambda x: x if x > 28 else None, temperatures)
hot_days = list(hot_days)  # преобразую в постоянный список, так как не работают функции min/max/mean вместе с list
print(hot_days)
a = max(hot_days)
b = min(hot_days)
c = sum(hot_days) / len(hot_days)
print(a, b, c)
