from django.conf.urls import url

from . import views

urlpatterns = [
    url ( r'^$', views.a , name = 'index'),
    # url ( r'^$', views.b, name='Login'),
]