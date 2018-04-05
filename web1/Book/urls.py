from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.BookHomePage, name='bookhome'),
	url(r'^test/$', views.test, name='test'),
	url(r'^show/$', views.showImg, name='show'),
	url(r'^booksub/$', views.BookSub, name='booksub'),
	url(r'^indentsub/$', views.IndentSub, name='indentsub'),
	url(r'^bookdonate/(?P<user>\d{11})/(?P<check>\d{1,2})/$', views.BookDonate, name='bookdonate'),
]