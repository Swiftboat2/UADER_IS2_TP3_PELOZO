import os
#*--------------------------------------------------------------------------
#* Ejemplo de patron Facade
#*
#*--------------------------------------------------------------------------
class Washing:
	def wash(self):
		print("Sub-sistema Lavadora: Función de lavado")


class Rinsing:

	def rinse(self):
		print("Sub-sistema Enjuagadora: Función de enjuagado")


class Spinning:

	def spin(self):
		print("Sub-sistema Centrifugadora: Función centrifugado")

class Vaciado:

	def vaciar(self):
		print("Sub-sistema Vaciado: Función de vaciado")


class WashingMachine:

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()
		self.vaciado = Vaciado()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()
		self.vaciado.vaciar()

if __name__ == "__main__":



	os.system("clear")
	print("Se comienza con el ciclo de lavado con <START>\n")
	washingMachine = WashingMachine()
	washingMachine.startWashing()

