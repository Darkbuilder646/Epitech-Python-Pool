key = int(input("Enter your number key\n"))
string = str(input("Enter your message\n"))
cryptString = ""

string = string.lower()

# 97 -> 122
for char in string:
    if(char == " " or char == "'"):
        cryptString += char
        continue

    indexUni = ord(char) + key
    if(indexUni > 122):
        indexUni = (indexUni - 122) + 96

    cryptString += chr(indexUni)

print(cryptString)