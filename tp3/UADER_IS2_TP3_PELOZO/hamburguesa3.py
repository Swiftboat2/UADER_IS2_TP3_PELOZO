class Hamburguesa:
    def __init__(self, tipo, tamaño):
        self.tipo = tipo
        self.tamaño = tamaño

    def entregar(self):
        pass

class EntregaEnMostrador(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.tipo} de tamaño {self.tamaño} está lista para ser recogida en mostrador.")

class RetiradaPorCliente(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.tipo} de tamaño {self.tamaño} ha sido retirada por el cliente.")

class EntregaADomicilio(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.tipo} de tamaño {self.tamaño} ha sido enviada por delivery.")

class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo_entrega, tipo, tamaño):
        if tipo_entrega == "mostrador":
            return EntregaEnMostrador(tipo, tamaño)
        elif tipo_entrega == "cliente":
            return RetiradaPorCliente(tipo, tamaño)
        elif tipo_entrega == "domicilio":
            return EntregaADomicilio(tipo, tamaño)
        else:
            raise ValueError("Tipo de entrega no válido.")
if __name__ == "__main__":
    tipo_entrega = input("Ingrese el tipo de entrega deseado (mostrador/cliente/domicilio): ").strip()
    tipo = input("Ingrese el tipo de hamburguesa: ").strip()
    tamaño = input("Ingrese el tamaño de la hamburguesa: ").strip()

    hamburguesa = HamburguesaFactory.crear_hamburguesa(tipo_entrega, tipo, tamaño)
    hamburguesa.entregar()
