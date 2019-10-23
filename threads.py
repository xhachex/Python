import _thread as hilo
from modules import func_cuadrado as sq
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time())))

try:
    hilo.start_new_thread( print_time, ("Thread-1", 0.05,))
    hilo.start_new_thread( print_time, ("Thread-2", 0.10,))
    hilo.start_new_thread( sq, (10,))
except:
    print ("Error")
