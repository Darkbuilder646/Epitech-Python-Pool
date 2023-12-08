def bread ():
    print (" <////////// > ")
def lettuce ():
    print (" ~~~~~~~~~~~~ ")
def tomato ():
    print (" O O O O O O ")
def ham ():
    print (" ============ ")

def MakeSandwiches(number: int):
    if(number <= 0):
        print("I can't do this")
        return
    for i in range(number):
        bread()
        ham()
        ham()
        tomato()
        lettuce()
        bread()
        print("\n")

MakeSandwiches(10)