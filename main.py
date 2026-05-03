import sqlite3
from random import choice

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXIST students (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,        
                 name TEXT,
                 age INTEGER,
                 major TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXIST courses (
                 course.id INTEGER PRIMARY KEY AUTOINCREMENT,        
                 course_name TEXT,
                 instructor TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXIST students_courses (
                 student_id INTEGER,        
                 course_id INTEGER,
                 FOREIGN KEY (student_id) REFERENCES students(id),
                 FOREIGN KEY (course_id) REFERENCES courses(course_id),
                 PRIMARY KEY (students_id, course_id)
                 ''')

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Заруєструвати студентів на курс")
    print("6. Показати студнтів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7:")

    if choice == "1":
        name = input("Введіть ім'я студента")
        age = input("Введіть вік студента")
        major = input("Введіть спуціальність студента")

        cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)")

        conn.commit()

    if choice == "2":
        course_name = input("Введіть назву курсу")
        instructor = input("Введіть викладача курсу")

        cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)",
                       (course_name, instructor))
        conn.commit()

    if choice == "3":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if not students:
            print("У базі немає жодного студента")
        else:
            print("\nСисок студентів")
            for student in students:
                print(f"ID: {student[0]}, Ім'я:")
