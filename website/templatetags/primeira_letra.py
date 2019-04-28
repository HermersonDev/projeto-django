# Filtro para recuperar a primeira letra de um valor

from django import template
from django.template.defaultfilters import stringfilter

# Coleta uma instãncia da biblioteca de filtros e tags do Django
register = template.Library()


@register.filter # Registra esse arquivo como um filtro
@stringfilter # Defini o tipo de valor(string) esperado pelo filtro
def primeira_letra(value):
	# Convert a string em lista e coleta o valor do indice zero(o primeiro caracter)
	return list(value)[0]