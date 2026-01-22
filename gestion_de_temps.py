#coding:utf-8


"""
            l   ocaltime()
(TimeSTAMP) -----------------> structure de temps
            <-----------------
                mktime()
"""
import time

print("Début de la gestion du temps")
time.sleep(5)
print("5 secondes se sont écoulées")

print((time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())))
print(time.strftime("%Z", time.localtime()))