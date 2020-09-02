#!/usr/bin/python3
import json
import random
import time

cities = ("Munich", "Berlin", "Hamburg", "Frankfurt", "Vienna", "Zurich")

def main():

    while True:
        theTime = (int(time.time()) // 300) * 300  # make it 5 minute grain
        if random.random() < 0.05:                 # 5% chance of late arriving data
            theTime -= 600                         # 10 minutes late
        row_dict = {
            'time' : theTime,
            'city' : random.choice(cities),
            'subloc' : random.randint(1, 3),
            'temp' : random.randint(0, 35)
        }
        row = json.dumps(row_dict)
        print(row)
        time.sleep(10)

if __name__ == "__main__":
    main()
