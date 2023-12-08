def bread ():
    print (" <////////// > ")
def lettuce ():
    print (" ~~~~~~~~~~~~ ")
def tomato ():
    print (" O O O O O O ")
def ham ():
    print (" ============ ")

def Make42Sandwiches():
    for i in range(42):
        bread()
        ham()
        ham()
        tomato()
        lettuce()
        bread()
        print("\n")

Make42Sandwiches()