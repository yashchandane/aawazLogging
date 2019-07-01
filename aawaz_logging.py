import pymysql as my
import datetime
import csv
import aawaz_parse
import init
import unzip
from file_logging import logger

# Get data in database
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
    insert_stats_array = []


    play_array_new = []    
    pause_array_new = []
    next_array_new = []
    previous_array_new = []
    fast_fwd_array_new = []
    rewind_array_new = []
    stop_array_new = []
    app_open_array_new = []
    device_detail_array_new = []
    search_array_new = []
    

    # Object for password class
    pass_obj = aawaz_parse.Password()

    # insert data in play table
    def insert_into_play_table(self, play_array, play_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("\nTotal numbers of record to insert in analytics_play table are "+ str(len(play_array)+len(play_array_new)) )
        
        play_sql = "insert into analytics_play( date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"
          
        play_sql_new = "insert into analytics_play( date_time, event_id, user_id, show_id, episode_id, start_time)\
             VALUES(%s, %s, %s, %s, %s, %s);"
        
        self.insert_db(play_sql, play_array, "analytics_play")
        self.insert_db(play_sql_new, play_array_new, "analytics_play_new")

        play_array.clear()
        play_array_new.clear()
        self.db.close()

    # insert data in pause table
    def insert_into_pause_table(self, pause_array, pause_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_pause table are "+ str(len(pause_array)+len(pause_array)) )

        pause_sql = "insert into analytics_pause( date_time, event_id, user_id, show_id, episode_id, pause_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"

        pause_sql_new = "insert into analytics_pause( date_time, event_id, user_id, show_id, episode_id, pause_time)\
             VALUES(%s, %s, %s, %s, %s, %s);"

        self.insert_db(pause_sql, pause_array, "analytics_pause")
        self.insert_db(pause_sql_new, pause_array_new, "analytics_pause_new")

        pause_array.clear()
        pause_array_new.clear()
        self.db.close()


    # insert data in next table    
    def insert_into_next_table(self, next_array, next_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
                
        logger.info("Total numbers of record to insert in analytics_next table are "+ str(len(next_array)+len(next_array_new)) )

        next_sql = "insert into analytics_next(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"

        next_sql_new = "insert into analytics_next(date_time, event_id, user_id, show_id, episode_id, start_time)\
             VALUES(%s, %s, %s, %s, %s, %s);" 

        self.insert_db( next_sql, next_array, "analytics_next" )
        self.insert_db( next_sql_new, next_array_new, "analytics_next_new" )

        next_array.clear()
        next_array_new.clear()
        self.db.close()
    

    # insert data in previous table
    def insert_into_previous_table(self, previous_array, previous_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_previous table are "+ str(len(previous_array)+len(previous_array_new)) ) 

        previous_sql = "insert into analytics_previous(date_time, event_id, user_id, show_id, episode_id, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s);"   

        previous_sql_new = "insert into analytics_previous(date_time, event_id, user_id, show_id, episode_id)\
             VALUES(%s, %s, %s, %s, %s);" 

        self.insert_db(previous_sql, previous_array, "analytics_previous")
        self.insert_db(previous_sql_new, previous_array_new, "analytics_previous")

        previous_array.clear()
        previous_array_new.clear()
        self.db.close()


    # insert data in fast forward table
    def insert_into_ff_table( self, fast_fwd_array, fast_fwd_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_fast_fwd table are "+ str(len( fast_fwd_array )+len( fast_fwd_array_new )) )

        fast_fwd_sql = "insert into analytics_fast_fwd(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);" 

        fast_fwd_sql = "insert into analytics_fast_fwd(date_time, event_id, user_id, show_id, episode_id, start_time)\
             VALUES(%s, %s, %s, %s, %s, %s);" 

        self.insert_db(fast_fwd_sql, fast_fwd_array, "analytics_fast_fwd")
        self.insert_db(fast_fwd_sql, fast_fwd_array, "analytics_fast_fwd")

        fast_fwd_array.clear()
        fast_fwd_array_new.clear()
        self.db.close()


    # insert data in rewind table
    def insert_into_rewind_table(self, rewind_array, rewind_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_rewind table are "+ str(len( rewind_array)+len( rewind_array_new)) )
 
        rewind_sql = "insert into analytics_rewind(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);" 

        rewind_sql = "insert into analytics_rewind(date_time, event_id, user_id, show_id, episode_id, start_time)\
             VALUES(%s, %s, %s, %s, %s, %s);" 
        
        self.insert_db(rewind_sql ,rewind_array ,"analytics_rewind")
        self.insert_db(rewind_sql ,rewind_array ,"analytics_rewind_new")
        
        rewind_array.clear()
        rewind_array_new.clear()
        self.db.close()


    # insert data in stop table
    def insert_into_stop_table(self ,stop_array, stop_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_stop table are "+ str(len(stop_array)+len(stop_array_new)))
  
        stop_sql = "insert into analytics_stop(date_time, event_id, user_id, show_id, episode_id, start_time, app_platform)\
             VALUES(%s, %s, %s, %s, %s, %s, %s);"

        stop_sql_new = "insert into analytics_stop(date_time, event_id, user_id, show_id, episode_id, start_time)\
             VALUES(%s, %s, %s, %s, %s, %s);"
        
        self.insert_db(stop_sql ,stop_array ,"analytics_stop")
        self.insert_db(stop_sql_new ,stop_array_new ,"analytics_stop_new")

        stop_array.clear()
        stop_array_new.clear()
        self.db.close()


    # insert data in app open table
    def insert_into_app_open_table(self, app_open_array, app_open_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_app_open table are "+ str(len(app_open_array)+len(app_open_array_new)))
        
        app_open_sql = "insert into analytics_app_open(date_time, event_id, user_id, app_open, app_platform)\
             VALUES(%s, %s, %s, %s, %s);"

        app_open_sql_new = "insert into analytics_app_open(date_time, event_id, user_id, app_open)\
             VALUES(%s, %s, %s, %s);"
        
        self.insert_db(app_open_sql, app_open_array, "analytics_app_open")
        self.insert_db(app_open_sql_new, app_open_array_new, "analytics_app_open_new")

        app_open_array.clear()
        app_open_array_new.clear()
        self.db.close()


    # insert data in device detail table
    def insert_into_device_detail_table(self, device_detail_array,device_detail_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_device_detail table are "+ str(len(device_detail_array)+len(device_detail_array_new)) )
        
        device_detail_sql = "insert into analytics_device_detail(date_time, event_id, app_id, version_code,\
             version_name, device_name, user_id, board, brand, device, hardware, manufacturer, model, time, sdk_int, \
                 os_built_release_version, app_platform) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        device_detail_sql_new = "insert into analytics_device_detail(date_time, event_id, app_id, version_code,\
             version_name, device_name, user_id, board, brand, device, hardware, manufacturer, model, time, sdk_int, \
                 os_built_release_version) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        
        self.insert_db(device_detail_sql, device_detail_array, "analytics_device_detail")
        self.insert_db(device_detail_sql_new, device_detail_array_new, "analytics_device_detail_new")

        device_detail_array.clear()
        device_detail_array_new.clear()
        self.db.close()


    # insert data in search table
    def insert_into_search_table(self, search_array, search_array_new):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        logger.info("Total numbers of record to insert in analytics_search table are "+ str(len(search_array)+len(search_array_new)) )
        
        search_sql = "insert into analytics_search(date_time, event_id, user_id, query, no_of_show_count, show_ids,\
             no_of_article_count, article_ids, app_platform)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"  

        search_sql_new = "insert into analytics_search(date_time, event_id, user_id, query, no_of_show_count, show_ids,\
             no_of_article_count, article_ids)VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"  
        
        self.insert_db(search_sql, search_array, "analytics_search")
        self.insert_db(search_sql_new, search_array_new, "analytics_search_new")

        search_array.clear()
        search_array_new.clear()
        self.db.close()


    # total data inserted in tables
    def insert_into_insert_stats_table(self, insert_stats_array):
        self.db = my.connect(host = "localhost", user = "root", passwd = str(self.pass_obj), db = "aawaz")
        self.cursor = self.db.cursor()
        
        insert_stats_sql = 'insert into analytics_logging_info(date_time, file_path, event_total_data) VALUES(%s,%s,%s);'
        inserted_row = self.cursor.execute(insert_stats_sql, insert_stats_array)
        
        self.db.commit()
        insert_stats_array.clear()
        self.db.close()

    # Execution and commit of query
    def insert_db(self, sql, data, tableName):
        inserted_rows = self.cursor.executemany(sql, data)
        self.db.commit()
        
    def array_append(self, path):
        
        # Value of each event
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

        # CSV file read and append in array
        with open(path, 'r') as DataCaptured:
            DataCap = csv.reader(DataCaptured, delimiter = '^', skipinitialspace = True)

            for i, line in enumerate(DataCap):
                if(line[1] == NEXT_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.next_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.next_array_new.append(line)
                    
                
                elif(line[1] == PLAY_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.play_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.play_array_new.append(line)
                    
                
                elif(line[1] == PAUSE_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.pause_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.pause_array_new.append(line)
                    

                elif(line[1] == PREVIOUS_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.previous_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.previous_array_new.append(line)
                    
                
                elif(line[1] == FAST_FWD_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.fast_fwd_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.fast_fwd_array_new.append(line)

                
                elif(line[1] == REWIND_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.rewind_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.rewind_array_new.append(line)
                    
                
                elif(line[1] == STOP_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.stop_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.stop_array_new.append(line)
                    
                
                elif(line[1] == APP_OPEN_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.app_open_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.app_open_array_new.append(line)
                    

                elif(line[1] == DEVICE_DETAIL_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.device_detail_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.device_detail_array_new.append(line)
                    
                    
                
                elif(line[1] == SEARCH_ID):
                    if(line[-1]=="play_debug" or line[-1]=="play_release" or line[-1]=="indus_debug" or line[-1]=="indus_release"):
                        self.search_array.append(line)
                    elif(line[-1]=="dev_debug" or line[-1]=="dev_release"):
                        pass
                    elif(line[-1]!="play_debug" or line[-1]!="play_release" or line[-1]!="indus_debug" or line[-1]!="indus_release"):
                        self.search_array_new.append(line)
                    
                else:
                    logger.info("Invalid Input")
        
        total_inserted_data = len(self.play_array) + len(self.pause_array) + len(self.next_array) + len(self.previous_array) + len(self.fast_fwd_array) + len(self.rewind_array) + len(self.stop_array) + len(self.app_open_array) + len(self.device_detail_array) + len(self.search_array) + len(self.play_array_new) + len(self.pause_array_new) + len(self.next_array_new) + len(self.previous_array_new) + len(self.fast_fwd_array_new) + len(self.rewind_array_new) + len(self.stop_array_new) + len(self.app_open_array_new) + len(self.device_detail_array_new) + len(self.search_array_new)

        self.insert_stats_array.append(str(datetime.datetime.now()))
        self.insert_stats_array.append(path)
        self.insert_stats_array.append(total_inserted_data)
        

        logger.info(str(self.insert_stats_array)+"\n")


        # Calling table's function
        self.insert_into_play_table(self.play_array, self.play_array_new)
        
        self.insert_into_pause_table(self.pause_array,self.pause_array_new)
        
        self.insert_into_next_table(self.next_array,self.next_array_new)
        
        self.insert_into_previous_table(self.previous_array, self.previous_array_new)
        
        self.insert_into_ff_table(self.fast_fwd_array, self.fast_fwd_array_new)
         
        self.insert_into_rewind_table(self.rewind_array, self.rewind_array_new)
        
        self.insert_into_stop_table(self.stop_array, self.stop_array_new)
        
        self.insert_into_app_open_table(self.app_open_array, self.app_open_array_new)
        
        self.insert_into_device_detail_table(self.device_detail_array, self.device_detail_array_new)
        
        self.insert_into_search_table(self.search_array, self.search_array_new)

        self.insert_into_insert_stats_table(self.insert_stats_array)