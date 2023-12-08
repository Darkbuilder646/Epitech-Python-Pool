check1 = "cat"
check2 = "garden"
check3 = "mice"


string = str(input("Enter your string\n"))
string2 = string.lower()

def ComputeWord(stringToCheck: str):
    instance = 0
    if(check1 in stringToCheck):
        instance += 1
    if(check2 in stringToCheck):
        instance += 1
    if(check3 in stringToCheck):
        instance += 1
    return instance 


number = ComputeWord(string2)

print(string, "has", number, "of word 'Cat,' 'Garden,' 'Mice'")
