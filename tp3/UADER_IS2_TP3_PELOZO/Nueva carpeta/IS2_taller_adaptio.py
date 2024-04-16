import os
#*--------------------------------------------------------------------
#* Ejemplo de pattern Adapter
#* La clase Adaptee requiere un parámetros de operación con dos
#* argumentos mientras que el programa principal solo puede enviar 
#* uno de ellos.
#*--------------------------------------------------------------------
class Adaptee:

    def open_method(self) -> None:
        pass

    def operation(self, parm1, parm2) -> None:
        print("Los parámetros recibidos fueron parm1(%s) y parm2(%s)" %(parm1,parm2))

class Adapter:
	def __init__(self) -> None:
		self._egokitzailea = Adaptee()
		self.p2 = "fakeparm"
	def open_method(self) -> None:
		print("Connection with adaptee Ok")

	def operation(self, p1) -> None:
        	self._egokitzailea(p1,self.p2)


#*------------------------------------------------------------
#* main
#*------------------------------------------------------------

os.system("clear")

#*--Crea objeto que no se puede acceder directamente

print("\n")
parm1="clave1"
try:
	a = Adaptee()
	Adaptee.operation("1")

except Exception as e:
	print("la ejecución de Adaptee directa dió error %s\n" % (e))

#*-- Crea objeto adaptador
z = Adapter()
#Adapter.open_method()
Adapter.operation("1")
