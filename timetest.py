import time
    
    
def sleep(num):
    for i in range(num):
        print("\rTime remaining: {} seconds.".format(num - i), end='')
        time.sleep(1)


sleep(100)
