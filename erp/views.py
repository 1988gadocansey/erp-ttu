from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from .models import Department, Faculty
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import account.views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class SignupView(account.views.SignupView):

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
        profile.some_attr = "some value"
        profile.save()
@login_required
def dashboard(request):
    try:
        department = Department.objects.order_by('name')
        context = {'department': department}
    except Department.DoesNotExist:
        raise Http404("Department entity does not exist")
    return render(request, 'dashboard/index.html', context)
