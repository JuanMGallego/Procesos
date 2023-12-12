import multiprocessing

# Proceso que recive el departamento y filtra por el departamento. Los envia a la cola
def proceso1(depSolicitado, cola):

    #Buscamos en el archivo por lineas
    with open("ejercicio02/salarios.txt", "r") as archivoSalarios:
        for linea in archivoSalarios:
            nombre, apellido, salario, departamento = linea.strip().split(';')

            #Si coincide lo añadimos a la cola
            if departamento == depSolicitado:
                cola.put(nombre, apellido, salario)
                    
#Proceso que filtra por el salario introducido. Envia los restantes a la cola
def proceso2(salSolicitado, cola):
    #Seleccionamos el salario de la linea
    for linea in cola.get():
        linea[0]

        #Lo enviamos a la cola si es mayor
        if int(linea[0] >= salSolicitado):
            cola.put(linea)

#Escribe en el txt de empleados los empleados filtrados
def proceso3(cola):
    for linea in cola.get():
        with open("ejercicio02/empleados.txt", "w") as archivoEmpleados:
            archivoEmpleados.write(linea)

if __name__ == "__main__":

    # solicitudes al user
    depSolicitado = input("Introduzca el nombre de un departamento: ")
    salSolicitado = round(input("Introduzca un salario minimo: "), 2)

    #Crear la cola
    cola = multiprocessing.Queue()

    #Se crean los procesos y se inician
    proceso1 = multiprocessing.Process(target=proceso1, args=(depSolicitado))
    proceso1.start()

    proceso2 = multiprocessing.Process(target=proceso2, args=(salSolicitado, cola))
    proceso2.start()

    proceso3 = multiprocessing.Process(target=proceso3, args=(cola))
    proceso3.start()

    # Esperar a que el Proceso 1 termine
    proceso1.join()

    # Esperar a que el Proceso 2 termine
    proceso2.join()

    # Esperar a que el Proceso 3 termine
    proceso3.join()