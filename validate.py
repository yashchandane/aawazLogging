import os
import sys
import shutil
import stat
from file_logging import logger

class Validate:
    def verify(self):

        if ((sys.argv[1] == "-s" or sys.argv[1] =="--source") and os.path.exists(sys.argv[2]) == True):
            logger.info("Verified Source path\n")
            pass

            if(sys.argv[3] == "-m" or sys.argv[3] =="--move"):
                pass
                logger.info("Verified Move path\n")

                if (os.path.exists(sys.argv[4]) == False):
                    os.mkdir(sys.argv[4])
                    logger.info("New Directory made ==> "+ sys.argv[4]+ "\n")

            elif(sys.argv[3] == "-d" or sys.argv[3] =="--delete"):
                logger.info("Verified Delete path\n")
                pass
                
        else:
            logger.info("Directory does not exist\n")
            sys.exit()


    def move_file(self, source, destination):
        logger.info("Moving files to ==> "+ destination+"\n")
        try:
            shutil.move(source, destination)
        except:
            logger.info("Can't move this file\nSimilar name file already exist in the directory\n")
        

    def delete_file(self, source):
        logger.info("Deleting compressed file ==> "+ source +"\n")
        os.chmod(source, stat.S_IRWXU)
        os.remove(source)
        

