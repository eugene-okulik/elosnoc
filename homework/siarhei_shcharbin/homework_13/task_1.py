import os
import datetime


dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
homework_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(homework_file_path)

with open(homework_file_path, 'r', encoding='utf-8') as data_file:
    lines = data_file.readlines()
    line1 = lines[0].strip()
    line2 = lines[1].strip()
    line3 = lines[2].strip()
    old_date1 = datetime.datetime.strptime(line1[3:29], '%Y-%m-%d %H:%M:%S.%f')
    new_date1 = old_date1 + datetime.timedelta(weeks=1)
    old_date2 = datetime.datetime.strptime(line2[3:29], '%Y-%m-%d %H:%M:%S.%f')
    day_week = datetime.datetime.strftime(old_date2, '%A')
    old_date3 = datetime.datetime.strptime(line3[3:29], '%Y-%m-%d %H:%M:%S.%f')
    new_date3 = datetime.datetime.now() - old_date3
    print(new_date1)
    print(str(day_week) + ' is the day of the week on this date')
    print(str(new_date3.days) + ' days since the date')
