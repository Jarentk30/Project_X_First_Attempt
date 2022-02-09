

class Sala_Urgencias:
    def __init__(self, numero_pacientes_en_espera, camas_disponibles):
        self.numero_pacientes_en_espera = numero_pacientes_en_espera
        self.camas_disponibles = camas_disponibles

    def add_ocupacion_cama(self, paciente_ingreso):
        self.camas_disponibles -= paciente_ingreso

urg = Sala_Urgencias(numero_pacientes_en_espera=15, camas_disponibles=20)
#print(urg.camas_disponibles)
#urg.add_ocupacion_cama(2)
#print(urg.camas_disponibles)
    
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self, nombre_otro, edad_otro):
        if edad_otro > 18:
            return(f"Buenas tardes Sr {nombre_otro}, mi nombre es {self.nombre}. ")
        return(f"Hola {nombre_otro}")
person = Persona(nombre= "David", apellido="Cardenas")
print(person.saludo("Samuel",14))
