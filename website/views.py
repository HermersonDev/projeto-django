#libs
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Usado em class para o requerimento de login
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings

#Model
from .models import Funcionario
#Form
from .forms import InsereFuncionarioForm



# Class based Views - lista os funcionarios
class FuncionarioListView(LoginRequiredMixin, ListView):

	# Definição do URL para o template de login
	login_url = settings.LOGIN_URL

	# Depois de efetuar redireciona para o template de FuncionarioListView
	redirect_field_name = 'website:lista_funcionarios'

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
class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):

	# Definição do URL para o template de login
	login_url = settings.LOGIN_URL

	# Depois de efetuar redireciona para o template de FuncionarioUpdateView
	redirect_field_name = 'website:lista_funcionarios'

	# Nome do template que será utilizado
	template_name = 'website/atualiza.html'
	# Definição do modelo
	model = Funcionario

	# Definir os campos para atualizar
	fields = '__all__'

	success_url = reverse_lazy('website:lista_funcionarios')

	def get_object(self, queryset = None):

		funcionario = None

		# Os campos {pk} e {slug} estão presentes em self.kwargs

		pk = self.kwargs.get(self.pk_url_kwarg)

		slug = self.kwargs.get(self.slug_url_kwarg)

		if pk is not None :
			# Busca o funcionário apartir do id
			funcionario = Funcionario.objetos.filter(id = pk).first()

		elif slug is not None :
			# Pega o campo slub do Model
			campo_slug = self.get_slug_field()

			# Busca o funcionario apartir do slug
			funcionario = Funcionario.objetos.filter(**{campo_slug : slug}).first()

		return funcionario


# Class based Views - Informações de um fucionário
class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):

	# Definição do URL para o template de login
	login_url = settings.LOGIN_URL

	# Depois de efetuar redireciona para o template de FuncionarioDeleteView
	redirect_field_name = 'website:lista_funcionarios'

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
class FuncionarioCreateView(LoginRequiredMixin, CreateView):

	# Definição do URL para o template de login
	login_url = settings.LOGIN_URL
	
	# Depois de efetuar redireciona para o template de FuncionarioCreateView
	redirect_field_name = 'website:cadastra_funcionario'

	# Nome do template que será utilizado
	template_name = 'website/cria.html'
	# Definição do modelo
	model = Funcionario
	# Class Form que contém a estrutura dos campos de funcionario
	form_class = InsereFuncionarioForm
	# Caso o cadastro for bem sucedido, redireciona para o template 'lista_funcionarios'
	success_url = reverse_lazy('website:lista_funcionarios')

	


# Autenticação
class UserAuth:

	def form_login(request):
		return render(request, 'website/login.html')

	def login(request):
			
		# Coleta os dados via POST
		username = request.POST['username']
		password = request.POST['password']

		# Autentica o usuário
		user = authenticate(request, username = username, password = password)

		#Verifica se a variavel 'user' contém um Objeto User
		if user is not None :
			# Efetua o login na aplicação e redireciona para index
			login(request, user)
			return redirect('index');
		else:
			return render(request, 'website/login.html', { 
				'error' : 'Username ou password incorreto !' 
			})

	
	@login_required # Decorador login requerido
	def logout(request):
		# Efetua o logout do Usuário
		logout(request)
		return redirect('index')








