# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") 

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}") #muutos masterissa
print(f"{erotus(x, y)}") #muutos masterissa

logger("lopetetaan ohjelma")
print("goodbye!")

