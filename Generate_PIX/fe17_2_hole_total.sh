#! /bin/bash

for i in $(seq 1 10)
do
	if [ $i -lt 10 ]
	then
		line_start=$(( (i-1)*5000+1 ))
		line_end=$(( i*5000 ))
	else
		line_start=$((9*5000+1))
		line_end=50938
	fi
	
	if [ -d run_${i} ]
	then
		rm -rf run_${i}
	fi
	
	mkdir run_${i}
	
	cat << eof > run_${i}/fe17_2_hole_total.py
from pfac import fac 

fac.SetAtom('Fe')

#Set the configurations
fac.Closed('1s')
##The ground and the ionized configurations used for energy calibration
##purposes.
fac.Config('T.G', '2s2 2p6')
fac.Config('T.G.2p', '2s2 2p5')

##Initial configurations
###T1:
fac.Config('T1.3*2', '2p6 3*2')
fac.Config('T1.3*1.4*1', '2p6 3*1 4*1')
fac.Config('T1.3*1.5*1', '2p6 3*1 5*1')
fac.Config('T1.3*1.6*1', '2p6 3*1 6*1')

fac.Config('T1.4*2', '2p6 4*2')
fac.Config('T1.4*1.5*1', '2p6 4*1 5*1')
fac.Config('T1.4*1.6*1', '2p6 4*1 6*1')

fac.Config('T1.5*2', '2p6 5*2')
fac.Config('T1.5*1.6*1', '2p6 5*1 6*1')

fac.Config('T1.6*2', '2p6 6*2')

fac.Config('T1.3*1', '2p6 3*1')
fac.Config('T1.4*1', '2p6 4*1')
fac.Config('T1.5*1', '2p6 5*1')
fac.Config('T1.6*1', '2p6 6*1')
###T2:
fac.Config('T2.3*2', '2s1 2p5 3*2')
fac.Config('T2.3*1.4*1', '2s1 2p5 3*1 4*1')
fac.Config('T2.3*1.5*1', '2s1 2p5 3*1 5*1')
fac.Config('T2.3*1.6*1', '2s1 2p5 3*1 6*1')

fac.Config('T2.4*2', '2s1 2p5 4*2')
fac.Config('T2.4*1.5*1', '2s1 2p5 4*1 5*1')
fac.Config('T2.4*1.6*1', '2s1 2p5 4*1 6*1')

fac.Config('T2.5*2', '2s1 2p5 5*2')
fac.Config('T2.5*1.6*1', '2s1 2p5 5*1 6*1')

fac.Config('T2.6*2', '2s1 2p5 6*2')

fac.Config('T2.3*1', '2s1 2p5 3*1')
fac.Config('T2.4*1', '2s1 2p5 4*1')
fac.Config('T2.5*1', '2s1 2p5 5*1')
fac.Config('T2.6*1', '2s1 2p5 6*1')
###T3:
fac.Config('T3.3*2', '2s2 2p4 3*2')
fac.Config('T3.3*1.4*1', '2s2 2p4 3*1 4*1')
fac.Config('T3.3*1.5*1', '2s2 2p4 3*1 5*1')
fac.Config('T3.3*1.6*1', '2s2 2p4 3*1 6*1')

fac.Config('T3.4*2', '2s2 2p4 4*2')
fac.Config('T3.4*1.5*1', '2s2 2p4 4*1 5*1')
fac.Config('T3.4*1.6*1', '2s2 2p4 4*1 6*1')

fac.Config('T3.5*2', '2s2 2p4 5*2')
fac.Config('T3.5*1.6*1', '2s2 2p4 5*1 6*1')

fac.Config('T3.6*2', '2s2 2p4 6*2')

fac.Config('T3.3*1', '2s2 2p4 3*1')
fac.Config('T3.4*1', '2s2 2p4 4*1')
fac.Config('T3.5*1', '2s2 2p4 5*1')
fac.Config('T3.6*1', '2s2 2p4 6*1')
############################################
#structure
fac.ConfigEnergy(0)
fac.OptimizeRadial(['T.G'])
fac.ConfigEnergy(1)

#create a directory to contain the output files, energy and PI.
import os
os.system('if [ -d out_dir ]; then rm -rf out_dir; fi; mkdir out_dir')
outfile_lev_b = 'out_dir/fe17_2_hole_b.en'
outfile_lev_a = outfile_lev_b[:-4]+'a.en'

outfile_rr_b = 'out_dir/fe17_2_hole_b.rr'
outfile_rr_a = outfile_rr_b[:-4]+'a.rr'

#STRUCTURE
fac.Structure(outfile_lev_b, ['T.G'])
fac.Structure(outfile_lev_b, ['T.G.2p'])

fac.Structure(outfile_lev_b, ['T1.3*2', 'T2.3*2', 'T3.3*2'])
fac.Structure(outfile_lev_b, ['T1.3*1.4*1', 'T2.3*1.4*1', 'T3.3*1.4*1'])
fac.Structure(outfile_lev_b, ['T1.3*1.5*1', 'T2.3*1.5*1', 'T3.3*1.5*1'])
fac.Structure(outfile_lev_b, ['T1.3*1.6*1', 'T2.3*1.6*1', 'T3.3*1.6*1'])

fac.Structure(outfile_lev_b, ['T1.4*2', 'T2.4*2', 'T3.4*2'])
fac.Structure(outfile_lev_b, ['T1.4*1.5*1', 'T2.4*1.5*1', 'T3.4*1.5*1'])
fac.Structure(outfile_lev_b, ['T1.4*1.6*1', 'T2.4*1.6*1', 'T3.4*1.6*1'])

fac.Structure(outfile_lev_b, ['T1.5*2', 'T2.5*2', 'T3.5*2'])
fac.Structure(outfile_lev_b, ['T1.5*1.6*1', 'T2.5*1.6*1', 'T3.5*1.6*1'])

fac.Structure(outfile_lev_b, ['T1.6*2', 'T2.6*2', 'T3.6*2'])

fac.Structure(outfile_lev_b, ['T1.3*1', 'T2.3*1', 'T3.3*1'])
fac.Structure(outfile_lev_b, ['T1.4*1', 'T2.4*1', 'T3.4*1'])
fac.Structure(outfile_lev_b, ['T1.5*1', 'T2.5*1', 'T3.5*1'])
fac.Structure(outfile_lev_b, ['T1.6*1', 'T2.6*1', 'T3.6*1'])
#print the energy table
fac.MemENTable(outfile_lev_b)
fac.PrintTable(outfile_lev_b, outfile_lev_a, 1)

#print the rr table
##T1
fac.RRTable(outfile_rr_b, ['T1.3*2'], ['T1.3*1'])
fac.RRTable(outfile_rr_b, ['T1.3*1.4*1'], ['T1.3*1', 'T1.4*1'])
fac.RRTable(outfile_rr_b, ['T1.3*1.5*1'], ['T1.3*1', 'T1.5*1'])
fac.RRTable(outfile_rr_b, ['T1.3*1.6*1'], ['T1.3*1', 'T1.6*1'])

fac.RRTable(outfile_rr_b, ['T1.4*2'], ['T1.4*1'])
fac.RRTable(outfile_rr_b, ['T1.4*1.5*1'], ['T1.4*1', 'T1.5*1'])
fac.RRTable(outfile_rr_b, ['T1.4*1.6*1'], ['T1.4*1', 'T1.6*1'])

fac.RRTable(outfile_rr_b, ['T1.5*2'], ['T1.5*1'])
fac.RRTable(outfile_rr_b, ['T1.5*1.6*1'], ['T1.5*1', 'T1.6*1'])

fac.RRTable(outfile_rr_b, ['T1.6*2'], ['T1.6*1'])

##T2
fac.RRTable(outfile_rr_b, ['T2.3*2'], ['T2.3*1'])
fac.RRTable(outfile_rr_b, ['T2.3*1.4*1'], ['T2.3*1', 'T2.4*1'])
fac.RRTable(outfile_rr_b, ['T2.3*1.5*1'], ['T2.3*1', 'T2.5*1'])
fac.RRTable(outfile_rr_b, ['T2.3*1.6*1'], ['T2.3*1', 'T2.6*1'])

fac.RRTable(outfile_rr_b, ['T2.4*2'], ['T2.4*1'])
fac.RRTable(outfile_rr_b, ['T2.4*1.5*1'], ['T2.4*1', 'T2.5*1'])
fac.RRTable(outfile_rr_b, ['T2.4*1.6*1'], ['T2.4*1', 'T2.6*1'])

fac.RRTable(outfile_rr_b, ['T2.5*2'], ['T2.5*1'])
fac.RRTable(outfile_rr_b, ['T2.5*1.6*1'], ['T2.5*1', 'T2.6*1'])

fac.RRTable(outfile_rr_b, ['T2.6*2'], ['T2.6*1'])

##T3
fac.RRTable(outfile_rr_b, ['T3.3*2'], ['T3.3*1'])
fac.RRTable(outfile_rr_b, ['T3.3*1.4*1'], ['T3.3*1', 'T3.4*1'])
fac.RRTable(outfile_rr_b, ['T3.3*1.5*1'], ['T3.3*1', 'T3.5*1'])
fac.RRTable(outfile_rr_b, ['T3.3*1.6*1'], ['T3.3*1', 'T3.6*1'])

fac.RRTable(outfile_rr_b, ['T3.4*2'], ['T3.4*1'])
fac.RRTable(outfile_rr_b, ['T3.4*1.5*1'], ['T3.4*1', 'T3.5*1'])
fac.RRTable(outfile_rr_b, ['T3.4*1.6*1'], ['T3.4*1', 'T3.6*1'])

fac.RRTable(outfile_rr_b, ['T3.5*2'], ['T3.5*1'])
fac.RRTable(outfile_rr_b, ['T3.5*1.6*1'], ['T3.5*1', 'T3.6*1'])

fac.RRTable(outfile_rr_b, ['T3.6*2'], ['T3.6*1'])

#ASCII
#fac.PrintTable(outfile_rr_b, outfile_rr_a, 1)

os.system('if [ -d out ]; then rm -rf out; fi; mkdir out')
#This is to create the directory where the PI data are stored.
os.system('if [ -d xsectn ]; then rm -rf xsectn; fi; mkdir xsectn')

f = open('../../create_fine_mesh_2/fine_mesh_bf', 'r')
content = f.readlines()
num_line = len(content)
f.close()

print ('num_line=', num_line)

f = open('../../create_fine_mesh_2/fine_mesh_bf', 'r')

for i in range(1, num_line+1) :
	line = f.readline()
	
	if i > ${line_end} or i < ${line_start}: continue
	
	
	line_split = line.split()
	print line_split[0]

	for j in range(1, len(line_split)):
		line_split[j] = float(line_split[j])

	fac.InterpCross(outfile_rr_b, 'out/'+line_split[0]+'_temp', int(line_split[0]), -1,
            line_split[1:], 0)
	
	#run add algorithm to obtain the total PI cross section, and delete the temp file.
	add_command = ('os.system(' + '\'../add_awk.sh -v ind=' + line_split[0] + ' ' +
					'time_read=1 ' + 'out/'+line_split[0]+'_temp ' +
					'time_read=3 ' + 'out/'+line_split[0]+'_temp\'' + ')')
	#print (add_command)
	eval(add_command)
	
	rm_command = ('os.system(' +    '\'rm ' +  'out/'+line_split[0]+'_temp\''    + ')')
	eval (rm_command)
eof
	
	cat << eof > FAC_2_hole_${i}.pbs
#PBS -q bigmem
#PBS -l walltime=15:00:00
#PBS -l nodes=1:ppn=2
#PBS -l mem=8GB
#PBS -N FAC_2_hole_${i}
#PBS -S /bin/ksh
#PBS -j oe

cd \${PBS_O_WORKDIR}
cd run_${i}

PYTHONPATH=/home/zhao.1157/fac-master/lib64/python2.3/site-packages
export PYTHONPATH

python fe17_2_hole_total.py
eof
	
	qsub FAC_2_hole_${i}.pbs
	sleep 1
done
