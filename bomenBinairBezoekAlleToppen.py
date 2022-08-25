#p83 Algoritme 4.3 Doorlopen van een binaire boom in inorde
class BinaireBoom:
    l = None
    r = None

    def __init__(self, id):
        self.id = id

    def visit(self):
        print(self.id)


boom1 = BinaireBoom(1)
boom2 = BinaireBoom(2)
boom3 = BinaireBoom(3)
boom4 = BinaireBoom(4)
boom5 = BinaireBoom(5)
boom6 = BinaireBoom(6)
boom7 = BinaireBoom(7)
boom8 = BinaireBoom(8)
boom9 = BinaireBoom(9)

boom1.l = boom2
boom1.r = boom3

boom2.l = boom4
boom2.r = boom5

boom3.l = boom6

boom5.l = boom7
boom5.r = boom8

boom6.l = boom9

def inOrde(wortel):
    if wortel != None:
        inOrdeRecursief(wortel)

def inOrdeRecursief(boom):
    if boom.l != None:
        inOrdeRecursief(boom.l)
    boom.visit()
    if boom.r != None:
        inOrdeRecursief(boom.r)
    

inOrde(boom1)