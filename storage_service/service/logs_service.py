from datetime import datetime
import logging

LOGS_FILENAME = '/code/storage_service/db/logs.txt'

def store_logs(message):
    with open(LOGS_FILENAME, 'a') as f:
        try: 
            if f.tell() == 0:
                logging.info('Creating new log file.')
                f.write('transaction log\n')
            else:
                logging.info('A log file was found, appending')

            f.write(message.body.decode('utf-8') + '\n')
        except Exception as e:
            logging.error(e)