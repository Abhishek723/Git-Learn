
import random

chars = '''abcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''
times = int(input('[.]Number of passwords?\n[.]'))
length = int(input('[.]Password length?\n[.]'))


f = open('path/delhi','w')


for i in range(times):
	password = ''
	for j in range(length):
		password += random.choice(chars)

	print('[.]',password,sep='')
