# -*- coding: utf-8 -*
import sys
import os

#fichiers = []
#ficss = sys.argv[2:(len(sys.argv))]
#for i in ficss:
#	fichiers.append(i)

exec = ["wc"]
exec.append("sort")
exec.append("-k")
exec.append(sys.argv[1])
exec.append(sys.argv[2])

if os.fork() == 0:
	fic = os.open("./erreurs_", os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
	os.dup2(fic, 2)
	os.execvp("wc",exec)
		

(pid, status) = os.wait();
if status != 0:
	print("null")

##copier
erreur = 0		
for arg in fichiers:
	(pid, status) = os.wait()
	if status != 0:
		erreur +=1

if erreur != 0:
	print(str(erreur)+" échec(s)")
	sys.exit(4)
