import time as t
statTime = t.time()

def powerFunc(nPower: int):
    print(pow(42,nPower))

def PowerRecursif(number: int, exposant: int):
    if exposant == 0:
        return 1

    if exposant >= 1:
        return number * PowerRecursif(number, exposant - 1)

#powerFunc(84) #time ~ 0.001001119613647461 sec
PowerRecursif(42, 168) #time ~ 0.000997781753540039 sec

duration = t.time() - statTime
print(duration)