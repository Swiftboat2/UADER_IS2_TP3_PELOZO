import os
#*--------------------------------------------------------------------
#* Este es un ejemplo de patrón bridge
#*
#*--- Se definen los métodos de producción, cada uno toma los mismos
#*--- tres atributos genéricos length, breadth and height produce un
#*--- cubo acorde a esa especificación
#*--------------------------------------------------------------------

#*--- Abstracción de implementación (API1)
class ProducingAPI1:

	def produceCuboid(self, length, breadth, height):

		print("API1 va a fabricar un CUBO de dimensiones(%d,%d,%d)" % (length,breadth,height))

#*--- Abstracción de implementación (API2)
class ProducingAPI2:

	def produceCuboid(self, length, breadth, height):

		print("API2 va a fabricar un cuboide de dimensiones(%d,%d,%d)" % (length,breadth,height))

#*--- Abstracción de implementación (API2)
class ProducingAPI3:

	def produceCuboid(self, length, breadth, height):

		print("API3 es muy especializado y largo de ejecutar se ejecuta en un servidor aparte")
		print("API3 va a fabricar un cuboide de dimensiones(%d,%d,%d)" % (length,breadth,height))

#*---Clase cuboid  con sus propiedades pero con método de fabricación flexible
 
class Cuboid:

	def __init__(self, length, breadth, height, producingAPI):

		self._length = length
		self._breadth = breadth
		self._height = height

		self._producingAPI = producingAPI

#*---- cuando se invoca la producción invoca al objeto cuyo puntero se almacenó al crear

	def produce(self):

		self._producingAPI.produceCuboid(self._length, self._breadth, self._height)

	def expand(self, times):

		self._length = self._length * times
		self._breadth = self._breadth * times
		self._height = self._height * times

	def setproducingAPI(self, producingAPI):

		self._producingAPI = producingAPI


#*-----------------------------------------------------------
#* main
#*-----------------------------------------------------------

os.system("clear")

#*--- implementa un primer cuboide y le asigna ProducingAPI1()
cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

#*--- implementa un segundo cuboide y le asigna ProducingAPI2()
cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()

#*--- expande ambos cubos al doble (notese que no involucra método de 
#*--- producción

print("\n Expande dimensiones de cubo \n")
cuboid1.expand(2)
cuboid2.expand(2)

#*--- y los manda a producir nuevamente

cuboid1.produce()
cuboid2.produce()

print("\n Cambia método de producción en run-time API2->API1\n")
cuboid2.setproducingAPI(ProducingAPI1())
cuboid2.produce()

print("\n Cambia método de producción en run-time API2->API1\n")
cuboid2.setproducingAPI(ProducingAPI3())
cuboid2.produce()

