from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ..forms import LocationForm
from ..models import Location


class LocationListView(LoginRequiredMixin, ListView):
    model = Location


class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('location-list')
