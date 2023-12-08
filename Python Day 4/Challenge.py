i = int(input("Enter a integer\n"))
s = str(input("Enter a string\n"))

if(i != 0):
    print(i if(l for l in s if l in "aeiouAEIOU") else "")
    print(i if(i >= 42) else s)