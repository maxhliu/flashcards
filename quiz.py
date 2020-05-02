#!/usr/bin/python3
import csv
import random
import sys

data = []

def shuffled(x):
    return random.sample(x, k=len(x))

def parse(fname):
    global data
    data = []
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

def quiz(fname):
    parse(fname)
    order = shuffled(range(len(data[0])))
    for row in shuffled(data):
        # print(row)
        for i in order:
            print(row[i])
            ans = input()

if __name__ == "__main__":
    quiz(sys.argv[1])
