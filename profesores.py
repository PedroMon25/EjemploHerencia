# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._max = ""
        self._categoria = ""

    # Getter y Setter
    def get_max(self):
        return self._max

    def set_max(self,max):
        self._max = max

    def get_categoria(self):
        return self._categoria

    def set_categoria(self,categoria):
        self._categoria = categoria


    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento},capacidad de estudio: {self._max},categoria: {self._categoria}"