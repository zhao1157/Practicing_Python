"""
	This is to extract the incident photon energy mesh from p-file for each bound level.
"""
import sys 
level_index = int(sys.argv[1])	

file_name_RM = '../../fe17_454_tail/outfile/combine_sultana_fac_5/fe17.px.60cc.fac'
file_name_mesh = 'RM_mesh_dir/'+sys.argv[1]


f_RM = open (file_name_RM, 'r')	
f_mesh = open (file_name_mesh, 'w')

#move control across the region of no-interest
for i in range(1, (level_index - 1)*24767+17):
	f_RM.readline()

#Here we are, and start working
for i in range (1, 24752):
	line_RM = f_RM.readline()
	line_RM_list = line_RM.split()
	
	f_mesh.write(line_RM_list[0]+'\n')
	
f_RM.close()
f_mesh.close()
	
	
	
