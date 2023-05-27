import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        init = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_run = end - init
        print(f"A função '{func.__name__}' levou {time_run} segundos para ser executada.")
        return result
    return wrapper