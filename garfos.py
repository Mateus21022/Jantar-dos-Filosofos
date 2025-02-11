import random
import threading
import time


class Garfos:
    def __init__(self, nome): 
        self.nome = nome
        self.lock = threading.Lock()  

    def pegar_garfo(self): 
        return self.lock.acquire(timeout=1) 
    
    def soltar_garfo(self):
        self.lock.release()



garfos = [
    Garfos("Garfo Nº 1"),
    Garfos("Garfo Nº 2"),
    Garfos("Garfo Nº 3"),
    Garfos("Garfo Nº 4"),
]


limite_garfos = threading.Semaphore(4)