import sqlite3 as sq
import re

conn = sq.connect('databases/orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname = input("Provide the file name: ")
if len(fname) < 1: fname = 'mbox.txt'
try:
    fh = open(fname)
except:
    print('The file was not found')

for line in fh:
    if not line.startswith('From: '): continue
    piece1 = line.split()
    email = piece1[1]
    piece2 = email.split('@')
    #piece3 = piece2[1].split('.')
    org = piece2[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

cur.execute('SELECT * FROM Counts ORDER BY count DESC')
conn.commit()
cur.close()
