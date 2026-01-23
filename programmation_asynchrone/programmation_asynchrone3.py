#coding:utf-8

import threading
import time

class Myprocess(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        count = 0
        while count < 5:
            time.sleep(self.delay)
            count += 1
            print(f"{self.name} - itération {count}")


th1 = Myprocess("Processus 1", 1)
th2 = Myprocess("Processus 2", 2)

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")