from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    url(r'^logout/$', auth_views.logout, {'next_page': 'login.html'}, name='logout'),
    url(r'^auth/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^$', views.index, name='index'),
]