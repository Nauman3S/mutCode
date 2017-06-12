import sqlite3
import datetime
conn = sqlite3.connect('TBL4.db')
c = conn.cursor()

 #Create table
##c.execute('''CREATE TABLE Tracks
##             (TrackID INTEGER PRIMARY KEY AUTOINCREMENT, AlbumID INTEGER, ArtistID INTEGER, Filename text, TrackListing INTEGER, Duration INTEGER, TrackTitle text, Year INTEGER, FileType text, Timestamp text, Playcount INTEGER, LastPlay text)''')
##
##c.execute('''CREATE TABLE Artists
##             (ArtistID INTEGER PRIMARY KEY AUTOINCREMENT, ArtistName text)''')
##
##c.execute('''CREATE TABLE Albums
##             (AlbumUID INTEGER PRIMARY KEY AUTOINCREMENT, AlbumTitle text, ArtistID INTEGER)''')

# Insert a row of data
#name='nameofArtist'
def Tracks(AlbumID, ArtistID,Filename,TrackListing, Duration,TrackTitle, Year, FileType,Timestamp,Playcount, LastPlay):

    c.execute("""INSERT INTO Tracks (AlbumID,ArtistID,Filename) VALUES (?,?,?)"""%(AlbumID,ArtistID,str(Filename)))
    
    c.execute("""INSERT INTO Tracks (Filename) VALUES ('"""+str(Filename)+"""')""")
def Artists(name):
    c.execute("""INSERT INTO Artists (ArtistName) VALUES ('"""+str(name)+"""')""")
def Albums(albumTitle,ArtistID):

    c.execute("""INSERT INTO Albums (AlbumTitle,ArtistID) VALUES ('"""+str(albumTitle)+"""',%d)"""%ArtistID)
# Save (commit) the changes

Tracks(12,2,"ABC",23,12,"Ttilte",2012,"exe",str(datetime.datetime.now()),3,"12-2-2014")
Artists("abc")
Albums("abc",2)
conn.commit()

print(datetime.datetime.now())
c.execute("SELECT * FROM Tracks")
a=c.fetchall()
print(a)
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
