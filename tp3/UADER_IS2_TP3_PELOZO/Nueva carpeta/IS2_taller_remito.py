#!/usr/bin/python3.7
#*--------------------------------------------------
#* remito.py
#* basado en factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
import os

#*--------------------------------------------------
#* La clase Creador es una superclase creadora de 
#* objetos donde las clases no están especificadas
#*--------------------------------------------------
class Creator(ABC):
    """
    La clase Creator declara la "factory" que retorna un puntero a un objeto
    pero que no tiene implementaciones concretas de sus métodos, es como 
    una plantilla de creación futura
    """

    @abstractmethod

    def factory_method(self):
        pass

#*----------------------------------------------------------------
#* Podría no crearlo pero también es posible implementar alguna
#* operación que sea común a todas las posibles implementaciones
#* esta lógica puede ser luego revertida al crear los objetos
#* operativos propiamente dichos
#*----------------------------------------------------------------
    def some_operation(self) -> str:

        print("{some_operation()}\n")
        # Primero se llama al método factory para crear un nuevo objeto remito.
        remito = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        #result = f"Ejecución del Creator con {remito.operation()}\n"
        return "{some_operation()} Ejecuta con (%s)" %(remito.operation())


#*-----------------------------------------------------------------------
#* Es necesario hacer implementaciones concretas que reciban el objeto
#* plantilla y le agreguen los métodos y atributos que le sean propios
#*-----------------------------------------------------------------------

class CreatorEnvioCorreo(Creator):
    def factory_method(self) -> remito:
        return EnvioCorreo()


class CreatorEnvioMensajeria(Creator):
    def factory_method(self) -> remito:
        return EnvioMensajeria()

class CreatorPortalVentas(Creator):
    def factory_method(self) -> remito:
        return PortalVentas()

class CreatorRetiraVentanilla(Creator):
    def factory_method(self) -> remito:
        return RetiraVentanilla()

#*------------------------------------------------------------------------------
#* Defino al objeto Remito propiamente dicho
#*-----------------------------------------------------------------------------
class remito(ABC):

    #*-------------------------------------------------------------------------
    #* Esta es una interfaz que define todos los métodos que son comunes a 
    #* los remitos independientemente de como sean enviados
    #*-------------------------------------------------------------------------
    @abstractmethod
    def operation(self) -> str:
        pass


#*-------------------------------------------------------------------------------
#* Ahora defino remitos concretos con su respectiva definición de método de envio
#*-------------------------------------------------------------------------------

class EnvioCorreo(remito):
    def operation(self) -> str:
        return "{Envio por correo}"


class EnvioMensajeria(remito):
    def operation(self) -> str:
        return "{Envio por mensajeria}"

class PortalVentas(remito):
    def operation(self) -> str:
        return "{Portal de ventas}"

class RetiraVentanilla(remito):
    def operation(self) -> str:
        return "{Retira por ventanilla}"


#*-------------------------------------------------------------------------------
#* El código que orquesta empieza con una instancia del Creator (factory) sin
#* definiciones concretas y procede a crearle las subclases de implementación
#* que sean necesarias.
#*-------------------------------------------------------------------------------
def client_code(creator: Creator) -> None:

    print(f"Soy un código que no sé lo que está creando pero invoca a los metodos para hacerlo basado en el creador provisto.\n"
	  f"{creator.some_operation()}",end="")

#*-------------------------------------------------------------------------------
#* Este es el punto de entrada de ejecución (explicito)
#*-------------------------------------------------------------------------------
if __name__ == "__main__":

    os.system("clear")
    print("{%s}\n\n" % (__name__))

    print("Crea primero un remito para ser enviado por correo")
    print("Para hacerlo invoca client_code con el creator específico de Envio por Correo")
    print("Llamará client_code-->CreatorEnvioCorreo-->Creator")
    client_code(CreatorEnvioCorreo())
    print("\n")

    print("Crea un segundo remito")
    client_code(CreatorEnvioCorreo())
    print("\n")

    print("Crea un tercer remito")
    client_code(CreatorEnvioMensajeria())

    print("Crea un cuarto remito")
    client_code(CreatorPortalVentas())

    print("Crea un quinto remito")
    client_code(CreatorRetiraVentanilla())

