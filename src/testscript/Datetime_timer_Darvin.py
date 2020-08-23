#!/usr/bin/python
import datetime
import time

#das funktioniert nicht
d_now = datetime.datetime.now()
year = d_now.year
month = d_now.month
day = d_now.day
d_start = datetime.datetime(year, month, day, 20, 32)
d_end = datetime.datetime(year, month, day, 21, 23)

print (d_start)
print (d_end)

#durchlauf = 1
endanf = 0
startanf = 1

while True:
    if d_now >= d_start and startanf > endanf :
        endanf = endanf + 1
        print("START") 
        print (endanf)
        print (startanf)    
    if d_now >= d_end and startanf == endanf:
        print ("END")
        startanf = startanf + 1
        time.sleep(1)
        endanf = 0
        startanf = 1
        print (endanf)
        print (startanf)
    #durchlauf = durchlauf + 1
