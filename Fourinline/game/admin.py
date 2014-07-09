from django.contrib import admin
from models import *
# Register your models here.
		

class TopesAdmin(admin.ModelAdmin):
	list_display = ('column','N',)

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name','color',)

class ColorAdmin(admin.ModelAdmin):
	list_display = ('color',)

class TurnoAdmin(admin.ModelAdmin):
	list_display = ('turno',)

class TableAdmin(admin.ModelAdmin):
	list_display = ('Column','row','player',)

class ModeAdmin(admin.ModelAdmin):
	list_display = ('playerMODE',)

admin.site.register(Player,PlayerAdmin)
admin.site.register(Topes,TopesAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Turno,TurnoAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Mode,ModeAdmin)