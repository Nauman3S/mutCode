import sqlite3
conn = sqlite3.connect('TBL1.db')
c = conn.cursor()

#print(c.execute('SELECT * FROM Tracks'))
print(c.fetchall())
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
