import json
import sqlite3 as sq

conn = sq.connect('databases/course_rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE
    );

    CREATE TABLE Member(
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        role INTEGER NOT NULL,
        PRIMARY KEY(user_id, course_id)
    );
''')

fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'roster_data.json'
data = open(fname).read()
jsfile = json.loads(data)

for entry in jsfile:
    username = entry[0]
    course = entry[1]
    role = entry[2]
    

    cur.execute('INSERT OR IGNORE INTO User(name) VALUES (?)', (username, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (username, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (course, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course, ))
    course_id = cur.fetchone()[0]

    print(user_id, course_id, role)
    cur.execute('''INSERT OR REPLACE INTO Member(user_id, course_id, role) 
    VALUES (?, ?, ?)''', (user_id, course_id, role))
    conn.commit()