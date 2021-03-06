from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from .views import Helloworld

#Contém a lista de roteamentos de URLs
urlpatterns = [
	
	#Index
	#path('', IndexTemplateView.as_view(), name = 'index'),

	path('', Helloworld.index, name = 'index'),

	#Inclui as URLs do app 'website'
	path('', include('website.urls', namespace = 'website')),

	#Interface administrativa
	path('admin/', admin.site.urls),
]