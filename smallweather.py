#!/usr/bin/python3
import json
import random
import time

cities = ("Munich", "Berlin", "Hamburg", "Frankfurt", "Vienna", "Zurich")

def main():

    while True:
        row_dict = {
            'time' : int(time.time()),
            'city' : random.choice(cities),
            'temp' : random.randint(0, 35)
        }
        row = json.dumps(row_dict)
        print(row)

if __name__ == "__main__":
    main()
