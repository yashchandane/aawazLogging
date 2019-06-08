import csv
import pymysql as my
import datetime
import os
from zipfile import ZipFile
import shutil
import sys

class AawazLogging:

    #Array for each Table
    play_array = []    
    pause_array = []
    next_array = []
    previous_array = []
    fast_fwd_array = []
    rewind_array = []
    stop_array = []
    app_open_array = []
    device_detail_array = []
    search_array = []
    insert_stats_array=[]

    #insert data in pause table
    def insert_into_play_table(self, play_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_play table are ", len(play_array) )
        
        play_sql = "insert into analytics_play( date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(play_sql, play_array, "analytics_play")
        play_array.clear()
        self.db.close()

    #insert data in pause table
    def insert_into_pause_table(self, pause_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_pause table are ", len(pause_array) )
        
        pause_sql = "insert into analytics_pause( date_time, event_id, user_id, show_id, episode_id, pause_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(pause_sql, pause_array, "analytics_pause")
        pause_array.clear()
        self.db.close()


    #insert data in next table    
    def insert_into_next_table(self, next_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_next table are ", len(next_array) )
        
        next_sql = "insert into analytics_next(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"  
        
        self.insert_db( next_sql, next_array, "analytics_next" )
        next_array.clear()
        self.db.close()
    

    #insert data in previous table
    def insert_into_previous_table(self, previous_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_previous table are ", len(previous_array) ) 
        
        previous_sql = "insert into analytics_previous(date_time, event_id, user_id, show_id, episode_id, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(previous_sql, previous_array, "analytics_previous")
        previous_array.clear()
        self.db.close()


    #insert data in fast forward table
    def insert_into_ff_table( self, fast_fwd_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_fast_fwd table are ", len( fast_fwd_array ) )
        
        fast_fwd_sql = "insert into analytics_fast_fwd(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(fast_fwd_sql, fast_fwd_array, "analytics_fast_fwd")
        fast_fwd_array.clear()
        self.db.close()


    #insert data in rewind table
    def insert_into_rewind_table(self, rewind_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_rewind table are ", len( rewind_array) )
        
        rewind_sql = "insert into analytics_rewind(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(rewind_sql ,rewind_array ,"analytics_rewind")
        rewind_array.clear()
        self.db.close()


    #insert data in stop table
    def insert_into_stop_table(self ,stop_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_stop table are ", len(stop_array) )
        
        stop_sql = "insert into analytics_stop(date_time, event_id, user_id, show_id, episode_id, time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(stop_sql ,stop_array ,"analytics_stop")
        stop_array.clear()
        self.db.close()


    #insert data in app open table
    def insert_into_app_open_table(self, app_open_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_app_open table are ", len(app_open_array) )
        
        app_open_sql = "insert into analytics_app_open(date_time, event_id, user_id, app_open, app_platform)\
             VALUES(%s, %s, %s, %s, %s);"   
        
        self.insert_db(app_open_sql, app_open_array, "analytics_app_open")
        app_open_array.clear()
        self.db.close()


    #insert data in device detail table
    def insert_into_device_detail_table(self, device_detail_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_device_detail table are ", len(device_detail_array) )
        
        device_detail_sql = "insert into analytics_device_detail(date_time, event_id, appid, version_code,\
             version_name, device_name, user_id, board, brand, device, hardware, manufacturer, model, time, sdk_int, \
                 os_built_release_version, app_platform) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"   
        
        self.insert_db(device_detail_sql, device_detail_array, "analytics_device_detail")
        device_detail_array.clear()
        self.db.close()


    #insert data in search table
    def insert_into_search_table(self, search_array):
        
        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        print("Total numbers of record to insert in analytics_search table are ", len(search_array) )
        
        search_sql = "insert into analytics_search(date_time, event_id, user_id, query, no_of_show_count, show_ids,\
             no_of_article_count, article_ids, app_platform)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"  
        
        self.insert_db(search_sql, search_array, "analytics_search")
        search_array.clear()
        self.db.close()


    #total data inserted in tables
    def insert_into_insert_stats_table(self, insert_stats_array):

        self.db = my.connect(host = "localhost", user = "root", passwd = "root", db = "aawaz")
        self.cursor = self.db.cursor()
        
        insert_stats_sql = 'insert into logging_insert_stats(date_time, file_path, event_total_data) VALUES(%s,%s,%s)'
        inserted_rows = self.cursor.execute(insert_stats_sql, insert_stats_array)
        
        self.db.commit()
        insert_stats_array.clear()
        self.db.close()

    #Execution and commit of query
    def insert_db(self, sql, data, tableName):
        inserted_rows = self.cursor.executemany(sql, data)
        self.db.commit()
        
    def main(self,path):
        
        #Value of each event
        PLATFORM = "android"
        PLAY_ID = "18"
        PAUSE_ID = "20"
        NEXT_ID = "21"
        PREVIOUS_ID = "22"
        FAST_FWD_ID = "23"
        REWIND_ID = "24"
        STOP_ID = "25"
        APP_OPEN_ID = "44"
        DEVICE_DETAIL_ID = "45"
        SEARCH_ID = "40"


        #CSV file read and append in array
        with open(path, 'r') as DataCaptured:
            DataCap = csv.reader(DataCaptured, delimiter = '^', skipinitialspace = True)

            for i, line in enumerate(DataCap):
                if(line[1] == NEXT_ID):
                    self.next_array.append(line)
                
                elif(line[1] == PLAY_ID):
                    self.play_array.append(line)
                
                elif(line[1] == PAUSE_ID):
                    self.pause_array.append(line)
                
                elif(line[1] == PREVIOUS_ID):
                    self.previous_array.append(line)
                
                elif(line[1] == FAST_FWD_ID):
                    self.fast_fwd_array.append(line)
                
                elif(line[1] == REWIND_ID):
                    self.rewind_array.append(line)
                
                elif(line[1] == STOP_ID):
                    self.stop_array.append(line)
                
                elif(line[1] == APP_OPEN_ID):
                    self.app_open_array.append(line)
                
                elif(line[1] == DEVICE_DETAIL_ID):
                    self.device_detail_array.append(line)
                
                elif(line[1] == SEARCH_ID):
                    self.search_array.append(line)
                
                else:
                    print("Invalid Input")
        
        total_inserted_data = len(self.play_array) + len(self.pause_array) + len(self.next_array) + len(self.previous_array) + len(self.fast_fwd_array) + len(self.rewind_array) + len(self.stop_array) + len(self.app_open_array) + len(self.device_detail_array) + len(self.search_array)

        self.insert_stats_array.append(str(datetime.datetime.now()))
        self.insert_stats_array.append(csvpath)
        self.insert_stats_array.append(total_inserted_data)
        
        print(self.insert_stats_array)
        
        #Calling table's function
        self.insert_into_play_table(self.play_array)
        
        self.insert_into_pause_table(self.pause_array)
        
        self.insert_into_next_table(self.next_array)
        
        self.insert_into_previous_table(self.previous_array)
        
        self.insert_into_ff_table(self.fast_fwd_array)
         
        self.insert_into_rewind_table(self.rewind_array)
        
        self.insert_into_stop_table(self.stop_array)
        
        self.insert_into_app_open_table(self.app_open_array)
        
        self.insert_into_device_detail_table(self.device_detail_array)
        
        self.insert_into_search_table(self.search_array)

        self.insert_into_insert_stats_table(self.insert_stats_array)

log_obj = AawazLogging()

#UNZIP FUNCTION
def unzip(source_filename, dest_dir):
    with ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

dirpath = input("Enter directory path")        #ASK USER FOR DIRECTORY
if (os.path.isdir(dirpath) == False):
    print(dirpath + " Directory does not exist.")
    
#GENERATING EXTRACT PATH AND UNZIP CSV FILES
for root, dirs, files in os.walk(dirpath):     
    for file in files:
        
        if file.endswith(".zip"):
            zippath = os.path.join(root, file)
            print("extracting file ", zippath)
            unzip(zippath, os.path.dirname(zippath))
            
            operation = input("Do you want to detete / move file \nPress D/delete to delete and M/move to move directory ? ").strip(" ")
        
            if(operation =="d" or operation =="D" or operation =="delete"):
                print("Deleting compressed file: ", zippath)
                os.remove(zippath)
        
            elif(operation=="m" or operation =="M" or operation =="move"):
                destination = input("Enter destination directory").strip(" ")
        
                if (os.path.isdir(destination) == False):
                    os.mkdir(destination)
            
                move = shutil.move(zippath, destination)
        
            else:
                sys.exit()



#LIST CSV FILES AND APPEND ITS DATA INTO DATABASE
for root, dirs, files in os.walk(dirpath):
    for file in files:
        
        if file.endswith(".csv"):
            csvpath = os.path.join(root, file)
            print("csv path to insert ", csvpath)
            log_obj.main(csvpath)
            
            operationcsv = input("Do you want to detete / move file \nPress D/delete to delete and M/move to move file ? ").strip(" ")

            if(operation =="d" or operation =="D" or operation =="delete"):
                print("Deleting compressed file: ", csvpath)
                os.remove(csvpath)
            
            elif(operation=="m" or operation=="M" or operation =="move"):
                destination_csv = input("Enter destination directory").strip(" ")
                
                if (os.path.isdir(destination_csv) == False):
                    os.mkdir(destination_csv)
                
                move = shutil.move(csvpath, destination_csv)

            else:
                sys.exit()
            