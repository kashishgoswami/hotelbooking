from django.conf.urls import url

from . import views

urlpatterns = [
    # url ( r'^$', views.a , name = 'index'),
    # url ( r'^$', views.room, name='Room'),
    url ( r'^$',views.room_detail_view, name='room deus'),
]   