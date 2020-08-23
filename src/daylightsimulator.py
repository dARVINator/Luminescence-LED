import datetime
import threading
import sunrise_test
import sunset_test


def get_time_as_num():
    time = datetime.datetime.now()
    #Die Funktion str konventiert die nummer in einen String
    time = str(time)[11:13] + str(time)[14:16]
    #Die Funktion int konventiert den string in einen integer
    return int(time)

def main():
    #Hier ist die festgelegte Zeit angeben
    start = 1759
    end = 1805

    timer = threading.Event()

    endanf = 0
    startanf = 1

    while True:
        time = get_time_as_num()
        #Hier wird der Sonnenaufgang angefangen falls alles zutrifft.
        if time >= start and startanf > endanf:
            sunrise_test.aufgang()
            endanf = endanf + 1
        
        #Hier wird der Sonnenuntergang angefangen falls alles zutrifft.
        elif time >= end and startanf == endanf:
            sunset_test.untergang()
            endanf = 0
            startanf = 1

        timer.wait(4.0)


if __name__ == '__main__':
    main()
