import time

def time_it(fn):
    def inner_func(*args, **kwargs):
        start = time.time()
        try:
            res = fn(*args, **kwargs)
        finally:
            print(time.time() - start)
        return res

    return inner_func


@time_it
def sleep_func(sec):
    print(f'run with {sec}')
    raise RuntimeError
    time.sleep(sec)
    

def deco(add_param):
    def inner_deco(fn):
        def inner(*args, **kwargs):
            return fn(*args, **kwargs) + add_param
        return inner
    return inner_deco


def time_it_avg(k):
    last_calls = []
    def time_it(fn):
        def inner_func(*args, **kwargs):
            start = time.time()
            try:
                res = fn(*args, **kwargs)
            finally:
                last_time = time.time() - start
                print(last_time)
                last_calls.append(last_time)
                print(sum(last_calls[-k:]) / min(len(last_calls), k))
            return res
    
        return inner_func
    return time_it


@time_it_avg(2)
def sleep_func_1(sec):
    print(f'run with {sec}')
    # raise RuntimeError
    time.sleep(sec)


if __name__ == '__main__':
    sleep_func_1(0.1)
    sleep_func_1(0.5)
    sleep_func_1(1.0)
    