class Auto():
    def say_ok(self):
        print('ok')

    def __init__(self, name):
        print('I\'m ', name )

c1 = Auto('Audi')
c2 = Auto('Ford')
c1.say_ok()