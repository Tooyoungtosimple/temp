from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.UserHomePage, name='userhome'),
	url(r'^regist/$', views.UserRegist, name='regist'),
	url(r'^login/', views.UserLogin, name='login'),
	url(r'^inf/(\d{1,2})/$', views.UserInf),
]