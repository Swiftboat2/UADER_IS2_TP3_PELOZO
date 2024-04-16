#!/usr/python
import json
import sys

#*--------------------------------------------------
#* newgetJason.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#* adaptado para consigna de trabajo práctico RRR
#*--------------------------------------------------

#
#  --- Se parte del patrón Singleton utilizado en clase
#      La metaclase se deja sin alterar y se usa solo para
#      asegurar una sola instancia
#  
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

#
#   --- Se definen variables de clase
#       conteniendo el blob de datos Json
#

    data = None
    obj  = None

#
#   --- Se carga el archivo en memoria
#
#
    def loadFile(self,jsonFile):
        with open(jsonFile) as myfile:
           self.data=myfile.read()
        self.obj = json.loads(self.data)
#
#   --- Se consulta el archivo
#


    def getToken(self,tk):
        return str(self.obj[tk])

#
#
#   --- Este es el programa llamador
#   --- Respecto a la consigna tanto el nombre de archivo
#       pasado al método loadFile como la clave a consultar con
#       getToken se obtiene desde los argumentos en vez de ser
#       constantes
#


if __name__ == "__main__":
    # The client code.
    s1 = Singleton()
    s1.loadFile("./sitedata.json")
    s=s1.getToken("token1")
    print(s)
