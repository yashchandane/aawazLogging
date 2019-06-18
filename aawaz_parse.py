import argparse
import getpass

class Password:
    def __init__(self):
        value = getpass.getpass('Database Password: ')
        self.value = value

        # Parser for commandline input
        parser = argparse.ArgumentParser(description="Enter Command line switch", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        groupSource = parser.add_mutually_exclusive_group(required = True)
        groupSource.add_argument("-s", "--source", action="store", default = None, help = "Source directory absolute path")


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
        
        

    def __str__(self):
        return self.value


        
