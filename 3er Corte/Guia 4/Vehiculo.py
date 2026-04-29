import threading
import random
import time

class Vehiculo(threading.Thread):
    def __init__(self, idx, vueltas_totales, finish_x, vel_func, lock, resultados, callback_mover):
        super().__init__()
        self.idx = idx
        self.vueltas_totales = vueltas_totales
        self.finish_x = finish_x
        self.vel_func = vel_func 
        self.lock = lock
        self.resultados = resultados
        self.callback_mover = callback_mover
        self.en_carrera = True

    def run(self):
        base_speed = random.uniform(60, 180)
        inicio = time.time()
        x = 50
        vueltas_completadas = 0
        tick = 0.02

        while self.en_carrera and vueltas_completadas < self.vueltas_totales:
            if random.random() < 0.05:
                base_speed *= random.uniform(0.8, 1.2)
            
            delta = base_speed * tick * self.vel_func()
            x += delta
            
            if x >= self.finish_x:
                vueltas_completadas += 1
                if vueltas_completadas < self.vueltas_totales:
                    x = 50 
                else:
                    x = self.finish_x
                    tiempo_total = time.time() - inicio
                    # Uso de Lock para sincronizar el acceso a la lista compartida
                    with self.lock:
                        self.resultados.append((self.idx + 1, tiempo_total))
            
            self.callback_mover(self.idx, x)
            time.sleep(0.01)

    def detener(self):
        self.en_carrera = False