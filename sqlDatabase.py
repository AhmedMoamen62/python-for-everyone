import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

## unique TEXT , say if we have two similar name or title any text it gonna fail
# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = 'roster_data.json'

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]

    print((name, title,role))

    ## ignore to skip if an error happens, like twice name or title and it's a unique
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    ## get the unique id of the name
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role) )

cur.execute('''
	SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
''')
conn.commit()



# import xml.etree.ElementTree as ET
# import sqlite3

# ## if not found, it will create it
# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()

# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;

# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY 
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );

# ''')

# fname = 'Library.xml'

# def lookup(d,key):
# 	found = False
# 	for child in d:
# 		if found: return child.text
# 		if child.tag == 'key' and child.text == key:
# 			found = True
# 	return None

# stuff = ET.parse(fname)
# all = stuff.findall('dict/dict/dict')
# print('Dict count',len(all))
# for entry in all:
# 	if (lookup(entry,'Track ID') is None) : continue

# 	name = lookup(entry,'Name')
# 	artist = lookup(entry,'Artist')
# 	album = lookup(entry,'Album')
# 	genre = lookup(entry,'Genre')
# 	count = lookup(entry,'Play Count')
# 	rating = lookup(entry,'Rating')
# 	length = lookup(entry,'Total Time')

# 	if name is None or artist is None or album is None or genre is None:
# 		continue

# 	print(name,genre,artist,count,rating,length)


# 	## ignore , if it is exist , don't insert again
# 	cur.execute('''INSERT OR IGNORE INTO Artist (name)
# 				VALUES ( ? )''',(artist,))
# 	cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
# 	artist_id = cur.fetchone()[0]

# 	cur.execute('''INSERT OR IGNORE INTO Genre (name)
# 				VALUES ( ? )''',(genre,))
# 	cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
# 	genre_id = cur.fetchone()[0]

# 	cur.execute('''INSERT OR IGNORE INTO Album (title,artist_id)
# 				VALUES ( ?, ? )''',(album,artist_id))
# 	cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
# 	album_id = cur.fetchone()[0]

# 	cur.execute('''INSERT OR REPLACE INTO Track (title,genre_id,album_id,len,rating,count)
# 				VALUES ( ?, ?, ?, ?, ?, ? )''',(name,genre_id,album_id,length,rating,count))


# cur.execute('''
# SELECT Track.title, Artist.name, Album.title, Genre.name 
#     FROM Track JOIN Genre JOIN Album JOIN Artist 
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3
# ''')
# conn.commit()

# import sqlite3

# ## connect the database file
# conn = sqlite3.connect('emaildb.sqlite')
# ## cursur is the handler
# cur = conn.cursor()

# ## delete the table if is has Counts exist
# cur.execute('''DROP TABLE IF EXISTS Counts''')
# cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fname  = 'mbox.txt'
# fh = open(fname)
# for line in fh:
# 	if not line.startswith('From: '): continue
# 	pieces = line.split()
# 	email = pieces[1]
# 	org = email[email.find('@') + 1:]
# 	## (email,) it's a tuple and ? is a place holder 
# 	cur.execute('SELECT count FROM Counts WHERE org = ? ',(org,))
# 	## fetch one row
# 	row = cur.fetchone()
# 	if row is None:
# 		cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''',(org,))
# 	else:
# 		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
	
# ## commit the changes to the database, it's a slow operation so it should be called after all changes is done
# conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count'
# counts = cur.execute(sqlstr)
# counts_list = list(counts)
# print(counts_list[len(counts_list) - 1][1])

# ## connect the database file
# conn = sqlite3.connect('emaildb.sqlite')
# ## cursur is the handler
# cur = conn.cursor()

# ## delete the table if is has Counts exist
# cur.execute('''DROP TABLE IF EXISTS Counts''')
# cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

# fname  = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
# 	if not line.startswith('From: '): continue
# 	pieces = line.split()
# 	email = pieces[1]
# 	## (email,) it's a tuple and ? is a place holder 
# 	cur.execute('SELECT count FROM Counts WHERE email = ? ',(email,))
# 	## fetch one row
# 	row = cur.fetchone()
# 	if row is None:
# 		cur.execute('''INSERT INTO Counts (email,count) VALUES (?,1)''',(email,))
# 	else:
# 		cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
# 	## commit the changes to the database, it's a slow operation so it should be called after all changes is done
# 	conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# ## row is a tuple of email and counts
# for row in cur.execute(sqlstr):
# 	print(str(row[0]),row[1])


## INSERT INTO Users (name,email) VALUES ('ahmed','ahmedmoamen138@gmail.com')
## DELETE FROM Users WHERE email='ahmedmoamen138@gmail.com'
## UPDATE Users SET name="ahmed" WHERE email="ahmedmoamen138@gmail.com"
## SELECT * FROM Users
## SELECT * FROM Users WHERE email='ahmedmoamen138@gmail.com'
## SELECT * FROM Users ORDER BY email

## SELECT Album.title,Album.artist_id,Artist.id,Artist.name FROM Album JOIN Artist on Album.artist_id = Artist.id
	# SELECT Track.title,Artist.name,Album.title,Genre.name
	# from Track JOIN Genre JOIN Album JOIN Artist 
	# on Track.genre_id = Genre.id and Track.album_id = Album.id 
	# and Album.artist_id = Artist.id