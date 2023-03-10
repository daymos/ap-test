from datetime import datetime
import logging
import os


def store_logs(message, db_path):
    with open(db_path, 'a') as f:
        if f.tell() == 0:
            logging.info('Creating new log file.')
            f.write('transaction log\n')
        else:
            logging.info('A log file was found, appending')

        f.write(message.body.decode('utf-8') + '\n')