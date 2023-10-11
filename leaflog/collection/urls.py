from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('login', views.CollectionLoginView.as_view(), name='login'),
    path('logout', views.CollectionLogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),

    path('location/', views.LocationListView.as_view(), name='location-list'),
    path('location/new', views.LocationCreateView.as_view(), name='location-create'),
    path('location/<slug:slug>/', views.LocationDetailView.as_view(), name='location-detail'),
    path('location/<slug:slug>/edit', views.LocationUpdateView.as_view(), name='location-update'),
    path('location/<slug:slug>/delete', views.LocationDeleteView.as_view(), name='location-delete'),

    path('taxon/', views.TaxonListView.as_view(), name='taxon-list'),
    path('taxon/new', views.TaxonCreateView.as_view(), name='taxon-create'),
    path('taxon/<int:pk>/', views.TaxonDetailView.as_view(), name='taxon-detail'),
    path('taxon/<int:pk>/edit', views.TaxonUpdateView.as_view(), name='taxon-update'),
    path('taxon/<int:pk>/delete', views.TaxonDeleteView.as_view(), name='taxon-delete'),

    path('accession/', views.AccessionListView.as_view(), name='accession-list'),
    path('accession/new', views.AccessionCreateView.as_view(), name='accession-create'),
    path('accession/<int:pk>/', views.AccessionDetailView.as_view(), name='accession-detail'),
    path('accession/<int:pk>/edit', views.AccessionUpdateView.as_view(), name='accession-update'),
    path('accession/<int:pk>/delete', views.AccessionDeleteView.as_view(), name='accession-delete'),

    path('api/taxon/search', views.ApiTaxonSearchView.as_view(), name='api-taxon-search'),
    path('api/taxon/<int:pk>', views.ApiTaxonGetView.as_view(), name='api-taxon-get'),
]
