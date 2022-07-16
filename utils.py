import os
log_file_name = os.environ['LOG_FILE_NAME']

def write_log(msg):
    with open(log_file_name, 'a') as f:
        f.write(msg + '\n')
