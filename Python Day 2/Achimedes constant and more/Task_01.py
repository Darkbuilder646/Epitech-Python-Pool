#4*(1/1 - 1/3 - 1/5 - 1/7 ...)
import math
iterration = n = int(input("Enter number of iterration\n"))	

def CalculatePi (n: int):
    result = 1.0

    for i in range(1, n+1):
        result += (1.0 if i%2 == 0 else -1.0) / (2 * i + 1)
        
    return round(4 * result, 6)

print(CalculatePi(iterration))
print(math.pi, " Vrai PI")