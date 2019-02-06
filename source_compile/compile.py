# -*- coding: utf-8 -*
import sys
import os

if len(sys.argv) < 3:
	print("Veuillez renseigner au moins un fichier .c et le nom de l'éxécutable")
	sys.exit(1)

for arg in (1, len(sys.argv)-2):
	if not os.path.isfile(sys.argv[arg]):
		# Teste si le fichier source existe
		print("{} n’existe pas".format(sys.argv[arg]))
		sys.exit(2)

fics = []
ficss = sys.argv[1:(len(sys.argv)-1)]
for i in ficss:
	fics.append(i.split(".")[0])

#Creation des .o
for arg in fics:
	if os.fork() == 0:
		fic = os.open("./erreurs_"+arg, os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
		os.dup2(fic, 2)
		os.execlp("c99", "c99", "-c", arg+".c")
		

erreur = 0		
for arg in fics:
	(pid, status) = os.wait()
	if status != 0:
		erreur = status

if erreur != 0:
	print("Une erreur s'est produite")
	sys.exit(4)


#Creation de l'exec
temp = []
temp.append("c99")
for arg in fics:
	temp.append(arg+".o")
	
temp.append("-o")
temp.append(sys.argv[len(sys.argv)-1])
if os.fork() == 0:
	fic = os.open("./erreurs2", os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
	os.dup2(fic, 2)
	os.execvp("c99",temp)

(pid, status) = os.wait()
if status != 0:
	print("Une erreure s'est produite lors de la création de l'exécutable")






