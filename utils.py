def write_log(msg):
    with open('./cifar-10.txt', 'a') as f:
        f.write(msg)
