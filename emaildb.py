import sqlite3 as sq

conn = sq.connect('databases/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = input("Enter the file name: ")
if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    line = line.split()
    email = line[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(email, count) VALUES (?, 1)', (email, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()

sqlcommand = "SELECT * FROM Counts ORDER BY count DESC LIMIT 10"

print("The top 10 sender's email accounts are: ")
for tuple in cur.execute(sqlcommand):
    print(tuple[0], tuple[1])

cur.close()
