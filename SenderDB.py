"""
PyBluez (with Python 2).
"""

import bluetooth


serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
f=open('database.db','r')
data=f.read()
###reading the data file before sending
while 1:
    
    s.send(data)
    break
f.close()




sock.close()
