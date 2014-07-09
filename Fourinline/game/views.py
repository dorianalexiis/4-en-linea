from django.shortcuts import render_to_response,render
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from forms import *
from models import *
from clases.Juego import Juego
import random

#-----------------INDEX--------------------------------------------------------------
def home(request):
	Mode.objects.all().delete()
	template="index.html"
	return render_to_response(template,context_instance= RequestContext(request,locals()))

#--------------------------------------------#--------------------------------------------
#view add1 donde se agrega el primer jugador
def add1(request,modo):
	modeP=Mode(playerMODE=modo)
	modeP.save()
	Player.objects.all().delete()
	player="PLAYER 1"
	if request.method =="POST":
		form =PlayerForm(request.POST)
		if form.is_valid():
			player=form.save()
			form=PlayerForm()
			if modo == "0":
				return HttpResponseRedirect("/add2/")
			else:
				color=Color.objects.exclude(color=player.color)
				NC = random.randrange(len(color))
				if player.name == "PC":
					PC=Player(name="CPU",color=color[NC])
				else:
					PC=Player(name="PC",color=color[NC])
				PC.save()
				return HttpResponseRedirect("/clear/")
	else:
		form=PlayerForm()
	template="form.html"
	return render_to_response(template,context_instance= RequestContext(request,locals()))
		

#--------------------------------------------#----------------------------------------------
#view add2 donde se agrega el segundo jugador del Juego
def add2(request):
	player="PLAYER 2"
	if request.method =="POST":
		form =PlayerForm(request.POST)
		if form.is_valid():
			player=form.save()
			form=PlayerForm()
			return HttpResponseRedirect("/clear/")
	else:
		form=PlayerForm()
	template="form.html"
	return render_to_response(template,context_instance= RequestContext(request,locals()))

#view para reiniciar casi todas las tablas de la db
def clear(request):
	Topes.objects.all().delete()
	Turno.objects.all().delete()
	Table.objects.all().delete()

	if Mode.objects.all()[0].playerMODE == 0:
		nu=random.randrange(2)
		ju=Player.objects.all()[nu]
		turno=Turno(turno=ju)
	else:
		turno=Turno(turno=Player.objects.all()[0])

	turno.save()

	for i in range(7):
		topes=Topes(column=i)
		topes.save()

	if  Mode.objects.all()[0].playerMODE == 0:
		return HttpResponseRedirect("/modo/")
	else:
		return HttpResponseRedirect("/game/")

#-------------Partida por Puntos-------------------------------------------------------------------------------
#view donde se genera la matriz y todo lo referente al juego 4 in line
def game(request):
	modo = Mode.objects.all()[0]

	juego=Juego(modo.playerMODE)

	juego.AgregarJ1(Player.objects.all()[0].name,Player.objects.all()[0].color.color)
	juego.AgregarJ2(Player.objects.all()[1].name,Player.objects.all()[1].color.color)
	datos=Table.objects.all()
	juego.ConstruirTablero(datos)


	Jugador1=juego.getJ1()
	ColorJ1=juego.getC1()
	Puntaje1=juego.getP1()

	Jugador2=juego.getJ2()
	ColorJ2=juego.getC2()
	Puntaje2=juego.getP2()


	turnoPlayer=Turno.objects.all()[0].turno

	if juego.End():
		if Puntaje1>Puntaje2:
			Ganador="Gandor: "+Jugador1
		else:
			if Puntaje2 > Puntaje1:
				Ganador="Ganador: "+Jugador2
			else:
				Ganador="Juego Empatado"
	M=juego.getMatriz()
	return render_to_response("game.html",locals())


#view para agregar la ficha del jugador que este en turno
def play(request,n):
	#JUEGA AQUI
	modo = Mode.objects.all()[0]

	tope=Topes.objects.get(column=int(n))
	if tope.N >= 0 :
		turno=Turno.objects.all()
		player=Player.objects.get(name=turno[0].turno.name)
		table=Table(Column=tope,row=tope.N,player=player)
		table.save()
		tope.N-=1
		tope.save()
		if modo.playerMODE == 0:
			newTurno=Player.objects.all()
			if newTurno[0].name==turno[0].turno.name :
				turno2=Turno(turno=newTurno[1])
			else:
				turno2=Turno(turno=newTurno[0])
			turno2.save()
			turno[0].delete()
		else:

			juego= Juego(modo.playerMODE)
			juego.AgregarJ1(Player.objects.all()[0].name,Player.objects.all()[0].color.color)
			juego.AgregarJ2(Player.objects.all()[1].name,Player.objects.all()[1].color.color)
			datos=Table.objects.all()
			juego.ConstruirTablero(datos)

			
			ColunmaJ = juego.JugadaIA()

			if ColunmaJ > -1:
				tope2=Topes.objects.get(column=ColunmaJ)
				pc=Player.objects.all()[1]
				if tope2.N >= 0 :
					table2 = Table(Column=tope2,row=tope2.N,player=pc)
					table2.save()
					tope2.N-=1
					tope2.save()
	return HttpResponseRedirect("/game/")

def modo(request):
	template="modo.html"
	return render_to_response(template,context_instance= RequestContext(request,locals()))

#----------Muerte Subita------------------------------------------------------------

#view donde se genera la matriz y todo lo referente al juego 4 in line
def games(request):

	modo = Mode.objects.all()[0]
	juego= Juego(modo.playerMODE)
	juego.AgregarJ1(Player.objects.all()[0].name,Player.objects.all()[0].color.color)
	juego.AgregarJ2(Player.objects.all()[1].name,Player.objects.all()[1].color.color)
	datos=Table.objects.all()
	juego.ConstruirTablero(datos)

	Jugador1=juego.getJ1()
	ColorJ1=juego.getC1()

	Jugador2=juego.getJ2()
	ColorJ2=juego.getC2()

	turnoPlayer=Turno.objects.all()[0].turno
	turnoC=Player.objects.get(name=turnoPlayer)

	
	if juego.End1():
		Ganador="Gandor: "+Jugador1
	elif juego.End2():
		Ganador="Ganador: "+Jugador2
	M=juego.getMatriz()
	return render_to_response("games.html",locals())

#view para agregar la ficha del jugador que este en turno
def plays(request,n):
	#JUEGA AQUI
	modo = Mode.objects.all()[0]
	juego= Juego(modo.playerMODE)
	juego.AgregarJ1(Player.objects.all()[0].name,Player.objects.all()[0].color.color)
	juego.AgregarJ2(Player.objects.all()[1].name,Player.objects.all()[1].color.color)
	datos=Table.objects.all()
	juego.ConstruirTablero(datos)

	if juego.End1() or juego.End2():
		return HttpResponseRedirect("/games/")

	tope=Topes.objects.get(column=int(n))
	if tope.N >= 0 :
		turno=Turno.objects.all()
		player=Player.objects.get(name=turno[0].turno.name)
		table=Table(Column=tope,row=tope.N,player=player)
		table.save()
		tope.N-=1
		tope.save()
		
		newTurno=Player.objects.all()
		if newTurno[0].name==turno[0].turno.name :
			turno2=Turno(turno=newTurno[1])
		else:
			turno2=Turno(turno=newTurno[0])
		turno2.save()
		turno[0].delete()
	return HttpResponseRedirect("/games/")