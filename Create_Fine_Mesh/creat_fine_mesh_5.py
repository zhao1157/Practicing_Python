#! /usr/bin/env python3
#As the node does not have numpy installed, I will have to move the files to my Mac to do the work.

#This script is to create the fine mesh for all initial levels
import numpy as np

f = open('fine_mesh_bf', 'w')

for line in open('level_thresh_order_mini_diff'):
	line_split = line.split()
	
	length = len(line_split)
	
	line_split[-1] = float(line_split[-1])
	#line_split[-1] = line_split[-1] if line_split[-1] < 1 else 1
	if line_split[-1] > 1:
		line_split[-1] = 1
		
	delta = line_split[-1]/10.0
	
	fine_mesh = []
	
	for num_thresh in range(1, length-2):
		e1 = float(line_split[num_thresh])+delta
		e2 = float(line_split[num_thresh+1])-delta
		
		if num_thresh < length-3:
			fine_mesh += list(np.linspace(e1, e2, 10))
		else:
			fine_mesh += list(np.linspace(e1, e2, 250))
		
	f.write(line_split[0]+' ')
	
	for i in range(len(fine_mesh)):
		f.write('{:.9E} '.format(fine_mesh[i]))
	f.write('\n')
	
f.close()

#To make sure all the points are different.
#Run an awk program
import os
os.system('./test_same.awk fine_mesh_bf')


