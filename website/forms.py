#Definindo a estrutura do Formulário do Funcionário

from django import forms
from .models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):

	#Campos adicionais

	"""
	chefe = forms.BooleanField(label = 'Chefe?', required = True)

	biografia = forms.CharField(
		label = 'Biografia',
		required = False,
		widget = forms.Textarea
	)
	"""


	#Definição dos campos que serão mostrados no formulário
	class Meta:

		#Modelo base
		model = Funcionario

		#Campos que estarão no formulário
		fields = [
			'nome',
			'sobrenome',
			'cpf',
			'tempo_de_servico',
			'remuneracao',

		]
		#Campos que não estarão no formulário
		exclude = [
			
		]



"""
class InsereFuncionarioForm(forms.form):

	#Campo nome
	nome = forms.CharField(required = True, max_length = 255)
	#Campo sobrenome
	sobrenome = forms.CharField(required = True, max_length = 255)
	#Campo cpf
	cpf = forms.CharField(required = True, max_length = 14)
	#Campo tempo de serviço
	tempo_de_servico = forms.IntegerField(required = True)
	#Campo remuneração
	remuneracao = forms.DecimalField()
"""