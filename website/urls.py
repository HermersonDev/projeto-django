#URLconf app 'website'

#Importação do arquivo de views
from django.urls import path
from .views import *

app_name = 'website'

# Contém a lista de roteamentos de URLs
urlpatterns = [

	# listar os funcionários
	path(
		'funcionarios/', 
		FuncionarioListView.as_view(), 
		name = 'lista_funcionarios'
	),

	# Atualizar funcionário
	# Buscar pelo {id}
	path(
		'funcionario/<pk>',
		FuncionarioUpdateView.as_view(),
		name = 'atualiza_funcionario'
	),
	# Buscar pelo {slug}
	path(
		'funcionario/<slug>',
		FuncionarioUpdateView.as_view(),
		name = 'atualiza_funcionario'
	),

	# Deletar funcionário
	path(
		'funcionario/excluir/<pk>',
		FuncionarioDeleteView.as_view(),
		name = 'deleta_funcionario'
	),

	# Cadastro funcionario
	path(
		'funcionario/cadastrar/',
		FuncionarioCreateView.as_view(),
		name = 'cadastra_funcionario'
	),

	#Login
	path(
		'form-login/',
		UserAuth.form_login,
		name = 'form_login'
	),

	#Login
	path(
		'login/',
		UserAuth.login,
		name = 'login'
	),

	#Logout
	path(
		'logout/',
		UserAuth.logout,
		name = 'logout'
	),
]

