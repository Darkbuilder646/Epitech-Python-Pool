# PI - 3 = 1²/(6+3²/(6+5²/(6+7²/(6+9²/(6+11²/(6+13²/(6+15²)))))))  => n = 7
import math
iterration = int(input("Enter number of iterration\n"))	

def CalculateAmazingPi (n: int):

    powerFract: float = 6 + pow((n*2)+1, 2)
    result: float = powerFract

    for i in reversed(range(n)):
        tempPowerFract: float = pow((i*2)+1, 2)

        if(i!=0):
            result = (tempPowerFract / result) + 6
        else:
            result = 1**2 / result

    return round(result + 3, 6)

print(CalculateAmazingPi(iterration))
#print(math.pi)
    