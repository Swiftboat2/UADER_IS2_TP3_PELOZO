import os
#*-------------------------------------------------------------------------------
#* Ejemplo de decorator pattern
#* Recursión de objetos para agregarle un "wrapper" con sus propios atributos
#* en este caso un estilo de escritura
#*-------------------------------------------------------------------------------

#*--- Esta es la clase que representa el texto original

class WrittenText:

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

#*--- Esta es la clase que la agrega subrayado

class UnderlineWrapper(WrittenText):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

#*--- Esta es la clase que le agrega italics

class ItalicWrapper(WrittenText):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

#*--- Esta es la clase que le agrega bold

class BoldWrapper(WrittenText):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

#*------------------------------------------------------------------------
#* main
#*------------------------------------------------------------------------
if __name__ == '__main__':

	os.system("clear")
	before_txt=WrittenText("UADER_IS2")
	after_txt= ItalicWrapper(UnderlineWrapper(BoldWrapper(before_txt)))

	print("\nAntes ObjectId(%s)--> despues ObjectId(%s)\n" % (before_txt,after_txt))
	print("\nAntes (%s) y despues(%s)\n" % (before_txt.render(),after_txt.render()))

