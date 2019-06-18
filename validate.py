import os
import sys
import shutil
import stat

class Validate:

    def verify(self):
        if ((sys.argv[1] == "-s" or sys.argv[1] =="--source") and os.path.exists(sys.argv[2]) == True):
            print("Verified Source\n")
            pass
            if(sys.argv[3] == "-m" or sys.argv[3] =="--move"):
                pass
                print("Verified Move\n")
                if (os.path.exists(sys.argv[4]) == False):
                    os.mkdir(sys.argv[4])
                    print("Directory made\n")
            elif(sys.argv[3] == "-d" or sys.argv[3] =="--delete"):
                print("Verified Delete\n")
                pass
        else:
            print("Directory does not exist\n")
            sys.exit()


    def move_file(self, source, destination):
        print("Moving files to ", destination,"\n")
        try:
            shutil.move(source, destination)
        except:
            print("Can't move file\nSimilar name file already exist in the directory")
        

    def delete_file(self, source):
        print("Deleting compressed file: ", source,"\n")
        os.chmod(source, stat.S_IRWXU)
        os.remove(source)
        

