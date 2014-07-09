class Jugador(object):
	__Nombre=""
	__Color=""


	def __init__(self,Nombre,Color):
		self.__Nombre=Nombre
		self.__Color=Color


	def getNombre(self):
		return self.__Nombre

	def getColor(self):
		return self.__Color

