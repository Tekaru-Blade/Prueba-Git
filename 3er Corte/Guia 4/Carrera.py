import threading
from Vehiculo import Vehiculo

class Carrera:
    def __init__(self, num_carros, vueltas, finish_x, vel_func, callback_mover, callback_fin):
        self.num_carros = num_carros
        self.vueltas = vueltas
        self.finish_x = finish_x
        self.vel_func = vel_func
        self.callback_mover = callback_mover
        self.callback_fin = callback_fin
        self.resultados = []
        self.lock = threading.Lock()
        self.vehiculos = []

    def iniciar(self):
        self.resultados.clear()
        self.vehiculos.clear()
        for i in range(self.num_carros):
            v = Vehiculo(i, self.vueltas, self.finish_x, self.vel_func, self.lock, self.resultados, self.callback_mover)
            self.vehiculos.append(v)
            v.start()

        threading.Thread(target=self.esperar_final, daemon=True).start()

    def esperar_final(self):
        for v in self.vehiculos:
            v.join() # Espera a que cada hilo de vehículo termine
        self.callback_fin(self.resultados)

    def detener(self):
        for v in self.vehiculos:
            v.detener()