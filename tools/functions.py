import time


def get_current_date():
    return time.strftime('%d_%m_%y-%H_%M_%S', time.localtime())


def get_current_timestamp():
    return time.time()
