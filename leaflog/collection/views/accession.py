from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ..forms import AccessionForm
from ..models import Accession


class AccessionListView(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = Accession


class AccessionDetailView(LoginRequiredMixin, DetailView):
    model = Accession


class AccessionCreateView(LoginRequiredMixin, CreateView):
    model = Accession
    form_class = AccessionForm


class AccessionUpdateView(LoginRequiredMixin, UpdateView):
    model = Accession
    form_class = AccessionForm


class AccessionDeleteView(LoginRequiredMixin, DeleteView):
    model = Accession
    success_url = reverse_lazy('accession-list')
