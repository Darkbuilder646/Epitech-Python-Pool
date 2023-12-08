nbr = -30

def MultipleByThree(number: int):
    return True if number % 3 == 0 else False

def MultipleByFive(number: int):
    return True if number % 5 == 0 else False

while nbr <= 30:
    if(MultipleByThree(nbr) and MultipleByFive(nbr)):
        print("FizzBuzz")
    elif(MultipleByThree(nbr)):
        print("Fizz")
    elif(MultipleByFive(nbr)):
        print("Buzz")
    else:
        print(nbr)
    nbr += 1