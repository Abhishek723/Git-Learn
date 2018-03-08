
import random

chars = '''abcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''
times = int(input('[.]Number of passwords?\n[.]'))
length = int(input('[.]Password length?\n[.]'))

<<<<<<< HEAD
f = open('path/Kanpur','w')
=======

f = open('path/delhi','w')


>>>>>>> 08cc3c972514d3de9bf45371f204ab66a021f901

for i in range(times):
	password = ''
	for j in range(length):
		password += random.choice(chars)

	print('[.]',password,sep='')
