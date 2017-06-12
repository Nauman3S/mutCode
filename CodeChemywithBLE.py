from sqlalchemy import *
import datetime
import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

import bluetooth

#from mutagen.mp3 import flac
db = create_engine('sqlite:///db0.db')

db.echo = False  # Try changing this to True and see what happens
dirFiles=[]
#metadata = BoundMetaData(db)
metadata = MetaData(bind=db)

Tracks = Table('Tracks', metadata,
    Column('TrackID', Integer, primary_key=True),
    Column('AlbumID', Integer),
    Column('ArtistID', Integer),
    Column('Filename', String),
    Column('TrackListing',Integer),
    Column('Duration',Integer),
    Column('TrackTitle',String),
    Column('Year',Integer),
    Column('FileType',String),
    Column('TimeStamp',String),
    Column('PlayCount',Integer),
    Column('LastPlay',String),
)

Artists = Table('Artists', metadata,
    Column('ArtistID', Integer, primary_key=True),
    Column('ArtistName', String),
)
Albums = Table('Albums', metadata,
    Column('AlbumUID', Integer, primary_key=True),
    Column('AlbumTitle', String),
    Column('ArtistID', Integer),
  
)

#Tracks.create()
#Artists.create()
#Albums.create()
def TracksF(AlbumID0, ArtistID0,Filename0,TrackListing0, Duration0,TrackTitle0, Year0, FileType0,TimeStamp0,PlayCount0, LastPlay0):
    
    i = Tracks.insert()
    #i.execute(name='Mary', age=30, password='secret')
    i.execute({'AlbumID': AlbumID0, 'ArtistID': ArtistID0,'Filename':str(Filename0),'TrackingList':TrackListing0,'Duration':Duration0,'TrackTitle':str(TrackTitle0),'Year':Year0,'FileType':str(FileType0),'TimeStamp':str(TimeStamp0),'PlayCount':PlayCount0,'LastPlay':str(LastPlay0)})
def ArtistsF(name):
    
    i=Artists.insert()
    i.execute({'ArtistName':str(name)})
def AlbumsF(albumTitle0,ArtistID0):
    
    i=Albums.insert()
    i.execute({'AlbumTitle':str(albumTitle0),'ArtistID':ArtistID0})

filesList=[]


#TracksF(12,33,"CodeChemy.py",12,33,"Lahore1",1997,"exe",str(datetime.datetime.now()),12,"12-9-2017")
#ArtistsF("Alp")
#AlbumsF("TitleOf",12)

s = Tracks.select()
rs = s.execute()

#row = rs.fetchone()
#row=rs.fetchone()
#print('FileNmae:',row['Filename'])

#for row in rs:
#    print(row.Filename+'\n')
print(rs.fetchall())

s1=Artists.select()
rs1=s1.execute()
print(rs1.fetchall())

s2=Albums.select()
rs2=s2.execute()
print(rs2.fetchall())

def getInfo(file):
    audio = EasyID3("Music\\"+file)
    tt=(audio['title'] )#track title
    an=(audio['artist'])#artist name
    print(audio['albumartist'])
    at=(audio['album'] )##albumTitle
    yr=(audio['date'] )##year
    #print(audio.keys())
#getInfo('mf.mp3')
Art=""
Song=""
Alb=""
ASA=[0,0,0]#art,song,alb
def readid3mp3(ip):

    audio = MP3(ip)

    if ((audio['TPE1']) == 0):
         tags.add = ID3()
         tags.add(TPE1(encoding=3, text =["Not Available"]))

    else:
         Art = (audio['TPE1'])

    if ((audio['TIT2']) == 0):
        tags.add =ID3()
        tags.add(TIT2(encoding=3, text ="Not Available"))

    else:
         Song = (audio['TIT2'])


    if ((audio['TALB']) is None):
         tags.add = ID3()
         tags.add(TALB(encoding=3, text ="Not Available"))

    audio = MP3(ip)    
    
    ASA[0]  = (audio['TPE1'])
    ASA[1] = (audio['TIT2'])
    ASA[2]  = (audio['TALB'])
    #ASA.append((audio['TPE1'])
    #ASA.append((audio['TT2'])
    #ASA.append((audio['TALB'])
    print(ASA[1])
    print(ASA[0])
    print(ASA[2])


#Print into file

    #myFile.write ("\n"+"Artist"+"\t \t \t Song Name" + "\t Album Name" )
    #myFile.write ("\n"+ str(Art) + "\t" + str(Song) + "\t" + str(Alb))

#Close File
#myFile.close()

#return


#Open File
 
def FileSearch():
    dbFiles=[]
    row=rs.fetchone()
    for row in rs:
        dbFiles.append(row.Filename)
    filesList=[]
    for file in os.listdir("Music/"):
        filesList.append(file)
    print(filesList)
    x=[x for x in filesList if x not in dbFiles]
    global dirFiles
    for i in range(0,len(x)):
        dirFiles.append(x[i])
    #dirFiles=x
    print(dirFiles)
    #print(x)

FileSearch()
def senderDBtoBLE():
    
    serverMACAddress = '00:1f:e1:dd:08:3d'
    port = 3
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    f=open('db0.db','r')
    data=f.read()
    ###reading the data file before sending
    while 1:
        
        s.send(data)
        break
    f.close()




    sock.close()

#print(dirFiles[4])

#getInfo(dirFiles[1])

TracksF(1,1,"01-drake-free_smoke-d553d2b7",1,3.38,"Free Smoke",2017,"mp3",str(datetime.datetime.now()),1,"2017")
ArtistsF("Drake")
AlbumsF("More Life",1)


TracksF(2,1,"02-drake_feat_giggs-no_long_talk-7d459400",1,2.29,"No Long Talk",2017,"mp3",str(datetime.datetime.now()),1,"2017")
ArtistsF("Drake feat")
AlbumsF("More Life",1)

TracksF(3,1,"03-drake-passionfruit-732fe97c",1,4.58,"Passionfruit",2017,"mp3",str(datetime.datetime.now()),1,"2017")
ArtistsF("Drake")
AlbumsF("More Life",1)


senderDBtoBLE()###sending DB file to BLE connected device

#TracksF(AlbumID0, ArtistID0,Filename0,TrackListing0, Duration0,TrackTitle0, Year0, FileType0,TimeStamp0,PlayCount0, LastPlay0):
#AlbumsF(albumTitle0,ArtistID0):

#mediafile = ID3("Music//"+dirFiles[2])
#metadata = mediafile.pprint()

#myFile = open("AlbArtSong.txt", "a+")

#Enter Inputs

#ip = input("Enter Mp3 file: ")
k=[]
##for i in range(2,len(dirFiles)):
##    
##    
##               
##    #try:
##        
##
##
##    print("tryyyyyyyyyyyyyyyyyyy")
##    m=readid3mp3("Music//"+dirFiles[i])
##    print(m)
##    print("Music//"+dirFiles[i])
##    k=dirFiles.split(".")
##    print("k======="+k)
##    TracksF(12,33,dirFiles[i],12,33,ASA[1],1997,k[1],str(datetime.datetime.now()),12,"12-9-2017")
##    ArtistsF(ASA[0])
##    AlbumsF(ASA[2],12)
##    TracksF(12,33,dirFiles[i],12,33,ASA[1],1997,k[1],str(datetime.datetime.now()),12,"12-9-2017")
##    ArtistsF(ASA[0])
##    AlbumsF(ASA[2],12)
###except:
##    
##    print("er")
     




##print( 'AlbumID:', row['TrackID'])
##print( 'Name:', row['Filename'])
##print( 'Age:', row.TrackTitle)

#print ('Password:', row[Tracks.c.password])

##for row in rs:
##    print( row.TrackTitle)
