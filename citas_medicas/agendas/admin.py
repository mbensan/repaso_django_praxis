from django.contrib import admin
from agendas.models import CentroMedico, Especialista

class CentroMedicoAdmin(admin.ModelAdmin):
  pass

class EspecialistaAdmin(admin.ModelAdmin):
  pass

# Register your models here.
admin.site.register(CentroMedico, CentroMedicoAdmin)
admin.site.register(Especialista, EspecialistaAdmin)