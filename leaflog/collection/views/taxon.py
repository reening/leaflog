from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ..forms import TaxonForm
from ..models import Taxon


class ApiTaxonSearchView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')

        if not q:
            return HttpResponseBadRequest()

        taxa = Taxon.objects.filter(display_name__icontains=q)
        results = [ i.to_json() for i in taxa ]

        return JsonResponse({'results': results})

class ApiTaxonGetView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        taxon = get_object_or_404(Taxon, pk=kwargs['pk'])
        return JsonResponse(taxon.to_json())


class TaxonListView(LoginRequiredMixin, ListView):
    queryset = Taxon.objects.filter(parent__isnull=True).order_by('name')
    context_object_name = 'taxa_list'


class TaxonDetailView(LoginRequiredMixin, DetailView):
    model = Taxon


class TaxonCreateView(LoginRequiredMixin, CreateView):
    model = Taxon
    form_class = TaxonForm


class TaxonUpdateView(LoginRequiredMixin, UpdateView):
    model = Taxon
    form_class = TaxonForm


class TaxonDeleteView(LoginRequiredMixin, DeleteView):
    model = Taxon
    success_url = reverse_lazy('taxon-list')
