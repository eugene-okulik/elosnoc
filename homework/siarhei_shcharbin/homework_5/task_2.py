a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
a_num_pos = a.index('42')
print(int(a[a_num_pos:]) + 10)
b_num_pos = b.index('514')
print(int(b[b_num_pos:]) + 10)
c_num_pos = c.index('9')
print(int(c[c_num_pos:]) + 10)
