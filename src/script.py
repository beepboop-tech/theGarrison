from BarTender import BarTender
from Drink import drinks
import atexit

b = BarTender()

def printMenu():
    print('\n\n')
    print('Menu')
    for i, drink in enumerate(drinks):
        print('\t' + str(i+1) + ": " + drink.name)
    print("Press 'q' to exit")
    
def handle(inpt):
    glass = input("Is there a glass on the trolley?")
    if (glass.lower() == 'y'):
        print("Makeing a " + str(drinks[int(inpt)-1].name))
        b.make(drinks[int(int(inpt)-1)])
        

printMenu()
inpt = input("What would you like?")

while (inpt.lower() != 'q'):
    handle(inpt)
    printMenu()
    inpt = input("What would you like?\t")
    

b.shutDown()


def ending():
    b.shutDown()
#atexit.register(ending)
