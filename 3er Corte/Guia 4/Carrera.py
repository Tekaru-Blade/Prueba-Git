import threading
import random
import time

class Carrera:
    def __init__(self, num_carros, vueltas, velocidad_general, callback_mover, callback_fin):
        self.num_carros = num_carros
        self.vueltas = vueltas
        self.velocidad_general = velocidad_general
        self.callback_mover = callback_mover
        self.callback_fin = callback_fin
        self.resultados = []
        self.lock = threading.Lock()
        self.en_carrera = False
        self.hilos = []

    def iniciar(self):
        if self.en_carrera:
            return
        self.en_carrera = True
        self.resultados.clear()
        self.hilos.clear()

        for i in range(self.num_carros):
            hilo = threading.Thread(target=self.mover_carro, args=(i,))
            hilo.start()
            self.hilos.append(hilo)

        monitor = threading.Thread(target=self.esperar_final)
        monitor.start()

    def detener(self):
        self.en_carrera = False

    def mover_carro(self, idx):
        base = random.uniform(60, 180)
        inicio = time.time()
        x = 50
        vueltas = 0
        FINISH_X = 850
        tick = 0.02

        while self.en_carrera and vueltas < self.vueltas:
            if random.random() < 0.05:
                base *= random.uniform(0.8, 1.2)
            delta = base * tick * self.velocidad_general()
            x += delta
            if x >= FINISH_X:
                vueltas += 1
                if vueltas < self.vueltas:
                    x = 50
                else:
                    total = time.time() - inicio
                    with self.lock:
                        self.resultados.append((idx + 1, total))
                    break
            self.callback_mover(idx, x)
            time.sleep(0.01)

    def esperar_final(self):
        for h in self.hilos:
            h.join()
        self.en_carrera = False
        self.callback_fin(self.resultados)