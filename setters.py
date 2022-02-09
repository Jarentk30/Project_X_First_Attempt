class Apartamentos:
    def __init__(self, precio = 100):
        self._precio = precio

    def cambio_precio(self, valor):
        if valor > 2000:
            raise ValueError("Es muy costoso para nuestro modelo")
        else:
            self._precio = valor
            print("Cambio exitoso")
    def pr(self):
        del self._precio   
    @property
    def r_precio(self):
        return self._precio
    
Apt = Apartamentos()
Apt.r_precio = 10
print(Apt._precio)
