from adivinador import *

# hilos = [Adivinador("Hilo " + str(_)) for _ in range(10)]

# for a in hilos:
#     a.start()

# for a in hilos:
#     a.join()

a1 = Adivinador("Hilo 1")
a2 = Adivinador("Hilo 2")
a3 = Adivinador("Hilo 3")
a4 = Adivinador("Hilo 4")
a5 = Adivinador("Hilo 5")
a6 = Adivinador("Hilo 6")
a7 = Adivinador("Hilo 7")
a8 = Adivinador("Hilo 8")
a9 = Adivinador("Hilo 9")
a10 = Adivinador("Hilo 10")

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()
a6.start()
a7.start()
a8.start()
a9.start()
a10.start()

a1.join()
a2.join()
a3.join()
a4.join()
a5.join()
a6.join()
a7.join()
a8.join()
a9.join()
a10.join()