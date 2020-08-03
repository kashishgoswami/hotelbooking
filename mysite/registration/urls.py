from django.conf.urls import url

from . import views

urlpatterns = [
    # url ( r'^$', views.register_view , name = 'index'),
    url ( r'^$', views.register, name='Registeration'),
]