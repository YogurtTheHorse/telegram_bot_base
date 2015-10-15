import os
import os.path

import sys
import string

name = 'Start'
recreate_file = True

if name == '':
	print ('Command name must be not empty')
	sys.exit(1)

if not os.path.isfile('command.py'):
	print ('Base class couldn\'t be found')
	sys.exit(2)

filename = name + '.py'
filename = filename[0].lower() + filename[1:]

for c in string.ascii_uppercase:
	filename = filename.replace(c, '_' + c.lower())

print('Command filename:', filename)
if not recreate_file and os.path.isfile(filename):
	print ("Command file already exists")
	sys.exit(3)

file_content = "from commands.command import Command\n\n"
with open('command.py', 'r') as f:
	file_content += f.read()

file_content = file_content.replace('Command', name).\
	replace('(object)', '({0})'.format('Command')).\
	replace('return [ ]', 'return [ \'{0}\'.lower() ]'.format(filename[:-3].replace('_', '')))

with open(filename, 'w') as f:
	f.write(file_content)

print('Succesfully created file...\nRecreating __init__.py file')

try:
	import __recreate_init # Recreates __init__.py
except:
	print('Couldn\'t create new __init__.py file')
	os.exit(4)