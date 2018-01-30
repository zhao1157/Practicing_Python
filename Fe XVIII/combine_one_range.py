#This script is usd to combine small section of photoionization cross section data into one

#================ INPUT ===================
num_level = 73	#number of levels for this initial symmetry
index_range = 0	#the index of the big section, which can commented out in some case
index_skip = [97]	#include all the small index which does not have XSECTN data
num_subrange = 100	#the number of sub-ranges in index_range
out_file = "XSECTN_total"	#the filename of the output data

#=========================================================================================
#======================== BLOCK BOX, BUT SHOULD BE MODIFIED IN SOME CASE =================
#================================= FILE_NAME[] & RANGE(42) ===============================
#open the individual file
files = []
file_name = []
for index in range(num_subrange):
	skip = False
	for i in index_skip:
		if (index == i):
			skip = True
			break
	
	if (skip == True):
		file_name.append("skip")
		files.append("skip_file")
		continue	
	file_name.append("XSECTN_"+str(index_range)+"_"+str(index))
	files.append(open(file_name[index], 'r'))

f_out = open(out_file, 'w')	

#start the processing for all the levels
for level in range(num_level):
	print "level= ", level
	first_file = 0
	head = []
	num_points = 0
	XSECTN = []
	
	#collect the data for each level
	for index in range(num_subrange):
		if (file_name[index] == 'skip'):
			continue
		print " "*4+"subrange= ", index
		first_file += 1
		
		#collect the head data in the first file, and just move the control for other files.
		if (first_file == 1):
			for line_num in range(42):
				head.append(files[index].readline())
		else:
			for line_num in range(42):	
				files[index].readline()
		energy_num_points = files[index].readline().split()	
		num_points += int(energy_num_points[1])
		zeros = files[index].readline()
		#now it's time to read the XSECTN data
		for line_num in range(int(energy_num_points[1])):
			XSECTN.append(files[index].readline())
	
	#Now the data for this level has been collected, so it's time to write to the final file.		
	for line_num in range(42):
		f_out.write(head[line_num])				
	
	f_out.write("  "+energy_num_points[0]+" "*5+str(num_points)+"\n")	
	f_out.write(zeros)
	for xsectn_line in XSECTN:
		f_out.write(xsectn_line)

#Close the files	
for index in range(num_subrange):
	skip = False
	for i in index_skip:
		if (index == i):
			skip = True
			break
	
	if (skip == True):
		continue	
	files[index].close()

f_out.close()	
	
