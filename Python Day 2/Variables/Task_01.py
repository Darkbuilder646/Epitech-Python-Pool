numberOfTime = int(input("Choose the number of 1\n"))

def ComputeAddOne(number):
    result = 0
    for i in range(1, number + 1):
        temp = "1"
        temp = temp * i
        result += int(temp)
    print(result)

def ComputePowerOne(number):
    result = 0
    one = 1
    for i in range(1, number + 1):
        result += one ** i
    print(result)

#ComputeAddOne(numberOfTime)
ComputePowerOne(numberOfTime)
