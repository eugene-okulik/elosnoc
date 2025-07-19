import pymysql
import os
import dotenv


dotenv.load_dotenv()
db = pymysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
cursor = pymysql.cursors.DictCursor(db)
cursor.execute(f'''SELECT s.name, s.second_name, g.title, b.title, sub.title, l.title, m.value  
from students s JOIN books b on s.id = b.taken_by_student_id
JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on  m.lesson_id = l.id
JOIN subjets sub on l.subject_id = sub.id''')
data = cursor.fetchall()

dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'data.csv')
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
homework_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(homework_file_path)

with open(homework_file_path, 'r', encoding='utf-8') as data_file:
    lines = data_file.readlines()
lines = lines[1:]
for line in lines:
    csv_line = line.strip().split(',')
    match_found = False
    for element in data:
        values = list(element.values())
        if values == csv_line:
            match_found = True
            break
    if not match_found:
        print(f'There is no data matching {csv_line} in the database')

cursor.close()
db.close()
