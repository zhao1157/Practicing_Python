#! /usr/bin/env python3
"""
==========Design========
First of all, I just read all the lines into a list, which can be found the number of 
elements in the list, i.e. the number of lines in the file, and did a simple test, which
is purely for my practice purpose. Then I started to extract the useful information by 
using readline() function for each line, and split it into a list by using split() for the 
string. Finally print out the enegy mesh in Ry and ev units.
========================
"""
filename = 'raw_energy_mesh_454' 	#The name of the file containing the data
mode = 'r'

f = open(filename, mode)

num_line = len(f.readlines()) 	#Find the number of lines in the file

f.close()	#Since the control has reached the end of the file, so we need to close and 
			#reopen it.
if num_line == 24767:
	print ('Good, you find the correct number of lines in the file\n')
else: 
	print ("Wrong, exiting from the script\n")
	raise SystemExit()	#This function is recommended, not quit() nor exit()

f = open(filename, mode)
f_extract = open ('extract_'+filename, 'w')

for i in range (1, num_line+1): #range(2, 4) is 2, 3, but 4 is not included.
	line = f.readline()
	if i >= 17:
		line = line.split() #Split the string into a list and access the photo-electron 
							#energy.
		energy_final = float(line[1]) * 13.605698066
		f_extract.write('{0}    {1:.9E}\n'.format(line[1], energy_final))

f.close()
f_extract.close()

