from example_cifar_10 import log_file_name
def write_log(msg):
    with open(log_file_name, 'a') as f:
        f.write(msg)
