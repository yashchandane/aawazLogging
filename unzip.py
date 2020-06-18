import sys
import os
from zipfile import ZipFile
import validate
import aawaz_logging
import stat
from file_logging import logger

#Unzips zip file and move or delete it
class UnzipZip:
    def __init__(self):
        self.log_obj = aawaz_logging.AawazLogging()

    def move_or_delete(self):

        #Generating extract path and unzip csv files
        for root, dirs, files in os.walk(sys.argv[2]):
            for zip in files:
                
                if zip.endswith(".zip"):
                   
                    zippath = os.path.join(root, zip)
                    logger.info("\nExtracting file "+ zippath + "\n")
                    self.unzip(zippath, os.path.dirname(zippath))
                    
                    if(sys.argv[3] == "-m" or sys.argv[3] == "-move"):
                        validate.Validate.move_file(self, zippath, sys.argv[4])

                    elif(sys.argv[3] == "-d" or sys.argv[3] == "-delete"):
                        validate.Validate.delete_file(self, zippath)

        #List csv files and append its data into database
        for root, dirs, files in os.walk(sys.argv[2]):
            for csv in files:
                
                if csv.endswith(".csv"):
                    csvpath = os.path.join(root, csv)
                    self.csvpath = csvpath
                    
                    logger.info("----------------------------------------------------------------------------------------\n")
                    logger.info("CSV path to insert: "+ csvpath + "\n")
                    self.log_obj.array_append(csvpath)

                    if(sys.argv[3] == "-m" or sys.argv[3] == "-move"):
                        validate.Validate.move_file(self, csvpath, sys.argv[4])

                    elif(sys.argv[3] == "-d" or sys.argv[3] == "-delete"):
                        validate.Validate.delete_file(self, csvpath)

    #Unzip function
    def unzip(self, source_filename, dest_dir):
        os.chmod(dest_dir, stat.S_IRWXU)
        with ZipFile(source_filename) as zf:
            zf.extractall(dest_dir)
