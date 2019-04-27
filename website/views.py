#libs
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

#Model
from .models import Funcionario
#Form
from .forms import InsereFuncionarioForm



# Class based Views - lista os funcionarios
class FuncionarioListView(ListView):

	# Nome do template que será utilizado
	template_name = 'website/lista.html'
	# Definição do modelo
	model = Funcionario
	"""
		Nome do contexto - array associativo com valores dos atributos
		do modelo funcionario.
	"""
	context_object_name = 'funcionarios'


# Class based Views - Atualizar um fucionário
class FuncionarioUpdateView(UpdateView):

	# Nome do template que será utilizado
	template_name = 'website/atualiza.html'
	# Definição do modelo
	model = Funcionario
	# Definir os campos para atualizar
	fields = '__all__'

	def get_object(self, queryset = None):

		funcionario = None

		# Os campos {pk} e {slug} estão presentes em self.kwargs

		id = self.kwargs.get(self.pk_url_kwarg)

		slug = self;kwargs.get(self.slug_url_kwarg)

		if id is not None :
			# Busca o funcionário apartir do id
			funcionario = Funcionario.objects.filter(id = id).first()

		elif slug is not None :
			# Pega o campo slub do Model
			campo_slug = self.get_slug_field()

			# Busca o funcionario apartir do slug
			funcionario = Funcionario.objects.filter(**{campo_slug : slug}).first()

		return funcionario

# Class based Views - Informações de um fucionário
class FuncionarioDeleteView(DeleteView):

	# Nome do template que será utilizado
	template_name = 'website/exclui.html'
	# Definição do modelo
	model = Funcionario
	"""
		Nome do contexto - array associativo com valores dos atributos
		do modelo funcionario.
	"""
	context_object_name = 'funcionario'
	# Caso a delação for bem sucedida, redireciona para o template 'lista_funcionarios'
	success_url = reverse_lazy('website:lista_funcionarios')

# Class based Views - Cadastro de um fucionário
class FuncionarioCreateView(CreateView):
	
	# Nome do template que será utilizado
	template_name = 'website/cria.html'
	# Definição do modelo
	model = Funcionario
	# Class Form que contém a estrutura dos campos de funcionario
	form_class = InsereFuncionarioForm
	# Caso o cadastro for bem sucedido, redireciona para o template 'lista_funcionarios'
	success_url = reverse_lazy('website:lista_funcionarios')




