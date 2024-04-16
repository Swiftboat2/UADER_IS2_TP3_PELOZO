import os
#*--------------------------------------------------------------------
#* Ejemplo de patrón de diseño observer
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------

class Subject:

#*------- Representa lo que se está observando

	def __init__(self):

		self._observers = []

	def notify(self, modifier = None):


		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):

#*------- Agregar observador si ya no está en la lista

		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):

#*------- Remover observador si está en la lista


		try:
			self._observers.remove(observer)
		except ValueError:
			pass


#*----------- Define a los observadores

class Data(Subject):

	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		print("El dato bajo observación ha sido actualizado al valor %d\n" % (value))
		self.notify()


class HexViewer:


	def update(self, subject):
		print('HexViewer: Se recibio una actualización %s que la procesa como 0x{%x}' % (subject.name, subject.data))

class OctalViewer:

	def update(self, subject):
		print('OctalViewer: Se recibio una actualización' + str(subject.name) + 'que la procesa como '+str(oct(subject.data)))


class DecimalViewer:

	def update(self, subject):
		print('DecimalViewer: Se recibio una actualización %s que la procesa como  %d' % (subject.name, subject.data))

"""main function"""

if __name__ == "__main__":


	os.system("clear")

	print("Crea los observadores DecimalViewer + HexViewer + OctalViewer\n")
	view1 = DecimalViewer()
	view2 = HexViewer()
	view3 = OctalViewer()


	print("\nCrea un objeto de datos, subscribe a el decimal y hex\n")
	obj1 = Data('Data 1')
	obj1.attach(view1)
	obj1.attach(view2)

	print("Modifica el dato")
	obj1.data = 10

	print("\nCrea un objeto de datos, subscribe a el decimal, hex y octal\n")
	obj2 = Data('Data 2')
	obj2.attach(view1)
	obj2.attach(view2)
	obj2.attach(view3)

	print("Modifica el dato")

	obj2.data = 15

	obj2.detach(view1)
	obj2.data = 12
