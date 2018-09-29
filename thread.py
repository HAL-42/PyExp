# -*- coding: utf-8 -*-

import threading
import time

lock = threading.Lock()
dpst = 100

def chg_dpst(n: int):
    global dpst
    dpst += n
    time.sleep(0.01)
    dpst -= n
    print(dpst)

def calc_dpst():
    print("The current thread is {}".format(threading.current_thread().name))
    for i in range(1000):
        lock.acquire()
        try:
            chg_dpst(i)
        finally:
            lock.release()

if __name__ == "__main__":
    tc1 = threading.Thread(target=calc_dpst,name="calc_dpst 1")
    tc2 = threading.Thread(target=calc_dpst,name="calc_dpst 2")
    tc3 = threading.Thread(target=calc_dpst,name="calc_dpst 3")
    tc1.start()
    tc2.start()
    tc3.start()
    tc1.join()
    tc2.join()
    tc3.join()
    print(dpst)






