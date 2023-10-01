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
]
