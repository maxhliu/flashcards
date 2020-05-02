#!/usr/bin/python3
import csv
import random
import sys
import json

data = []
stats = {}

def shuffled(x):
    return random.sample(x, k=len(x))

class Stats:
    def __init__(self, path='stats.json'):
        self.path = path
        self.stats = readstats()

    def readstats(self):
        with open(self.path) as f:
            return json.load(f)

    def writestats(self):
        with open(self.path, 'w') as f:
            json.dump(self.stats, f)

    def increment(self, stat, success=True, memory=5):
        freq = self.getstat(stat)
        if success: freq['success'] += 1
        freq['total'] += 1
        self.setstat(stat, freq)

    def getstat(self, stat):
        return self.stats.get(stat, {'success': 0, 'total': 0})

    def setstat(self, stat, val):
        self.stats[stat] = val

    def getscore(self, stat):
        pass


def parse(fname):
    global data
    with open(fname) as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]

def quiz(fname):
    parse(fname)
    order = shuffled(range(len(data[0])))
    for row in shuffled(data):
        # print(row)
        for i in order:
            print(row[i])
            ans = input()

def iquiz(fname):
    parse(fname)
    order = shuffled(range(len(data[0])))
    for row in shuffled(data):
        # print(row)
        for i in order:
            print(row[i])
            ans = input()

if __name__ == "__main__":
    iquiz(sys.argv[1])

