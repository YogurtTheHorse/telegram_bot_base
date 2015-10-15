import ast

from os import listdir
from os.path import isfile, join

def need_import(f):
	return isfile(join('.',f)) and f.endswith('.py') and not f.startswith('__') and f != 'command.py'

def classname(filepath):
	with open(filepath, 'r') as f:
		source = f.read()

	p = ast.parse(source)
	classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
	if len(classes) > 0:
		return classes[0]

files = [ f for f in listdir('.') if need_import(f) ]

output = """# ---------------------------------
# Generated with '__recreate_init.py'
# DON'T TOUCH
# ---------------------------------

"""

classes_list = [ ]

for f in files:
	classes_list.append(classname(f))
	output += 'from commands.{0} import {1}\n'.format(f[:-3], classes_list[-1])

print("Found command files: ", files)
print("Found classes: ", classes_list)

commands_list = '[ '

if len(classes_list) > 0:
	for c in classes_list:
		commands_list += c + '(), '

	commands_list = commands_list[:-2] 

commands_list += ' ]\n'

output += '\ncommands = {0}'.format(commands_list)

with open('__init__.py', 'w') as init_file:
	init_file.write(output)
