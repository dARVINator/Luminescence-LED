#!/usr/bin/env python

import datetime
import threading


def do_your_work():
    print("Hello")
    print("world")


def get_time_as_num():
    time = datetime.datetime.now()              # -> 2019-01-12 11:09:33.033172
    time = str(time)[11:13] + str(time)[14:16]  # 2019-01-12 11:09:33.033172 -> 11:09 -> 1109
    return int(time)


def main():
    start = 2054  # 08:00 Uhr
    end = 2055   # 08:15 Uhr

    timer = threading.Event()

    while True:
        time = get_time_as_num()
        if time >= start and time <= end:
            while get_time_as_num() < end:
                do_your_work()

        timer.wait(4.0)


if __name__ == '__main__':
    main()