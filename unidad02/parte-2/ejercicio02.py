import random
from multiprocessing import Process, Queue

# Proceso que genera las 10 ips aleatoriamente
def proceso1(queue):

    # Generar 10 direcciones IP aleatorias
    direccionesIp = [str(f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}") for _ in range(10)]
    
    # Enviar las direcciones IP al Proceso 2
    queue.put(direccionesIp)

# Proceso que lee las direcciones ip y las filtra
def proceso2(input_queue, output_queue):

    # Recibir las direcciones IP del Proceso 1
    direccionesIp = input_queue.get()

    # Filtrar las direcciones IP por clases A, B o C
    ipsFiltradas = [ip for ip in direccionesIp if int(ip.split(".")[0]) <= 223]

    # Enviar las direcciones filtradas al Proceso 3
    output_queue.put(ipsFiltradas)

# Proceso que recoge las ips del proceso 2 y las musetra junto a su clase
def proceso3(queue):
    # Recibir las direcciones IP filtradas del Proceso 2
    ipsFiltradas = queue.get()

    # Imprimir por consola la dirección IP y la clase a la que pertenece
    for ip in ipsFiltradas:

        # Selecciona la clase de IP (Letra)
        tiposClase = ["A", "B", "C"]
        clase = int(int(ip.split(".")[0]))

        if clase <= 127:

            print(f"Dirección IP: {ip}, Clase: {tiposClase[0]}")

        elif clase >= 128 and clase <= 191:
            
            print(f"Dirección IP: {ip}, Clase: {tiposClase[1]}")
        
        elif clase >= 192 and clase <= 223:
            
            print(f"Dirección IP: {ip}, Clase: {tiposClase[2]}")
        
        else:

            print(f"Dirección IP: {ip}, Clase: Desconocida")
        
# Main con las creaciones de las colas y los procesos
if __name__ == "__main__":

    # Se crean las colas
    cola1 = Queue()
    cola2 = Queue()

    # Mandar los procesos
    p1 = Process(target=proceso1, args=(cola1,))
    p2 = Process(target=proceso2, args=(cola1, cola2))
    p3 = Process(target=proceso3, args=(cola2,))

    p1.start()
    p1.join()

    # Esperar a que el Proceso 1 termine antes de lanzar el Proceso 2

    p2.start()
    p2.join()

    # Esperar a que el Proceso 2 termine antes de lanzar el Proceso 3

    p3.start()

    p1.join()
    p2.join()
    p3.join()