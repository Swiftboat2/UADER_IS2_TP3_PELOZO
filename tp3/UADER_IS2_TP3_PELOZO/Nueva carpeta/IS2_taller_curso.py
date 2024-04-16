
import os
#*--------------------------------------------------------------------
#* Ejemplo de taller para patrón visitor
#*--------------------------------------------------------------------

class Cursos_FCyT:

	def accept(self, visitor):
		visitor.visit(self)

#*------------ Recibe puntero a objetos pero no sabe si son maestros o alumnos
#*------------ Los define en tiempo real

	def teaching(self, visitor):
		print(self, "Enseñado por ", visitor)

	def studying(self, visitor):
		print(self, "Estudiado por ", visitor)

#*------------ Muestra el nombre de la clase

	def __str__(self):
		return self.__class__.__name__


class IS1(Cursos_FCyT): pass
class IS2(Cursos_FCyT): pass
class MATE1(Cursos_FCyT): pass


class Visitor:

	def __str__(self):
		return self.__class__.__name__


#*------ Si es un instructor el método .visit indica que enseña
class Profesor(Visitor):
	def visit(self, crop):
		crop.teaching(self)


#*----- Si es un alumno el método .visit indica que aprende
class Alumno(Visitor):
	def visit(self, crop):
		crop.studying(self)


#*---------------- main

os.system("clear")

#*----- Crea cursos

print("\nCrea cursos")
is1 = IS1()
is2 = IS2()
mate1 = MATE1()

#*----- Crea visitantes genericos

print("\nCrea instructor y estudiante")
instructor = Profesor()
student = Alumno()

#*----- Aplica los visitantes a las clases, su naturaleza está
#*----- determinado por la clase

print("\nAplica instructor y estudiante a los diferentes cursos")
print("\nIS1")
is1.accept(instructor)
is1.accept(student)

print("\nIS2")
is2.accept(instructor)
is2.accept(student)

print("\nMate 1")
mate1.accept(instructor)
mate1.accept(student)

