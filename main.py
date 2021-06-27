# coding=utf-8
# https://projects.raspberrypi.org/en/projects/temperature-log/
from time import time, sleep
import psutil
import subprocess
import csv
import os

RUNTIME = 600  # runtime of each cycle in seconds, must be multiple of 10

if not RUNTIME % 10 == 0:
    raise ValueError("Runtime must be a multiple of 10!")

values = []

def get_cpu_temp():
    raw = psutil.sensors_temperatures()
    tl = list(raw.items())
    temp = tl[0][1][0].current
    return temp

def do_logging():
    for _ in range(RUNTIME//10):
        temperature = get_cpu_temp()
        cpu_speed = psutil.cpu_freq()[0]
        ctime = round(time())
        print(f"{ctime}: {cpu_speed}MHz: {temperature} deg C")
        values.append([ctime, temperature, cpu_speed])
        sleep(10)

try:
    print("sleeping to decrease CPU speed after setup")
    sleep(10)

    print("logging idle")
    do_logging()


    stress = subprocess.Popen(["stress", "-c", "4", "-m", "1", "-t", str(RUNTIME)])

    print("logging stress")
    do_logging()

    stress.poll()

    print("logging cooldown")
    do_logging()
except KeyboardInterrupt:
    pass

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(values)

