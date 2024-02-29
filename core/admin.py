from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numleitos', 'andar']


class MedicoConvenioInline(admin.StackedInline):
    model = models.Atende
    extra = 2
    raw_id_fields = ['convenio']


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['crm', 'nome', 'telefone', 'salario', 'ambulatorio']
    inlines = [MedicoConvenioInline]
