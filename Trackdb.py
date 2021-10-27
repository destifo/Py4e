import sqlite3 as sq
import xml.etree.ElementTree as ET

conn = sq.connect('Databases/drchucktrackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title TEXT UNIQUE
    );

    CREATE TABLE Genre(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE , 
        name TEXT UNIQUE
    );

    CREATE TABLE Track (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE, 
	album_id  INTEGER,
    genre_id INTEGER,
	len INTEGER, rating INTEGER  DEFAULT 'NO REVIEWS', count INTEGER DEFAULT 0
    );

''')

fname = input('Enter the file name: ')
if len(fname) < 1: fname = 'Library.xml'

def lookup(dict, key):
    found = False
    for child in dict:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

xmlfile = ET.parse(fname)
tracks = xmlfile.findall('dict/dict/dict')
print('Dict count:', len(tracks))

for track in tracks:
    if lookup(track, 'Track ID') is None: continue

    artist = lookup(track, 'Artist')
    title = lookup(track, 'Name') 
    album = lookup(track, 'Album')
    genre = lookup(track, 'Genre')
    rating = lookup(track, 'Rating')
    len = lookup(track, 'Total Time')
    count = lookup(track, 'Play Count')

    if artist is None or album is None or title is None or title is None :
        continue
    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)', (artist, ))
    cur.execute('SELECT id from Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album(artist_id, title) VALUES (?, ?)', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    try: genre_id = cur.fetchone()[0]
    except: genre_id = 'unknown'

    cur.execute('''INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ? , ? , ?, ?)''', (title, album_id, genre_id, len, rating, count))
    
    conn.commit()

def artist_track_viewer(name):
    cur.execute('''SELECT 
	Track.title, Artist.name 
	FROM Track JOIN Artist JOIN Album 
	ON Track.album_id = Album.id AND Album.artist_id = Artist.id
	AND Artist.name = ?''', (name, ))
    tracks = cur.fetchone()
    print("Total tracks found:", len(tracks))
    for track in tracks:
        print(track[1])
