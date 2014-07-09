from Tablero import Tablero
from Jugador import Jugador

class Juego(object):
	modo=0

	def __init__(self,n):
		self.__tablero=Tablero()
		self.modo=n

	def AgregarJ1(self,Nombre,Color):
		self.__J1=Jugador(Nombre,Color)

	def AgregarJ2(self,Nombre,Color):
		self.__J2=Jugador(Nombre,Color)

	def getJ1(self):
		return self.__J1.getNombre()

	def getJ2(self):
		return self.__J2.getNombre()

	def getC1(self):
		return self.__J1.getColor()

	def getC2(self):
		return self.__J2.getColor()

	def getP1(self):
		return self.__tablero.Puntuacion(self.__J1.getColor())

	def getP2(self):
		return self.__tablero.Puntuacion(self.__J2.getColor())

	def End(self):
		return self.__tablero.Lleno()

	def End1(self):
		if self.__tablero.Cuatro(self.__J1.getColor()):
			return True
		return False

	def End2(self):
		if self.__tablero.Cuatro(self.__J2.getColor()):
			return True
		return False

	def getMatriz(self):
		return self.__tablero.getMatriz()

	def ConstruirTablero(self,datos):
		self.__tablero.Construir(datos,self.__J1,self.__J2)

	def JugadaIA(self):
		return self.__tablero.JugadaIA()