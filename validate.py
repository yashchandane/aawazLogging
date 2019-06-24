import os
import sys
import shutil
import stat
import pymysql as my
import aawaz_parse

class Validate:
    def verify(self):
        try:
            self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
            self.cursor = self.db.cursor()
        
            verify_sql = 'use aawaz'
            execution = self.cursor.execute(verify_sql)
        
            self.db.commit()
            self.db.close()
        except:
            print("Wrong Password")
        finally:
            sys.exit()

        if ((sys.argv[1] == "-s" or sys.argv[1] =="--source") and os.path.exists(sys.argv[2]) == True):
            print("Verified Source path\n")
            pass

            if(sys.argv[3] == "-m" or sys.argv[3] =="--move"):
                pass
                print("Verified Move path\n")

                if (os.path.exists(sys.argv[4]) == False):
                    os.mkdir(sys.argv[4])
                    print("New Directory made ==> ", sys.argv[4], "\n")

            elif(sys.argv[3] == "-d" or sys.argv[3] =="--delete"):
                print("Verified Delete path\n")
                pass
                
        else:
            print("Directory does not exist\n")
            sys.exit()


    def move_file(self, source, destination):
        print("Moving files to ==> ", destination,"\n")
        try:
            shutil.move(source, destination)
        except:
            print("Can't move this file\nSimilar name file already exist in the directory")
        

    def delete_file(self, source):
        print("Deleting compressed file ==> ", source,"\n")
        os.chmod(source, stat.S_IRWXU)
        os.remove(source)
        

