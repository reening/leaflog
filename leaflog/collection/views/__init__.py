from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from ..forms import CollectionAuthenticationForm
from ..models import Taxon


class CollectionLoginView(auth_views.LoginView):
    authentication_form = CollectionAuthenticationForm
    template_name = 'collection/login.html'


class CollectionLogoutView(auth_views.LogoutView):
    next_page = '/'


class TaxonListView(LoginRequiredMixin, ListView):
    queryset = Taxon.objects.filter(parent__isnull=True).order_by('name')
    context_object_name = 'taxa_list'


@login_required
def index(request):
    return render(request, 'collection/index.html')


from .location import *
from .taxon import *
