import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, publish_year int, pages_count int, created_at TEXT)''')
conn.commit()
conn.close()


def db_work(db_str):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(db_str)
    answer = cursor.fetchall()
    conn.commit()
    conn.close()
    return (answer)
