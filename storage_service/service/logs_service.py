from datetime import datetime
import logging

LOGS_FILENAME = '/code/storage_service/db/logs.txt'

def store_logs(message):
    with open(LOGS_FILENAME, 'a') as f:
        try: 
            if f.tell() == 0:
                logging.info('Creating new log file.')
                f.write('correlation_id,change,timestamp\n')
            else:
                logging.info('A log file was found, appending')

            log_string = "{},{},{}\n".format(
                message.correlation_id,
                datetime.now().isoformat(),                                
                message.body.decode('utf-8'),
            )

            f.write(log_string)
        except Exception as e:
            logging.error(e)