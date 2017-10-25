from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Auth
    url(r'^', include(router.urls)),

    url(r'^logout/$', auth_views.logout, {'next_page': '/erp'}, name='logout'),
    url(r'^auth/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^metrics/', include(router.urls)),
    url(r"^account/signup/$",views.SignupView.as_view(), name="account_signup"),
url(r"^account/", include("account.urls")),

]