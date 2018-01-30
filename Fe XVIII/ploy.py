#This script is used to plot the photoionization cross section data

import os

#============ INPUT ============
file_xsectn = "XSECTN_total"	#file containing the xsectn data
num_levels = 73	#number of levels for this initial symmetry

#===============================================================================
#================================ BLACK BOX ====================================
#===============================================================================
f = open(file_xsectn, 'r')
os.popen('if [ -f total.ps ]; then rm -rf total.ps; fi')

for level in range(1, 1+num_levels):
	for line in range(41):
		f.readline()
	
	symmetry_level = f.readline().split()
	title_plot = symmetry_level[1]+"\_"+symmetry_level[2]+"\_"+symmetry_level[3]
	
	num_points = int(f.readline().split()[1])
	f.readline()
	
	f_data = open("rm_data", 'w')
	for line in range(num_points):
		f_data.write(f.readline())
		
	f_data.close()
	
	#Now data is extracted for this level, time to plot it
	gnuplot_content = "\
set terminal postscript color enhanced\n\
set out 'tem.ps'\n\
set title \'"+title_plot+"\'\n\
set logscale y\n\
set format y \"%T\"\n\
set ylabel 'log10(PI)'\n\
set xlabel 'Photon Energy (Ry)'\n\
plot 'rm_data' u 1:2 title '200 CC BPRM' with lines lc rgb 'blue'\n\
"
	f_gnuplot = open('plot.plt', 'w')
	f_gnuplot.write(gnuplot_content)
	f_gnuplot.close()
	
	
	os.popen('gnuplot plot.plt && cat tem.ps >> total.ps')
	
os.popen('sleep 5 && open total.ps')	
	
	
	
	
	
	
	
	
	
