# TO_SPARSE_FORMAT --> Lee el fichero (matricial) que se le pasa por linea de comandos y lo convierte a Sparse_Format.
import sys
import random 

file_name = sys.argv[1]
print "Start on "+file_name +" >> ",


f = open(file_name)
data = f.read().strip()
f.close()
     
M = [[float(num) for num in line.strip().split()] for line in data.split('\n')]
print "File Read >> Start Write new document with SPARSE FORMAT"

file_out_name = "T_S_F_"+file_name
file_out = open(file_out_name, 'w')

for line in M:
	if((random.randint(0,10000000000)%2)==0):
		file_out.write ("+1 "),
	else:
		file_out.write ("-1 "),
	cont = 1
	for element in line:
		if(element != 0):
			file_out.write ( '%d'%(cont) + ":" + '%s'%(element) +" "),
		cont = cont +1
	file_out.write ("\n")

file_out.close()
print "Finish, Work complete"