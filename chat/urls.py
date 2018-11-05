from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('front/', views.start_page,name="front"),
    path('front/roomname/', views.index, name='roomname'),
    url(r'^front/roomname/(?P<room_name>[^/]+)/$', views.room, name='room'),



]
