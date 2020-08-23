import datetime
import threading
import sunrise
import sunset


def get_time_as_num():
    time = datetime.datetime.now()
    #Die Funktion str konventiert die nummer in einen String
    time = str(time)[11:13] + str(time)[14:16]
    #Die Funktion int konventiert den string in einen integer
    return int(time)

def timer():
    #Hier ist die festgelegte Zeit angeben
    start = 700
    end = 2000

    timer = threading.Event()

    endanf = 0
    startanf = 1

    while True:
        time = get_time_as_num()
        #Hier wird der Sonnenaufgang angefangen falls alles zutrifft.
        if time >= start and startanf > endanf:
            sunrise.exe_sunrise()
            endanf = endanf + 1
            if time >= start and time <= end:
                while get_time_as_num() < end:
                    timer.wait(30.00)
                    #Hier können später noch Funktionen hinzugefügt werden wie Gewitter, Wolken etc.g
        
        #Hier wird der Sonnenuntergang angefangen falls alles zutrifft.
        elif time >= end and startanf == endanf:
            sunset.exe_sunset()
            endanf = 0
            startanf = 1
            if time >= end and time >= start: #or time <= end and time <= start
                while get_time_as_num() > end and get_time_as_num() > start or get_time_as_num() < start:
                    timer.wait(30.00)
                    #Hier können später noch Funktionen hinzugefügt werden wie Mondphasen etc.

        timer.wait(59.00)#Zahl muss noch geändert werden 


if __name__ == '__main__':
    timer()
