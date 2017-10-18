from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from .models import Department, Faculty
from django.http import Http404
from django.shortcuts import render

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

def dashboard(request):
    try:
        department = Department.objects.order_by('name')
        context = {'department': department}
    except Department.DoesNotExist:
        raise Http404("Department entity does not exist")
    return render(request, 'dashboard/index.html', context)
