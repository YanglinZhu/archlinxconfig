import random
numberOfStreaks = 0
ifNotStreaks = False
Streaks = 0
for experimentNumber in range(1000000):
    if random.randint(0 , 1):
        if ifNotStreaks:
            Streaks += 1
        else:
            ifNotStreaks = True
    else:
        if ifNotStreaks:
            ifNotStreaks = False
            Streaks = 0
    if Streaks == 6:
        numberOfStreaks += 1
        Streaks = 0
print('Chance of streak:%s%%'%(numberOfStreaks/10000))


