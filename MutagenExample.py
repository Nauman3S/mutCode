from mutagen.easyid3 import EasyID3
audio = EasyID3("ophelia.mp3")
print(audio['title'] )#track title
print(audio['artist'])#artist name
print(audio['albumartist'])
print(audio['album'] )##albumTitle
print(audio['date'] )##year
print(audio.keys())
#print(audio['composer'])
audio.pprint()
#audio.save()
