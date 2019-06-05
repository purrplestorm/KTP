from django.contrib import admin
from django.urls import path
import articles
from articles import views
from django.conf.urls import url
admin.autodiscover()

urlpatterns = [
               
    url(r'^archive/', views.archive, name='archive'),
    url(r'^admin/', admin.site.urls),
    url(r'^article/(?P<article_id>\d+)/$', views.get_article, name='get_article'),
    url(r'^article/new', views.create_post, name = 'create_post'),
    
               
    url(r'^registration', views.create_user, name = 'create_user'),
    url(r'^login', views.login_user, name = 'login_user'),
    url(r'^test', views.test, name = 'test'),
]
