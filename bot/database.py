import sqlite3

def init_db():
    connection = sqlite3.connect("school_data.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()

def save_student(name, age, grade):
    connection = sqlite3.connect("school_data.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
    """, (name, age, grade))

    connection.commit()
    connection.close()
