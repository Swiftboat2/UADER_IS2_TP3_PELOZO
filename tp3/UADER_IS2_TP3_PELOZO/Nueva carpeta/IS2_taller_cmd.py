import os
#*--------------------------------------------------------------------
#* Patron command
#*--------------------------------------------------------------------
"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

#*------ Este es la interfaz (plantilla) de un comando (genérico)
class Command(ABC):
	
	def __init__(self, receiver):
		self.receiver = receiver
	
	def process(self):
		pass

#*------ Esta es una implementación de un comando específico
class CommandImplementation(Command):
	
	def __init__(self, receiver):
		self.receiver = receiver

	def process(self):
		self.receiver.perform_action()

#*----- Este es el receptor del comando
class Receiver:
	
	def perform_action(self):
		print('La acción requerida ha sido realizada en <Receiver>')

#*----- Este es el emisor del comando
class Invoker:
	
	def command(self, cmd):
		self.cmd = cmd

	def execute(self):
		print("se ha recibido el comando")
		self.cmd.process()

"""main method"""
if __name__ == "__main__":

	os.system("clear")
	print("Crea receptor")	
	receiver = Receiver()

	print("asocia el receptor a la implementación del comando")
	cmd = CommandImplementation(receiver)

	print("crea el invocador")
	invoker = Invoker()

	print("envia el comando al invocador y ejecuta")
	invoker.command(cmd)
	invoker.execute()

