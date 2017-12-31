#! /usr/bin/env python3

f = open('temp')
line = f.readline()
while line:
	print (line, end = '')
	line=f.readline()

print ("==========")

#By comparison, it's easily seen that input() will triger an error when reading nothing.
#to read file using input(), run the copy like ./a.py < input_file
line = input('This line is: ')

while line:
	print (line)
	line = input('This line is: ')


"""


#=======112=======
#This script is to practice os.popen() which invokes a pipe that can be connected with the
#parent pipe.
import os

#This scipt is to pracitce the output of popen.
for line in os.popen('ls -l').readlines()[1:]:
	line = line.split()
	print ('%22s: %s/%04d' % (line[-1], line[-4], int(line[-3])))
	
cat_file = 'temp'
print (os.popen('cat' + ' ' + cat_file).readlines())

#os.system() can also be input data
os.system('cat' + ' ' + cat_file)

print ([os.popen('./test.sh').read()])




#======111=======
#This script is to practice enumerate
f= open ('temp')
#for line_num, line_content in enumerate(open('temp'), 1):
for line_num, line_content in enumerate(f, 1):
	print (line_num, line_content, end = '')



import os
print (os.popen('ls -a').readlines())




#=======110========
#This scritp is to practice constructing dictionary with zip
keys = [2, 3, 4]
values = ["2", '3', '4']

a = dict(zip(keys, values))
print (a)

b = {i: j for (i, j) in zip(keys, values)}
print (b)

#c[i]=j so c should be predefined.
c={}
for i, j in zip(keys, values): c[i] = j
print (c)






#======109======
#This script is to practice zip
a = [2, 3, 4, 5]
b = (23, 23, 4)

for i, j in zip(a, b):
	#print (i, "+", j, "=", i+j)
	print ('%d+%d=%d'%(i, j, i+j))




#=======108=======
#This script is to practice range/len combination in for loop
a = [2, 3, 4]
show = input('show the updated results(y/n)?: ')

for i in range(len(a)):
	a[i] += 1
else:
	if show.lower() == 'y':
		for i in range(len(a)):
			print (a[i])




#=======107=======
#This script is to practice rstrip()
for line in open('temp'):
	print (list(line.rstrip()))
	for cha in line.rstrip():
		print (cha, '.')
		#if not cha: print ('break'); break

i=0
for line in open('temp'):
	i += 1
	if i == 4: break
else:
	print ('temp has less than 4 lines')

f = open('temp')
while True:
	line = f.readline().rstrip()
	print (list(line.rstrip()))
	if not line: break
f.close()

if '\n'.rstrip: print ('not empty')





#==========106========
#This script is to practice nested loop
a = ['I', 'love', 'you']
test = ('YOU', "lovde")

for i in test:
	for key in a:
		if i.lower() == key.lower():
			print ("found")
			break
	else:
		print ("not found")





#=======105========
#This script is to practice for loop in a dictionary
#for loop iterates through any sequence and also dictionary and files.
#However in dictionary, only keys are iterated.
for key in {"name": "seth", "age": 27, "position": "student"}:
	print (key)



#=======104======
#This script is to practice loop else
a = 'I love you'

while a:
	if a[0] == 'o': print ('found'); break
	a=a[1:]
else:
	print ('Not found')




#======103=======
#This script is to practice testing prime numbers
while True:	
	test_num = input ("enter the number: ")
	if test_num.lower() == "stop": break
	
	test_num = int(test_num)
	factor = test_num // 2
	while factor > 1:
		if test_num % factor == 0:
			print (test_num, " is not a prime number.", sep = "")
			break
		factor -= 1
	else:
		print (test_num, " is a prime number.", sep = "")




#========102=======
#This script is to practice while loop
while True:
	name = input("Enter your name: ")
	if name.lower() == "stop": break
	age = input("Enter your age: ")
	if age.lower() == "stop": break
	print ("Hello ", name, "! You are ", age, " years old.", sep = "")
	
	


#======101========
#This script it to pracetice loop else, which is only executed when no break statement in
#the loop is encountered.
a = [2, 3, 4]
i=1
while a:
	a=a[1:]
	i += 1
	#if i == 2: break
else:
	print ('This is loop else')



#=======100========
#This script is to practice pass and continue
a=3
while a > 1:
	#pass	#pass does NOTHING at all, but is it useful?
	continue
	print ('After pass') 
	a -= 1



#======99=======
#This script is to simulate do-until loop
a=3
while True:
	print ("%d"%(a-32))
	if a ==3: break



#========98=========
#This script is to practice while loop 
a=0; b = 9

while a<b:
	print (a, end = "|")
	a+=2




#========97=======
#This script is to practice while loop with testing an object empty or not
#As long as the object is non-empty string or non-zero number, it's true.
a = "I love you"
while a:
	print (a, 1, sep="|", end = "||")
	a=a[1:]




#========96=========
#This script is to practice while loop
true=''
while true:
	print ('love', ' ', 'Or press Ctrl+C to terminate it')




#=======95=======
#This script is to practice continue
j = 3

for i in range(9):
	if i >= j:
		continue
	print ("i = ", i)




#=========94========
#This script is to practice writing the shell script in one line.
import os

os.system('touch test; if [ -f test ]; then echo "test exists. Deleting."; fi; rm test; ls')




#=======93========
#This script is to test spaces and tabs
if 2 > 1:
	print ('first')
	print ('second')




#=======92=======
if 4 > 32:
	(print 
	("no"))	#This is to test the continuation, \, {}, (), []
else:
		print ("yes")
	print ("??")	#Has to be matched by the previous indentation level.





#========91========
#This script is to practice else if
if 2 > 2:
	print ("no")
elif 3>2:
		print ("Yes, use elif, not else if")



#========90========
#This script is to practice input from the command line
a = input()
while (a):
	print (a)
	a = input()
print (a)




#========89========
#This script is to practice while loop to read from stdin
while not 0:
	input_str = input('Enter: ')
	if input_str.lower() == 'stop': break
	
	if not input_str.isdigit():
		print ('BAD!'*3)
	else:
		print (float(input_str)**2)
	print (input_str.upper())
	
	try:
		a = int(float(input_str))
	except:
		print ("Bad!" * 8)
	else:
		print (a**2)





#========88========
#This script is to test some syntax in python 2.X
import numpy as np
for line in open('temp'):
	#print '{:s}'.format(line)
	line_split = line.split()
	print float(line_split[1])
	print list(np.linspace(float(line_split[0]), float(line_split[1]), 20, endpoint = False))



#=======87======
#This script is to practice f.write() which does not generate '\n' automatically
f = open('temp', 'w')

f.write(str(2)+' ')
f.write('%.4E\n'%2.343)
f.write('{0:.4e}\n'.format(23.23))

f.close()





#=======86=======
import numpy as np

arr = np.linspace(2, 3, 23, endpoint = False) +1

print (arr[1])




#=========85==========
#This is to test the reference in a function
def test_f(a):
	a[0] = 'CHANGED'

b = [2, 3, 4]

test_f(b)
print (b)	#it turns out pass by reference

test_f(b[1:])
print (b)




#=========84========
#This is to practice pickle module which deals with binary file, not text file
l = [2, 3, 4, "This is a list"]

f = open('temp.txt', 'wb')

import pickle 
pickle.dump(l, f)
f.close()




#=======83=======
#This is to practice eval()
sd = "this is a string"

sd_copy = eval('sd')

print (sd_copy)

a = eval('23')
print (a)

b = eval('print ("I love you")')

print ('{0[name]}'.format({"name": "zhao"}))

#This execute the expression in ''
eval ('print ("{0[name]}".format({"name": "zhao"}))')





#======82======
#This script is to practice file operation

f = open('temp.txt')	#by default, the accessing mode is 'r'

#Since file has an iterator in itself, so we can just use it, not its method.
for i in f:
	print (i)	#Here since each line has '\n', and print by default ends with 
						#'\n', so we need to deactivate it by end = ''

f.close()

f = open ('temp.txt')

a = f.read()
print (a)
f.close()

f = open('temp.txt')
a = f.read(3)
print (a)

a = f.read(3)
print (a)

a = f.read(300)	# only terminated by the number of characters or the end of the file, NOT
				#the end of the line.
print (a)
print ("***")
a = f.readline()	#readline() terminates at '\n'
print (a)
f.close()
#This is to test writelines()
line = ['line 1\n', 'Can not be non-string type 23'+' cat\n', 'line3\n']
f = open('text', 'w')
f.writelines(line)
f.close()

f = open('text')
print (f.read())
f.close()

#This is practice seek() method
f = open('text')
f.seek(7)
print (f.readline())
f.seek(2,1)		#Not work well for 1 and 2.
print (f.readline())




#==========81==========
#This is to test the difference between tuple and dictionary
t = ('zhao', 27, ['physicist', 'CEO'])

for i in t:
	print (i)

from collections import namedtuple

PERSON = namedtuple('PERSON_TYPE', 'name age jobs')

me = PERSON('ZHAO', 27, ['PHYSICIST', 'CEO'])
 
#namedtuple has the method .index() and .count()
for i in me:
	print (i, me.index(i), me.count(i))

me_dict = me._asdict()
for i in me_dict:
	print (i, me_dict[i])

#This is to test the unpacking assignment

my_name, my_age, my_jobs = me
print (my_age, my_name, my_jobs)





#======80=====
#This is to test the file pointer when defined in a funciton and accessed again outside.
def tes():
	f = open('temp.txt', 'w')
	f.write('This is in function tes()\n')

tes()
f.write('This is after calling the tes() function\n')



#========79========
#This is to test the scope of variables in a function
def tes(a):
	print (a)
	a[1] = 23
	del a
	#print (a)

a = [2, 3]
b = 0
tes(b)

print (a)




#==========78=========
#This script is to practice write()
def write_to (f_w, a):
	for i in range(len(a)):
		f_w.write('{} '.format(a[i]))
	f_w.write('\n')
	
f = open('temp.txt', 'w')
a = [2, 3, "this is a test"]

write_to(f, a)

f.close()





#=======77=======
#This script is to practice the index in a for loop
for i in range(4):
	print (i)

print (i+1, i+2)





#=======76======
#This script is to practice linspace and addition to a number
import numpy as np

a = np.linspace(2, 4, 6, endpoint = False)

print (a[1:])
print (a+22)

#For list, "+" means 
b = [2, 3]
print (b+2)




#=======75=======
#This script is to practice System.Exit()
import sys 
for i in range(4):
	if i >1:
		#raise SystemExit()
		sys.exit()
	print (i)




#===========74============
#This script is to verify that "\" is still used to be the indicator that the next line
#is the continuation of the line before.
print ("love", \
"you\n")





#========73=========
#This script is to practice lambda operator and map() function
a = list( map(lambda x, y : x/10 + y, range(4), [1]*4) )

print (a)

#To generate a uniform range for float numbers, we can use lambda operator and map()
#function
b = list( map(lambda x : x/10, range(2, 9)) )

print (b)






#=========72=========
#This script is to practice assigning a dict to another variable
#Just like simple variables, large dictionary or list can be assigned to other variable.
d = {(2, 3, 4): 'element', 2:[2, 3, 4]}

dd = {}

dd[(1990, 4, 2)] = d

print (dd[(1990, 4, 2)][(2, 3, 4)])

print (dd[1990, 4, 2][2][2])



#========71=========
#This script is to practice try except statements in the case where the key is not in the 
#dictionary. 
d = {'name': 'zhao'}

#KeyError is invoked whenever
try:
	a = d['name ']
except KeyError:
	a = 2

print (a)





#========70========
#How dictionary is important? The following example maps the release year to the movie,
#so just like in many websites, you might need to choose the year so that a certain moves
#can show up for you to choose from.
d = {1970: 'xmen_1',
	 1999: ['xmen_2', 'fall in love']}

print (d[1999][:])





#======69=======
d = {'a':1, "b": '1', 2:1, '34':23}

for (key, value) in d.items():
	if value == 1:
		print ((key, value), key, value)

for key in d.keys():
	if d[key] == '1':
		print ((key,d[key]))

collect = [key for (key, value) in d.items() if value == 1]

for i in collect:
	print ('The keys are', i)




#======68======
#This script is to practice dict update() method
key_2 = 'sd'
key_list = ['key_1', key_2]
value_list = [2, 3]

d = dict (zip(key_list, value_list))

print ('{}'.format(d))

key_list = ['key_1', 'key_2']
value_list = [223, 3]

c = dict(zip(key_list, value_list))
d.update(c)
print ('{0}'. format(d))




#==========67==========
#This script is to practice dictionary
info = {'me': {'f_n': 'seth', 'l_n': 'zhao', 'age':27, 'hobbies': ['sports', {'reading': 2}]},
		'he': {'f_n':'eugena', 'l_n': 'feng', 'age':29}}

print (info['me']['age'], info['he']['age'])
print (info['me']['hobbies'][1]['reading'])




#=========66==========
#This script is to practice sort() method in list
l = ['A', 'a', 'A', 'B', 'b']

l.sort(key=str.upper, reverse=True)
print (l)

l = ['A', 'a', 'A', 'B', 'b']
l.sort()	#No argument
print (l)

l = [3, 'a', 5, 'B', 'b']
l.reverse()	#No argument
print (l)





#=========65=========
#Another way of finding the offsets of a value in a list. This is much simpler than the 
#previous one, so we make a copy of the original list and assign the element that's the
#value to a different value, so easier.

l = [3, 2, 3, 2, 4, 2, 2]

l_copy = l.copy()	#to avoid destroying the original one, we need to make a copy by its			
					#method copy() instead of assignment.
#l_copy	= l	#what this is actually doing is assigning the same pointer to the object to
			#the new variable or name.

for i in range (0, l.count(2)):
	ind = l_copy.index(2)
	print (ind, end = ' ')
	l_copy[ind] = 'NONE'

print (end = '\n')
print (l, l_copy)





#=====64=======
#Find all the offsets of a value in a list
l = [3, 2, 3, 2, 4, 2, 2]
print ("There are " + str(l.count(2)), "2's")

temp = l.copy()
j = len(temp)

collect_index = []

while (j > 0):
	ind = temp.index(2)
	print (ind)
	collect_index += [ind]
	
	temp = temp [ind+1:]
	print (temp)
	j = len(temp)

print (collect_index)
	
print (collect_index[0], end = ' * ')

s = collect_index[0]

for i in collect_index[1:]:
	s += (i+1)
	print (s, end = " * ")




#=====63======
#This script is to test whether '\n' is in the element when transformed into a list.
filename = 'a62'
mode = 'r'

f = open(filename, mode)
line = f.readline()
line = line.split()

print (line[2], line[0])
line[2] = int(line[2]) + 3

print (line[2])
print (f.read())	#Here you see the control is not at the beginning, so it reads the rest.
f.close()
import os
os.system('clear')

#new purpose
f = open(filename, mode)
num_line = len( f.readlines() )
f.close()
print (num_line)

if num_line % 2 == 0:
	iteration = int(num_line/2)
else:
	iteration = int(num_line/2) + 1

print (iteration)
os.system('clear')

#Start the real purpose
f = open(filename, mode)
if num_line % 2 == 0:
	for i in range (1, iteration+1):
		g = []
		for j in range (1, 3):
			line = f.readline()
			line = line.split()
			g += [float(line[2])]
		print (g)	
else:
	for i in range (1, iteration):
		g = []
		for j in range (1, 3):
			line = f.readline()
			line = line.split()
			g += [float(line[2])	]		
		print (g)
	g = []
	for j in range (2*(iteration-1)+1, num_line+1):
		line = f.readline()
		line = line.split()
		g += [float(line[2])]		
	print (g)





#=====62=======
#This script is to practice read a file into one single string, and split it into lines
filename = 'a62'
mode = 'w'

f = open(filename, mode)
for i in range (1, 10, 2):
	f.write('{0}^2 = {1}\n'.format(i, i**2))

f.close()

mode = 'r'
f = open(filename, mode)

lines = f.read().split('\n')

print (lines, len(lines))




#======61======
#This script is to practice writing to and reading from a file
import numpy as np

filename = 'a61'
mode = 'w'

f = open(filename, mode)
f.write('line 1\nline 2\nline 3\n')

for i in np.linspace(1, 10, 10):
	f.write('{0:6.1f} {1:5d} {2:5d}\n'.format(int(i), int(i**2), int(i**3)))

f.close()
	
mode = 'r'
f=open(filename, mode)
#How to find the number of lines in a file? Use readlines() function which read each line
#into an element of a list, which can be found the number of elements in it by len(). But
#the cors
num_line = len(f.readlines())
f.close()

f=open(filename, mode)
for i in range(1, num_line+1):
	#Before reaching to the desired position, the control just moves, which is the way
	#I found to move the control the desired position.
	line = f.readline()	#Each line read into a string, so in order to access each field,
						#we need to split the into a list, which enables a element access.
	
	if i>=4:
		a=line.split()
		print (a[0], float(a[0])/2, end = ' >>\n')
		




#======60=======
#This script is to practice os module which can call operating system dependent functions
#Looks like this is going to be a very useful module which contains function system().
import os
os.system("if [ ! -d new ]; then echo not exists; mkdir new; fi")

print ("****\nStart sleeping for 2 seconds")
os.system("sleep 2")	
print ("Finished sleeping for 2 seconds\n****")

os.system("ls; rmdir new")




#=====59======
#This script is to practice python command line arguments using sys and argv
##The arguments passed from the command line are strings, so it's not good for list.
#import sys 
#print (sys.argv[0], sys.argv[1][1])

#By importing this script, we can use this function with arguments passed into it.
print ("We are going to call function test_func()")
def test_func (ml):
	#this is the document of this function
	print ("This is the subscript!")
	print (ml[0], ml[1], ml[2], ml[3][1])



#========58========
import numpy as np

print (np. space(2, 33,3 ))



#======57======
#This script is to practice unpacking key-value pairs in dictionary
d = {'name': 'zhao', 'age': 27}
dd = {'add': 'china', 'ress': 'usa'}
print ( '{name}, {add}, {0}'.format(2, **d, **dd) )



#======56=======
#This script is to practice formatting parameters in formatted method.
print ( '%-0*.*f'%(9, 2, 2.348) )

print ( '{1:^0{2}.{0}f}'.format(2, 2.348, 9) )




#=====55======
#This script is to practice the positions of other variables when a former variable is
#expanded.
d = {'name': 'zhao', 'age': 27}
l = [2, 3, 'hello']
print ('{0}_{2}, {1}_{4}, {2}_{4}_{3}'.format(*d, *l))





#=====54=====
#This script is to practice mixing positional, key-indexed and dict variables in formatted
#expression.
d = {'name': 'zhao', 'age': 27}
a = 'hello'
date_1 = 'July 8th'
#remember when [] is needed, when it's not.
print ( '{0}, {1[age]}, {date}'.format( a, d, date = date_1 ) )




#======53======
#This script is to practice advanced formatting method: >(right-alignment), <(left-alignment)
#^(middle-alignment)
print ('{0:o^+9.2f}'.format(2.348))




#=====52======
#This script is to practice unpacking sequence in format
l = [2, 3909, 4]

print ('%+0*.*f'%(9, 2, 2.3))
print ('{2}_{3[1]}'.format(*l, l))	#one is unpacked and the other is a whole.

print ('{0[1]:*^9d}'.format(l))




#=====51=====
#This program is to practice dictionary in formatting
s = {'name': 'zhao', 'age': 27}
age = 278
name = 'zhao'

print ( '{2[name]}>>{2[age]}, {name}_{age}_{1}_{0}'.format('love', 'you', s, age=age, name=name) )





#======50======
#This script is to practice format strings which can name object attributes and keys
l = [2, 'love_you']
t = (23, 'Jingjing_Feng')
d = {'name': 'zhao', 'age':27}
s = {2, 3, 'love'}
print (l[1].split('_'))

print ( '{2[name]:4.2s}, {2[age]:+09d}, {0[1]}, {0[0]}***{1[1][8]}'.format(l, t, d) )
import sys 
print ( '{0.platform}'.format(sys) )

print ('{0}, {1}'.format(*l))	#Here *l means unpacking l
print ('{}, {}'.format(*t))
print ('{0}: {2[name]} *** {1}: {2[age]}'.format(*d, d))
print ('{0}, {1}, {2}'.format(*s))




#======49======
#This script is to practice something fun
M = 8
a = {}

for i in range(M):
	#This formatted string can used as a key or a value assigned to a key of a dictionary.
	a['{}'.format(i*'_')]= '{}'.format((M-i)*'*') 
	
for i in range(M):
	print (a['{}'.format(i*'_')])



#=====48======
#This script is to practice mixing positional variables and key-value pairs in string
#formatting expression
a = 27
#You can not put dictionary variable in the method format() as an argument, you have to 
#expand it following the positional variables.
age = 2
#formatting method is the way to mix variables and keys. It can not be done with %
print ('{name}:{0} {age}: {1}'.format(a, 'love', age= 27, name = 'seth'))	#scope of age

print (age)




#====47======
#This script is to practice dictionary-based formatting expression
d = {'name': 'zhao', 'age': 27}
print ('%(name)s\'s age is %(age)d'%d)





#=====46======
#This script is to practice undetermined width and precision
width = 19
pre = 1
a = 23.32343
print ('%+0*.*g'%(width, pre, a))




#=======45=======
#This script is to practice find all the occurances of a substring in a string using
#find method
a = 'I lovsdf 9o soe you!'

print ( a.find('!', 0, len(a)) )

match = 'o'
i = 0	#initialize the index from the start.

while i != len(a):
	i = a.find(match, i, len(a))
	if i < 0:
		i = len(a)+i
	else:
		print (i, end = ' ')
	i = i+1
	



#=====44======
#This script is to practice an application of slicing
import sys
print (sys.argv[1:])



#=====43=======
#This script is to practice in for-loop
a = 'I love you!'

for ch in a:
	print (ch, end = '\v')



#======42======
#This script is to practice end in print
for i in range(2, 9):
	print ([i, i*i], end = ' ')	#without end, each print starts a new line.



#======41======
#This script is to practice something fun
n = 43
s = 'I love you! Do you love me?'
for i in range(1, len(s)):
	print (s[:-i]+'_'*n+s[len(s)-i:])




#=====40======
#This script is to practice triple double-quotes
print (
''' love		#Notice, never put comments between triple quotes.
  lsdf 
sdf '''
)




#=======39======
#This script is to practice raw string in opening a file
f = open('../text', 'w')
f.write('love you forever!\nMe too\n')
f.close()
f = open('../text', 'w')
f.write('')
f.close()



#======38=======
#This script is to practice variables, objects and their associative linking
a = [2, 3, 4]
b = [2, 3, 4]
c = b
d = b 

print (b is d, b is c, c is d)
import sys
print ( sys.getrefcount('[2, 3, 4]') )

#This example demonstrates that a and b point to the same object, so when one variable
#modifies the object, the value returned by another variable updates the modifications.
a = ['hihlove']
b = a
b[0] = 2
#c = b.replace('h', 'H', 1)
print (a, b)




#=====37======
#This script is to practice True and False values in boolean
print ((True, False), True*3+32, False-3)
print (True * 3 - False -39)




#=====36=====
#This script is to practice operation on sets
s = {2, 3, 4, 5, 6}
ss = set(range(4))
print (s, ss)
print (s&ss)
print (s^ss)
print (s-ss == s-(s&ss))
print (ss > s&ss < s, s < s|ss > ss, s|ss == s&ss | s^ss)


#====35======
#This script is to practice F=Gm7m8/r^2 and set comparison
l1 = [2, 3, 4]
l2 = [3, 4, 2]
print (l1==l2)	#relative position matters
print (set(l1) == set(l2))	#relative position is not mattering
print (sorted(l1) == sorted(l2))
l1.sort()
print (l1)


#====34=====
#This script is to practice transforming a list into a set
x='hisd'
l = [2, 3, 'h', 'h', x]
print (l)
print ('easy way>>>')

s = set(l)
print (s)

print ('use set comprehension')
sc = {(l[i], i) for i in range(len(l))}	#the expression can not be in list or set type.
										#they are unhashable (mutable)
print (sc)

sc.add(('xx', 23))
print (sc)





#=====33========
#This script is to practice Fraction()
from fractions import Fraction
a = Fraction(2, 3)
b = Fraction('2.3')

print (a, b, a*b, a-b, a**b, Fraction(str(a**b)))
print (Fraction('2/3'))

a = Fraction(1, 10)
b = Fraction(1, 10)
c = Fraction(1, 10)
d = Fraction(3, 10)

print (a + b + c - d)



#======32=======
#This script is to practice decimal type which is fixed-precision
print (0.1*3-0.3, '||', 0.1+0.1+0.1-0.3)
from decimal import Decimal
a=b=c='0.1'
d = '0.3'
e = Decimal(a) + Decimal(b) + Decimal(c) - Decimal(0.3)
print (e)
print (Decimal(a) + Decimal(b) + Decimal(c) - Decimal(d))




#=====31=====
#This script is to practice random.choice() and random.shuffle()
#random.choice() depends on the relative position, so dictionary and sets are not
#supported; random.shuffle() requires the mutability and positional indexing of the type.
l = [2, 3, 'hi']
t = (2, 3, 'hi')
s = {2, 3, 4}

import random
print ( random.choice(l) )
print ( random.choice(t) )

l_a = l + ['xx']
print ( random.shuffle(l_a) )
print (l_a)

G = ( (i, l_a) for i in range(4) )

for i in [2, 3, 4, 'hi']:
	print (next(G))
	random.shuffle(l_a)	#this still affects the 


#=====30=====
#This program is to practice using set to remove duplicates in list
a = [2, 3, 2, 2, 3]

a = list(set(a))
print (a)

print (set([2, 2, 3]))




#=====29======
a = 1
if a == 1:
	print ('large')




#====28====
#This script is to practice writing a file
f = open('temp.txt', 'w')
f.write('I love you\n')
f.write('I LVOE YOU TOO')
f.close()

f = open('temp.txt', 'r')
text = f.read()
print (text)

line = text.split('\n')

print (line)



#====27======
#Both list and tuple have methods like index() and count()
t = (2, 3, 2, 2, 'hi', 'hi')
print ('{}_{}\n{}_{}'.format(t.index(2), t.count(2), t.index('hi'), t.count('hi')))

print (t[0:-2])
#t[0] = 2	#tuple is immutable, so once created, it can not be modified.




#======26======
#This script is to practice changing list
l = []
for i in range(30):
	l.append(i**2)

print (l)

l = [i*2 for i in range(30)]
print (l)

G = (i for i in range(30))
for i in range(30):
	print (next(G))



#====25====
#This script is to practice in
a = 'ab234'
j=1
for i in a:
	print (i*j)
	j=j+1




#=====24=====
#This script is to practice sorted()
l = ['a', 'c', '2', '9']

print (sorted(l), l)
a=''
for i in sorted(l):
	a += i	#concatenation
print (a)




#=====23=====
#This script is to practice keys()
l = [1, 2, 'love']
#print (l.keys())	#It turns out there is no keys() method for list
D = {'love':0, 'author':1}
keys = list(D.keys())

for key in keys:
	print (key+'_'+'{}'.format(len(key)))




#=======22======
#This script is to practice sorted dictionary using for loop
index_0 = 'title'
value_0 = 'love'

index_1 = 'date'
value_1 = '2017/06/29'

index_2 = 'author'
value_2 = 'seth'
D = dict(zip([index_0, index_1, index_2], [value_0, value_1, value_2]))

print (D)
sorted(D)
print (D)
print (sorted(D))

for key in sorted(D):
	print (key+'>>'+D[key])




#=====21=======
#This script is to practice for loop
for i in range(3):
	print ({i, i**2})
	print ()	




#=====20======
#This script is to practice missing keys 
a = {'title':'love'}

print ('f' in a)
if not 'f' in a:
	print ('\'f\' is not an index of a')
	print (list(a.keys()))



#=====19======
#This script is to practice nesting dictionary
D = {'name':{'first':'seth', 'last':'zhao'},
	 'visit': ['China', 'USA']}

print (D['visit'][-2][1:-1])
D['visit'][0] = D['visit'][0].upper()
D['visit'][1] = D['visit'][1].lower()

print (D)
print('The first name is'+' '+D['name']['first'], '\nThe last name is'+' '+D['name']['last'])
print ('He visited '+D['visit'][0]+' and '+D['visit'][1])

print (sum({1, 2, 3}))
a = {'x':1, 'y':3}
#print (sum(a))	#No this is not valid.



#=====18======
#This script is to practice deleting an index in a dictionary
D = {'name': 'seth', 'age': 27, 'nationality':'china'}
print (D)
del(D['name'])
print (D)




#=====17======
#This script is to test list operations
l = [1, 2, 'live', 'you!']
print (l, l[-1]+l[-1][1:-1])
print (l[3:][0][-3:-1])

print (l)
del(l[0])
print (l)




#=====16=====
#This script is to practice defining dictionary
index_0 = 'name'
value_0 = 'seth'

index_1 = 'age'
value_1 = 27

index_2 = 'nationality'
value_2 = 'China'

print ('The first way of defining a dictonary')
person = {index_0:value_0, index_1: value_1, index_2:value_2}
print (person, '>>>>'+index_0+':'+ person[index_0])

print ('The second way of defining a dictonary')
person_1 = {}
person_1[index_0] = value_0
person_1[index_1] = value_1
person_1[index_2] = value_2

print (person_1[index_0]+'>>>'+person_1[index_2]+'>>>', person_1[index_1])

print ('The third way of defining a dictionary')
person_2 = dict( zip([index_0, index_1, index_2], [value_0, value_1, value_2]) )
print (person_2[index_2])

print ('The fourth way of defining a dictionary')
person_3 = dict(index_0=value_0)
print (person_3)




#=====15======
#This script is to practice dictionary
Seth = {}
Seth['age'] = 27
Seth['height'] = 180.2
print ('age: {1:+04d}, height: {0:+08.2f}'.format(Seth['height'], Seth['age']))
print ('The basic information of Seth is :', Seth)




#======14======
#This script is to practice set
a = {-21, 3, 2, 'hi'}	#set

print (a)

a = [1, 1, 3]
print ( { i:a[i] for i in range(3) } ) #dictionary




#======13======
#This script is to practice generator by comprehension included in parenthesis
complementary = ['cute', 'lovely', 'beautiful']
G = ( complementary[i] for i in list(range(len(complementary))) )

print ('You are', next(G), '!')
print ('You are', next(G), '!')
print ('You are', next(G), '!')

a = [[1, 2] ,[ 3, 4, 5]]

SUM_a = ([len(row), sum(row)] for row in a) 
print ( next (SUM_a) )
print ( next (SUM_a) )
#print ( next (SUM_a) )	#it's stopped



#=====12======
#This script is to practice sum on strings, which turns out to be invalid.
a = [[1, 2, 3, 4],	#Here you can not include another list of numbers, only numbers in the
	 [2, 3, 4, 5]]   #outer-most list.
print ([[len(row), sum(row), sum(row)/len(row)] for row in a if row[0] > 1])




#=====11======
#This script is to practice list comprehension
a = [ 2, '23', 'love', ['xjl', 2] ]
print (list(range(len(a))))
print ( [a[i]*2 for i in list(range(len(a)))] )

print ( [1 for i in [1, 2 ,3]] )
#del(a[0])
a.pop(0)
print ([ row[0] for row in a])

a.remove('23')
print (a)
del(a)
#print (a)	#delete the whole list


#======10======
#This script is to practice list comprehension
#a = ['2', 2, 2.34, 'love you', ['xx', '99']]
x = 'x'; y = 'y'; z = 'z'
a = [ [1, 2, 3], ['a', 'b', 'c'], [x, y, z]]
index = 2
print ([ [index, a[index][1]] for index in list(range(len(a))) ])
print ( 'len(a) is', len(a) )

print(list(range(2, 3)))

a = ['2''love you', ['xx', '99']]
print ([row[1] for row in a])	#if row is a string, then row[1] means the second character
								#if row is a list, then row[1] means the second element.
print (a[0])

a = [[i, i*i] for i in list(range(1, 4))]

print ('List of a is', a)



#=====9=======
#This script is to practice nesting list
l = [['I', 'L', 'U'], [5, 2, 0]]

print (l[1][0], l[1][1], l[1][2])




#=====8=======
#This script is to practice list operations
l = [1, 2, 1, '1', '2']
l.remove(1)
print (l)
l.remove(1)
print (l)
l.insert(0, ['x', 23])
print (l)
#l.extend (['xds', 23, 'love'])
l.append(['xds', 23, 'love'])
print (l)

l = [1, '2.3', 'love', 2.34e-7]
print (l[0], l[1], '\n', "This is a sub-list:", l[:-1], '\n', l[:-2]+['x'], '\n', l[1][2])

l.append(['xx', 'x'])
print (l[4][0], l[4][1])
l.pop(4)
print (l)

l = ['aa', 'bc', '2']
l.sort()
print (l)
l.reverse()
print (l)
del(l[2])
print (l[1])



#========7=======
#This script is to practice triple quotes
#It turns out only works well in interactive mode.





#====6======
#This script is to practice advanced formatting
name = 'Mum'
person = 'you'
print ('{1}, do you know how much I love {0}?'.format(person, name))

#+ means sign should be shown if it's positive, 0 means the space not filled should be 0.
#23 means the minimum number of space, ',' is the separator of 3 digits, .2 means 2 
#decimal places, G/g means scientific or non-scientific notation whichever is shorter.
print ('{:+023,.4G}'.format(-2234324.3423))






#=====5======
#This script is to practice rstrip() and lstrip()
a='  sd sd  '
a=a.rstrip()	
a=a.lstrip()
print (a+"xx")

a='ASB'
print(a[1:2].lower())




#=====4======
#This script is to practice isalpha() and isdigit()
a='dsd2d'

print (a.isalpha())

a=234	#isdigit() is a method in string class, so int object does not have this method
a='234d'
print (a.isdigit())


#======3=======
a = 'I,love,you'
l_a = a.split(',')

print (a[:4].upper(), ',', a[2].upper()+'_'+a[4].upper())

print ('"ov" is at position', a.find('ov'), ', \'ou\' is at position', a.find('ou'))
print ('Replace "o" with "O".', a.replace('o', 'O', 2))

print ('>>>')
print ('This is: ', l_a[0], '\n',l_a[1], '\n', l_a[2], '\0')


#======2======
a = len(str(2**3000))

print (a)

print(3.14*3)


#========1======
print ('hi')
print ("HI")
"""
