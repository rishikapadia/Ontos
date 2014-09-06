from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework import viewsets
from ontosApp.serializers import UserSerializer

from ontos.settings import STATIC_URL

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


def main(request):
    context = {'STATIC_URL': STATIC_URL}
    return render_to_response(request, 'ontosAppTemplates/main.html', context)


