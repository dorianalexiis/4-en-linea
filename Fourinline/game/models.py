from django.db import models

# Create your models here.
class Topes(models.Model):
	column=models.IntegerField(primary_key=True)
	N=models.IntegerField(default=5)


class Color(models.Model):
	color=models.CharField(max_length=40,primary_key=True)
	def __unicode__(self):
		return self.color
			
class Player(models.Model):
	name=models.CharField(max_length=80,primary_key=True)
	color=models.OneToOneField(Color)
	def __unicode__(self):
		return self.name



class Turno(models.Model):
	turno=models.OneToOneField(Player)
	def __unicode__(self):
		return self.turno.name



class Table(models.Model):
	Column=models.ForeignKey(Topes)
	row=models.IntegerField()
	player=models.ForeignKey(Player)

class Mode(models.Model):
	playerMODE=models.IntegerField(primary_key=True)