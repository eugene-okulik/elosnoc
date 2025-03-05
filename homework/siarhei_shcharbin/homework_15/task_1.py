import pymysql

db = pymysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = pymysql.cursors.DictCursor(db)
name = 'Siarhei'
second_name = 'Shcharbin'
book1 = 'Beighley MySQL'
book2 = 'SQL for dummies'
group_title = 'Slow learners'
group_start = 'Oct-2024'
group_end = 'Mar-2025'
subject1 = 'Math for Programmers'
subject2 = 'Programming for Dummies'
subject3 = 'Python for QAs'
mark1 = 3
mark2 = 4
mark3 = 5
mark4 = 2
mark5 = 5
mark6 = 5

cursor.execute(f"INSERT INTO students (name, second_name) VALUES ('{name}', '{second_name}')")
student_id = cursor.lastrowid
print(f"Id of the student is {student_id}")
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books_query, [
        (book1, student_id),
        (book2, student_id)
    ]
)
cursor.execute(f"SELECT title FROM books where taken_by_student_id = '{student_id}'")
cursor.execute(f"INSERT INTO `st-onl`.groups (title, start_date, end_date) "
               f"VALUES ('{group_title}', '{group_start}', '{group_end}')")
group_id = cursor.lastrowid
print(f"Group id is {group_id}")
cursor.execute(f"SELECT * FROM `st-onl`.groups WHERE id = '{group_id}'")
cursor.execute(f"UPDATE students SET group_id = '{group_id}' where id = '{student_id}'")
cursor.execute(f"INSERT INTO subjets (title) VALUES ('{subject1}')")
subject1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO subjets (title) VALUES ('{subject2}')")
subject2_id = cursor.lastrowid
cursor.execute(f"INSERT INTO subjets (title) VALUES ('{subject3}')")
subject3_id = cursor.lastrowid
print(f"Subjects ids are: {subject1_id}, {subject2_id}, {subject3_id}")
insert_lessons_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_lessons_query, [
        (subject1, subject1_id),
        (subject1, subject1_id),
        (subject2, subject2_id),
        (subject2, subject2_id),
        (subject3, subject3_id),
        (subject3, subject3_id)
    ]
)
cursor.execute(f"SELECT id from lessons WHERE subject_id = '{subject1_id}'")
data1 = cursor.fetchall()
cursor.execute(f"SELECT id from lessons WHERE subject_id = '{subject2_id}'")
data2 = cursor.fetchall()
cursor.execute(f"SELECT id from lessons WHERE subject_id = '{subject3_id}'")
data3 = cursor.fetchall()


def get_lessons_ids(data_ids):
    lesson_ids = [lesson['id'] for lesson in data_ids]
    id1, id2 = lesson_ids[0], lesson_ids[1]
    return id1, id2


lesson1_id, lesson2_id = get_lessons_ids(data1)
lesson3_id, lesson4_id = get_lessons_ids(data2)
lesson5_id, lesson6_id = get_lessons_ids(data3)
print(f"Lessons ids are: {lesson1_id}, {lesson2_id}, {lesson3_id}, {lesson4_id}, {lesson5_id}, {lesson6_id}")
insert_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks_query, [
        (mark1, lesson1_id, student_id),
        (mark2, lesson2_id, student_id),
        (mark3, lesson3_id, student_id),
        (mark4, lesson4_id, student_id),
        (mark5, lesson5_id, student_id),
        (mark6, lesson6_id, student_id)
    ]
)
cursor.execute(f"SELECT `value` from marks WHERE student_id = '{student_id}'")
all_marks = cursor.fetchall()
print(f"All marks for the student are: {all_marks}")
cursor.execute(f"SELECT title from books WHERE taken_by_student_id = '{student_id}'")
all_books = cursor.fetchall()
print(f"All books assigned to the student are: {all_books}")
cursor.execute(f'''SELECT s.name, s.second_name, b.title, g.title, m.value, l.title, sub.title
from students s JOIN books b on s.id = b.taken_by_student_id
JOIN `groups` g on s.group_id = g.id
JOIN marks m on s.id = m.student_id
JOIN lessons l on  m.lesson_id = l.id
JOIN subjets sub on l.subject_id = sub.id WHERE s.id = {student_id}''')
everything = cursor.fetchall()
print(f"All information related to the student is: {everything}")

db.commit()
cursor.close()
db.close()
