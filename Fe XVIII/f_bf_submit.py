#use python 2.x
#This script is to run stgf, prebf and stgbf for the main energy range which is divided
#into many small sections.
import os

#specify the increment of the z-scaled energy and the number of points in each region
incremet = 85.0/18/18/1000
print (incremet)	#make sure the increment is no-zero by eye inspection.
num_pts = 20		#number of points in each region
num_region = 50		#number of regions to be divided.
b_symmetry = "0 1 1"	#initial symmetry which is ONLY one.
f_symmetry = "0 1 0\n0 3 0"		#final symmetries which are at most 3.

#                           *********** BLACK BOX ***********
#                           ***********           ***********
#*************************** Dont' Touch the following code! *****************************
#                           *********************************

#Set the content of stgbf.inp file, which is the same for all the runs.
content_stgbf = "\
-1 0 0\n\
"+b_symmetry+ " 0 0\n\
"+f_symmetry+"\n\
-1 -1 -1\n\
"

#a directory where XSECTN files are collected
os.popen('if [ -d XSECTN ]; then rm -rf XSECTN; fi; mkdir XSECTN;')

for i in range(num_region):
	#========= 1 ========
	#Write the content of the PBS file.
	content_pbs = "\
#PBS -A PAS0578\n\
#PBS -l walltime=168:00:00\n\
#PBS -l nodes=1:ppn=3\n\
#PBS -N f_bf_" + str(i) + "\n\
#PBS -j oe\n\
#PBS -m a\n\
#PBS -S /bin/bash\n\
\n\
cd ${PBS_O_WORKDIR}/f_bf_" + str(i) +"\n\
\n\
ln -s ../mkouter_f\n\
ln -s ../mkouter_bf\n\
\n\
ln -s ../H\n\
for d_file in $(ls ../D??); do ln -s ${d_file}; done\n\
for b_file in $(ls ../run_stgb/B??); do ln -s ${b_file}; done\n\
\n\
./mkouter_f && sleep 2 && ifort stgfjj.o && sleep 2 && ./a.out < stgf.inp > stgf.out && sleep 2\n\
\n\
if [ -f DVEC ]; then rm -f DVEC; fi; sleep 2;\n\
./mkouter_bf && sleep 2 && ifort prebf.o && sleep 2 && ./a.out < stgbf.inp > prebf.out && sleep 2\
&& ifort rstgbf.o && sleep 2 && ./a.out < stgbf.inp > stgbf.out\n\
\n\
mv XSECTN ../XSECTN/XSECTN_" + str(i) + "\n\
"

	#========== 2 =======
	#Write the content of stgf.inp file.
	content_stgf = "\
0 2 1 250\n\
0.0001\n\
1\n\
1\n\
"+str(num_pts)+" "*3 + str(incremet*num_pts*i) +" "*3 + str(incremet) + "\n\
2\n\
"+f_symmetry+"\n\
"

	#========== 3 ==========
	#Create directory
	os.popen('if [ -d f_bf_'+str(i)+' ]; then rm -rf f_bf_'+str(i)+'; fi; mkdir f_bf_'\
			+str(i)+';')
	#Write to files
	f = open('f_bf_'+str(i)+'/my_pbs', 'w')
	f.write(content_pbs)
	f.close()
	
	f = open('f_bf_'+str(i)+'/stgf.inp', 'w')
	f.write(content_stgf)
	f.close()
	
	f = open('f_bf_'+str(i)+'/stgbf.inp', 'w')
	f.write(content_stgbf)
	f.close()
	
	#========== 4 ==========
	#Submit the job now
	os.popen('qsub f_bf_' + str(i) + '/my_pbs; sleep 2')
	
