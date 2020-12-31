import socket
import os
from getmac import get_mac_address as gma
from colorama import Fore, init
init()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname )
print(Fore.CYAN +"""
██████╗  ██████╗           ██╗███╗   ██╗███████╗ ██████╗     
██╔══██╗██╔════╝           ██║████╗  ██║██╔════╝██╔═══██╗    
██████╔╝██║                ██║██╔██╗ ██║█████╗  ██║   ██║    
██╔═══╝ ██║                ██║██║╚██╗██║██╔══╝  ██║   ██║    
██║     ╚██████╗    ██╗    ██║██║ ╚████║██║     ╚██████╔╝    
╚═╝      ╚═════╝    ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝                                                               
""")
print("\n")
print(Fore.YELLOW + "INFORMACIÓN DE LA PC: ")
print(Fore.WHITE +"El nombre de tu ordenador es: " + hostname)
print("Tu dirección IP es: "+ ip)
print("La dirección MAC: "+ gma())
print("\n")
print(format(Fore.LIGHTGREEN_EX+"Programado por Pedro Jurado",'>40'))
print(Fore.WHITE +"\n")
os.system("pause")

