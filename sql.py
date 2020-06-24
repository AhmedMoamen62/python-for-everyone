import sqlite3

## connect the database file
conn = sqlite3.connect('emaildb.sqlite')
## cursur is the handler
cur = conn.cursor()

## delete the table if is has Counts exist
cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname  = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()
	email = pieces[1]
	org = email[email.find('@') + 1:]
	## (email,) it's a tuple and ? is a place holder 
	cur.execute('SELECT count FROM Counts WHERE org = ? ',(org,))
	## fetch one row
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''',(org,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
	
## commit the changes to the database, it's a slow operation so it should be called after all changes is done
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count'
counts = cur.execute(sqlstr)
counts_list = list(counts)
print(counts_list[len(counts_list) - 1][1])

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