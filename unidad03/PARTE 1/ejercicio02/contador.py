from threading import Thread

class Contador(Thread):

    variable_compartida = 0

    def run(self):
        while(Contador.variable_compartida < 1000):
            Contador.variable_compartida += 1
            print("Variable: ", Contador.variable_compartida)