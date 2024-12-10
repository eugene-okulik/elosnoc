# Values for input are:
# 'результат операции: 42'
# 'результат операции: 514'
# 'результат работы программы: 9'


a = input()
a_num_pos = int(a.index(':')) + 2
print(int(a[a_num_pos:]) + 10)
