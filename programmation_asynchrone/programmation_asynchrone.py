#coding:utf-8

import threading
import time

def process_one():
    i = 0
    while i < 3:
        print("Processus un - itération", i)
        time.sleep(2)
        i += 1

def process_two():
    i = 0
    while i < 3:
        print("Processus deux - itération", i)
        time.sleep(3)
        i += 1

th1 = threading.Thread(target=process_one)
th2 = threading.Thread(target=process_two)

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")