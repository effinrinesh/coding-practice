#Question statement
'''Using Databases with Python


To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
No file chosen
(Must have a .sqlite suffix)
You do not need to export or convert the database - simply upload the .sqlite file that your program creates.
See the example code for the use of the connect() statement.

Musical Track Database
This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip.
The ZIP file contains the tracks.csv file to be used for this assignment. You can export your own tracks from iTunes and create a database, 
but for the database that you turn in for this assignment, only use the tracks.csv data that is provided. You can adapt the tracks_csv.py 
application in the zip file to complete the assignment.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)
                Track                   Artist	   Album	   Genre
            Chase the Ace	            AC/DC	Who Made Who	Rock
                 D.T.	                AC/DC   Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
''' 

#Practice code
'''
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
'''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
'''
'''
handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip();
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]

    print(name, artist, album, count, rating, length)

    cur.execute(''''''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )'''''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute(''''''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )'''''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute(''''''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )'''''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()
'''
#Soln.

import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')
#Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
#0                            1          2      3   4     5     6
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces)<7: continue
    Title = pieces[0]
    Artist = pieces[1]
    Album = pieces[2]
    Count = pieces[3]
    Rating = pieces[4]
    Length = pieces[5]
    Genre = pieces[6]

    cur.execute(''' INSERT OR IGNORE INTO Artist (Name) VALUES (?)''', ( Artist, ))
    cur.execute('SELECT Id FROM Artist WHERE Name = ? ', (Artist, ))
    Artist_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Genre (Name) VALUES (?)''', ( Genre, ))
    cur.execute('SELECT Id FROM Genre WHERE Name = ? ', (Genre, ))
    Genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (Title, Artist_id) 
            VALUES ( ?, ? )''', ( Album, Artist_id ) )
    cur.execute('SELECT Id FROM Album WHERE Title = ? ', (Album, ))
    Album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR REPLACE INTO Track
        (Title, Album_id, Len, Rating, Count, Genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( Title, Album_id, Length, Rating, Count, Genre_id ) )
    conn.commit()


sqlstr = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''

for row in cur.execute(sqlstr):
    print(row)