key = int(input("Enter your number key\n"))
string = str(input("Enter your message\n"))
unCryptString = ""

string = string.lower()

# 97 -> 122
for char in string:
    if(char == " " or char == "'"):
        unCryptString += char
        continue

    indexUni = ord(char) - key
    if(indexUni < 97):
        indexUni = 123 - (97 - indexUni)

    unCryptString += chr(indexUni)

print(unCryptString)