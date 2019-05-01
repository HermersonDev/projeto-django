
from django.http.response import HttpResponseForbidden
# Middleware para IPs autorizados

class FiltraIpMiddleware:

	def __init__(self, get_response = None):
		self.get_response = get_response

	def __call__(self, request):
		
		response = self.get_response(request)

		return response

	# Método que é chamado antes da view
	def process_view(self, request, func, args, kwargs):
		# Lista de IPs autorizados
		ips_autorizados = ['127.0.0.1']

		#IP do usuário
		ip = request.META.get('REMOTE_ADDR')

		# Verifica se o Ip do usuário está na lista de IPs autorizados
		if ip not in ips_autorizados :
			# Se ip não autorizado -> HTTP 403 (Não Autorizado)
			return HttpResponseForbidden("IP não autorizado ")

		# Se for autorizado, não faz nada
		return None

