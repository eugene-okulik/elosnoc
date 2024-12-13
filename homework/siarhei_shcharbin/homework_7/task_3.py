# Values for input are:
# 'результат операции: 42'
# 'результат операции: 54'
# 'результат работы программы: 209'
# 'результат: 2'


def sum_10(result):
    result_num_pos = int(result.index(':')) + 2
    print(int(result[result_num_pos:]) + 10)


a = input()
sum_10(a)

