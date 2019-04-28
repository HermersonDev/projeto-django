# Tag para mostrar o horário atual
from datetime import datetime as dt 
from django import template

# Coleta uma instãncia da biblioteca de filtros e tags do Django
register = template.Library()


@register.simple_tag # Defini como uma tag simples
def tempo_atual():
	# Coleta o tempo atual e formata para o formato horas:minutos:segundos
	return dt.now().strftime('%H:%M:%S') 