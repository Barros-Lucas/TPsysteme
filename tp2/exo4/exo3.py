
import sys
import os
import codecs

rdCS, wrCS = os.pipe()
rdSC, wrSC = os.pipe()

# search how i can loop on the read to get all the return without increase TAMPON size
TAILLE_TAMPON = 1024

if os.fork() == 0:
    os.close(wrCS)
    while True:
        r = os.read(rdCS, TAILLE_TAMPON)
        if r.decode().lower() == "quit".lower():
            sys.exit(0)
        retour = ""
        if not os.path.isfile(r.decode()):
            retour = "ce fichier n'existe pas"
        else:
            with open(r.decode(), 'r') as content_file:
                retour = content_file.read()
        os.write(wrSC, retour.encode())

    
os.close(wrSC)
while True:
    
    mess = input("message : ")
    if mess.lower() == "quit".lower():
        os.write(wrCS, "quit".encode())
        os.wait()
        sys.exit(0)
    os.write(wrCS, mess.encode())
    r = os.read(rdSC, TAILLE_TAMPON)
    print(r.decode())
