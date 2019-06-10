import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

groupSource = parser.add_mutually_exclusive_group(required = True)
groupSource.add_argument("-s", "--source", action="store", default = None, help = "Source directory absolute path")

groupPassword = parser.add_mutually_exclusive_group(required = True)
groupPassword.add_argument("-p", "--password", action="store", default = None, help = "MYSQL database password")

groupMoveOrDelete = parser.add_mutually_exclusive_group(required = True)
groupMoveOrDelete.add_argument("-d", "--delete", action="store", default = None, help = "Delete source files after success")
groupMoveOrDelete.add_argument("-m", "--move", action="store", default = None, help = "Move source files after success")

args = parser.parse_args()
print("args: ", args)

if (args.delete):
    print("delete: ", args.delete)

elif (args.move):
	print("move", args.move)

else:
	print("move or delete required")
	
	
if (args.source):
	print("source", args.source)
	
if (args.password):
	print("password", args.password)
		


