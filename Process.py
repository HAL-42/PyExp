from multiprocessing import Process, Pool, Queue
import os
import time

def run_put(msg: str, q: Queue):
    print("The current PID is {PID}".format(PID=os.getpid()))
    q.put(msg)
    time.sleep(2)

def run_get(q: Queue):
    print("The current PID is {PID}".format(PID=os.getpid()))
    while True:
       print(q.get(True))

if __name__ == '__main__':
    q = Queue()
    pg = Process(target=run_get, args=(q,))
    pg.start()
    pw = [ Process(target=run_put, args=("Yes"+str(i),q,)) for i in range(5)]
    for x in pw:
       x.start()
    print('Waiting for all subprocesses done...')
    for x in pw:
        x.join()
    pg.terminate()
