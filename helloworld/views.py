from django.views.generic.base import TemplateView

#Class based Views - index
class IndexTemplateView(TemplateView):

	#Nome do template que será utilizado
	template_name = 'website/index.html'