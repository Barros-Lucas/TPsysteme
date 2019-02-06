# -*- coding: utf-8 -*
import signal,sys
import os

pid = os.getpid() 

print ("Je boucle sans fin. Arrêtez-moi avec un kill -USR1 " +str(pid))

def handler(num_sig, frame):
	exit(0)

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, handler)

while True: pass
