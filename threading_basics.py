import threading
import time


def func():
    print("action #1 in progress")
    time.sleep(3)
    print("action #1 done")


""" 
target takes function name as a variable;
args is an optinal parameter and is used to pass function parameter values to a thread; 
it takes values as a tuple, so there must be a comma after the last value like 
(1,) or (1, 2, 3,)
"""
# t = threading.Thread(target=func, args=())
t = threading.Thread(target=func)  # create a thread
t.start()  # launch a thread

"""
an executable file alone is run in one thread already, so when we start another thread manually, 
the amount od threads equals 2, which we can theck with the next line of code
"""
print("\n" + str(threading.active_count()))
