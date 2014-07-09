import random

class Columna():
	fila=[]
	numero=0

class Tablero(object):
	__matriz=list()
	__FIN=0

	def __init__(self):
		self.Vaciar()

	def getMatriz(self):
		M=self.__matriz
		return M

	def Construir(self,datos,J1,J2):
		self.__FIN=len(datos)
		for tab in datos:
			if tab.player.name == J1.getNombre():
				self.__matriz[tab.Column.column].fila[tab.row]=J1.getColor()
			else:
				self.__matriz[tab.Column.column].fila[tab.row]=J2.getColor()

	def Vaciar(self):
		self.__matriz=list()
		for i in range(7):
			rows=list()
			for j in range(6):
				rows.append("white")
			d=Columna()
			d.fila=rows
			d.numero=i
			self.__matriz.append(d)

	def Lleno(self):
		if self.__FIN == 42:
			return True
		else:
			return False

	def Cuatro(self,F):
		punt=self.__Vertical(F)
		if punt > 0:
			return True
		punt=self.__Horizontal(F)
		if punt > 0:
			return True
		punt=self.__DiagonalP(F)
		if punt > 0:
			return True
		punt=self.__DiagonalS(F)
		if punt > 0:
			return True

		return False

	def JugadaIA(self):
		if self.Lleno():
			return -1
		Con=True
		while Con:
			Columna = random.randrange(7)
			Con=self.__columaD(Columna)
		return Columna

	def __columaD(self,Columna):
		j=0
		while j < 6 :
			if self.__matriz[Columna].fila[j] == "white":
				return False
			j+=1
		return True


	

	def Puntuacion(self,F):
		punt=0
		punt+=self.__Vertical(F)
		punt+=self.__Horizontal(F)
		punt+=self.__DiagonalP(F)
		punt+=self.__DiagonalS(F)
		return punt

	def __Vertical(self,F):
		punt=0
		cont=0
		i=0
		while  i < 7:
			j=0
			while j < 6:
				if F == self.__matriz[i].fila[j]:
					cont=0
					while (j < 6) and (F == self.__matriz[i].fila[j]) :
						cont+=1
						j+=1
					if cont > 3:
						punt+=cont-3
				j+=1
			i+=1
		return punt	

	def __Horizontal(self,F):
		punt=0
		cont=0
		i=0
		while  i < 6:
			j=0
			while j < 7:
				if F == self.__matriz[j].fila[i]:
					cont=0
					while (j < 7) and (F == self.__matriz[j].fila[i]) :
						cont+=1
						j+=1
					if cont > 3:
						punt+=cont-3
				j+=1
			i+=1
		return punt	


	def __DiagonalP(self,F):
		punt=0
		for i in range(3):
			ii=0
			j=i
			while(ii<7) and (j<6):
				if self.__matriz[ii].fila[j] == F:
					cont =0
					while (ii<7) and (j<6) and (self.__matriz[ii].fila[j] == F):
						cont+=1
						ii+=1
						j+=1
					if cont > 3:
						punt += cont-3
				else:
					ii+=1
					j+=1

		for i in range(1,4):
			ii=i
			j=0
			while(ii<7) and (j<6):
				if self.__matriz[ii].fila[j] == F:
					cont =0
					while (ii<7) and (j<6) and (self.__matriz[ii].fila[j] == F):
						cont+=1
						ii+=1
						j+=1
					if cont > 3:
						punt += cont-3
				else:
					ii+=1
					j+=1
		return punt


	def __DiagonalS(self,F):
		punt=0
		for i in range(3,7):
			ii=i
			j=0
			while (ii>=0) and (j<6):
				if self.__matriz[ii].fila[j] == F:
					cont =0
					while (ii>=0) and (j<6) and (self.__matriz[ii].fila[j] == F):
						cont+=1
						ii-=1
						j+=1
					if cont > 3:
						punt += cont-3
				else:
					ii-=1
					j+=1
		for i in range(2,4):
			ii=i
			j=5
			while (ii<7) and (j>=0):
				if self.__matriz[ii].fila[j] == F:
					cont =0
					while (ii<7) and (j>=0) and (self.__matriz[ii].fila[j] == F):
						cont+=1
						ii+=1
						j-=1
					if cont > 3:
						punt += cont-3
				else:
					ii+=1
					j-=1	

		return punt

	