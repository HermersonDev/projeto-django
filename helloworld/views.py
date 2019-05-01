from django.conf import settings
from django.shortcuts import redirect, render

#from django.views.generic.base import TemplateView

#Class based Views - index
'''
class IndexTemplateView(TemplateView):

	#Nome do template que será utilizado
	template_name = 'website/index.html'

'''

# Méthodo simples para Index

class Helloworld:

	def index(request):

		# Verifica se não existe um usuário autenticado
		if not request.user.is_authenticated :
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

		return render(request, 'website/index.html')