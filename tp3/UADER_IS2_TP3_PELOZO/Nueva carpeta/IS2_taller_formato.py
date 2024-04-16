#!/usr/python
import os
import sys
#*--------------------------------------------------------------------
#* Implementación de chain of responsibility gestiona formatos
#* de impresión
#*--------------------------------------------------------------------
class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        if self.nextHandler == None:
           print("La lista de actuadores se ha terminado, no se puede resolver el formato")
           return
        self.nextHandler.handle(request)

#*-------------------------------- PDF Handler

class PDFHandler(Handler):

    def handle(self, request):
        print("Handler PDF: explora pedido de impresión formato(%s)" % request.format_)
        if request.format_ == "pdf":
            self.output_report(request.title, request.text)
        else:
            print("Handler PDF: pasa al siguiente actuador")
            super(PDFHandler, self).handle(request)

    def output_report(self, title, text):
        print ('\n<html>')
        print ('  <head>')
        print ('    <title>%s</title>' % title)
        print ('  </head>')
        print ('  <body>')
        print ('  <p>%s</p>' % text)
        print ('  </body>')
        print ('</html>\n')

#*-------------------------------- TXT Handler

class TextHandler(Handler):

    def handle(self, request):
        print("Handler TXT: explora pedido de impresión formato(%s)" % request.format_)
        if request.format_ == "txt":
            self.output_report(request.title, request.text)
        else:
            print("Handler TXT: pasa al siguiente actuador")
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print ('\n'+5*'*' + title + 5*'*')
        print ("%s" % (text))
        print ("")
#*-------------------------------- MS-Word Handler

class DocHandler(Handler):

    def handle(self, request):
        print("Handler DOC: explora pedido de impresión formato(%s)" % request.format_)
        if request.format_ == "doc":
            self.output_report(request.title, request.text)
        else:
            print("Handler DOC: pasa al siguiente actuador")
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print ('\n'+5*'*' + title + 5*'*')
        print ("MS-Word file text(%s)" % (text))
        print ("\n")
#*-------------------------------- Word Handler

class ErrorHandler(Handler):

    def handle(self, request):
        print ("Invalid request")


#*-----------------------------------------------------------------
#* Ejemplo de código cliente donde es creado un objeto que
#* simula un reporte
#*----------------------------------------------------------------
class Report(object):
    """Strategy context."""

    def __init__(self, _title, _text, _format):
        self.title = _title
        self.text = _text
        self.format_ = _format



if __name__ == '__main__':

    os.system("clear")
#*---------------------------------------------------------------
#* Inicializa los actuadores de formatos conocidos
#*---------------------------------------------------------------
    pdf_handler = PDFHandler()
    text_handler = TextHandler()
    doc_handler = DocHandler()

#*---- Establece ahora la cadena de llamada

    pdf_handler.nextHandler = text_handler


#*---------------------------------------------------------------
#* Crea un reporte
#*---------------------------------------------------------------
    print("Ejecutando programa %s\n" % (sys.argv[0]))
    print("Archivo a imprimir %s\n" % (sys.argv[1]))
    filename=sys.argv[1].split('.')
    print("\nEnvia a imprimir un archivo en formato %s (solo actuadores .pdf y .txt)\n" % (filename[1]))   
    report = Report("Reporte mensual de ventas","Las ventas del mes han subido un 3%",filename[1])

#*---- Lo envia a la cadena de responsabilidad para que lo procese

    pdf_handler.handle(report)

#*--- Agrega un nuevo actuador y vuelve a enviar

    print("\nAgrega un nuevo actuador para .DOC y vuelve a enviar\n")
    text_handler.nextHandler = DocHandler()
    pdf_handler.handle(report)
