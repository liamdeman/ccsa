#75 Algoritme 4.1 Doorlopen van een boom in preorde
class Boom:
    kinderen = []
    def __init__(self, id):
        self.id = id

    def visit(self):
        print(self.id)


boom1 = Boom(1)
boom2 = Boom(2)
boom3 = Boom(3)
boom4 = Boom(4)
boom5 = Boom(5)
boom6 = Boom(6)
boom7 = Boom(7)
boom8 = Boom(8)
boom9 = Boom(9)
boom10 = Boom(10)
boom11 = Boom(11)

boom1.kinderen = [boom2, boom6]

boom2.kinderen = [boom3,boom4,boom5]

boom6.kinderen = [boom7, boom11]

boom7.kinderen = [boom8, boom9]

boom9.kinderen = [boom10]

def preOrde(wortel):
    print('preOrde')
    recursieStapPreOrde(wortel)

def recursieStapPreOrde(boom):
    boom.visit()
    for kind in boom.kinderen:
        recursieStapPreOrde(kind)

def postOrde(wortel):
    print('postOrde')
    recursieStapPostOrde(wortel)

def recursieStapPostOrde(boom):
    for kind in boom.kinderen:
        recursieStapPostOrde(kind)
    boom.visit()


    

preOrde(boom1)
postOrde(boom1)