# -*- coding: utf-8 -*
import sys
import os

if len(sys.argv) < 3:
	print("Veuillez renseigner au moins un fichier .c et le nom de l'éxécutable")
	sys.exit(1)
print(sys.argv)

for arg in (1, len(sys.argv)-1):
	if not os.path.isfile(sys.argv[arg]):
		# Teste si le fichier source existe
		print("{} n’existe pas".format(sys.argv[arg]))
		sys.exit(2)

for arg in range(1, len(sys.argv)-1):

	if os.fork() == 0:
		#fic = os.open("/tmp/erreurs", os.O_CREAT|os.O_WRONLY|os.O_TRUNC)
		#os.dup2(fic, 2)
		#os.execlp("c99", "c99", " -c", arg)
		print("c99 -c "+sys.argv[arg])
		
(pid, status) = os.wait()

if status != 0:
	print ("ok")
