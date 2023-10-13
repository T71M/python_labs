import datetime as date
import random as r
import itertools


teams = [f't{i + 1}' for i in range(16)]
r.shuffle(teams)
dateStart = date.datetime(2016, 9, 14)

groups = [[], [], [], []]

for i in range(len(groups)):
    for _ in range(4):
        groups[i].append(teams.pop())


matches = list(itertools.chain(groups[0], groups[1], groups[2], groups[3]))


for i in range(0, len(matches), 2):
    print(
        f'матч между командами {matches[i]} - {matches[i+1]} состоится: {dateStart}')
    dateStart += date.timedelta(days=14)
