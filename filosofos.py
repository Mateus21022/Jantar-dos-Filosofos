from garfos import * 
import random
import threading
import time
import keyboard

class Filosofos: 
    def __init__(self, nome, garfo_esquerda, garfo_direita):     
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita

    def funcao_filosofo(self):
    
        designacao = random.randint(1, 3)
        match designacao:
            case 1: 
                self.tentar_pegar_garfo()
            case 2:
                self.pensar()
            case 3: 
                self.comer()

    def pensar(self):
        print(f"{self.nome} está pensando...")

    def comer(self):
        print(f"{self.nome} está tentando comer...")
        if self.pegar_garfos_funcao(self.garfo_esquerda) and self.pegar_garfos_funcao(self.garfo_direita):
            print(f"{self.nome} está comendo...")
            time.sleep(2)
            self.soltar_garfos_funcao(self.garfo_esquerda)
            self.soltar_garfos_funcao(self.garfo_direita)
            print(f"{self.nome} parou de comer e largou os garfos.")
        else:
            print(f"{self.nome} não conseguiu pegar os garfos.")
            self.pensar()
            time.sleep(1)
        
    def tentar_pegar_garfo(self):
        print(f"{self.nome} está tentando pegar garfos, mas não vai comer agora.")
        time.sleep(1)

    def pegar_garfos_funcao(self, garfo):
        if limite_garfos.acquire(timeout=1):
            if garfo.pegar_garfo():
                print(f"{garfo.nome} foi pego.")
                return True
            else: 
                limite_garfos.release()
                print(f"{garfo.nome} não pôde ser pego.")
                return False
        else:
            print(f"Não foi possível pegar o {garfo.nome}. Todos os garfos estão ocupados.")
            return False

    def soltar_garfos_funcao(self, garfo):
        garfo.soltar_garfo()
        limite_garfos.release()
        print(f"O {garfo.nome} foi solto.")


garfos = [
    Garfos("Garfo Nº 1"),
    Garfos("Garfo Nº 2"),
    Garfos("Garfo Nº 3"),
    Garfos("Garfo Nº 4"),
    Garfos("Garfo Nº 5")
]

limite_garfos = threading.Semaphore(4)

filosofos = [
    Filosofos("Sócrates", garfos[0], garfos[1]),
    Filosofos("Platão", garfos[1], garfos[2]),
    Filosofos("Aristóteles", garfos[2], garfos[3]),
    Filosofos("Descartes", garfos[3], garfos[4]),
    Filosofos("Kant", garfos[4], garfos[0])
]

def escolher_filosofo():
    while True:
        filosofo = random.choice(filosofos)
        filosofo.funcao_filosofo()
        if keyboard.is_pressed('esc'): 
            print("Programa encerrado.")
            break
        time.sleep(1)


escolha_thread = threading.Thread(target=escolher_filosofo)
escolha_thread.start()
