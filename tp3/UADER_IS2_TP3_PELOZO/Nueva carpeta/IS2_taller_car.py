import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getCar(self):
      car = Car()
      
      # Primero el chasis
      body = self.__builder.getBody()
      car.setBody(body)
      
      # Luego el motor
      engine = self.__builder.getEngine()
      car.setEngine(engine)
      
      # Finalmente (4) ruedas
      i = 0
      while i < 4:
        wheel = self.__builder.getWheel()
        car.attachWheel(wheel)
        i += 1

      # Retorna el vehiculo completo
      return car

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Car:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("planta motora: %d" % (self.__engine.horsepower))
      print ("ruedas: %d\'" % (self.__wheels[0].size))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class JeepBuilder(Builder):
   
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 22
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 400
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Wheel:
   size = None

class Engine:
   horsepower = None

class Body:
   shape = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   jeepBuilder = JeepBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(jeepBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   jeep = director.getCar()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   jeep.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

   main()
