##ref https://nedbatchelder.com/code/modules/id3reader.html

import id3Reader
import os
files=[]
for file in os.listdir(os.getcwd()):
    files.append(file)
    print(file)

# Construct a reader from a file or filename.
#id3r = id3Reader.Reader('ophelia.mp3')
#print(files)
print('files ID3 Data-----------\n\n\n')
for i in range(0,len(files)):
    if('mp3' in files[i]):
        id3r = id3Reader.Reader(files[i])
        print (id3r.getValue('album'))
        print (id3r.getValue('title'))
        print (id3r.getValue('track'))
        print (id3r.getValue('year'))
# Ask the reader for ID3 values:


