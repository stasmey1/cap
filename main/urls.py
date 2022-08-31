from django.urls import path
from .views import *

urlpatterns = [
    path('', AllCountries.as_view(), name='training'),
    path('group/<int:pk>/', group, name='group'),
    path('country/<int:pk>/', CountryDetail.as_view(), name='country'),
    path('start_game/', start_game, name='start_game'),
    path('add_country/', AddCountry.as_view(), name='add_country'),
    path('edit_country/<int:pk>/', edit_country, name='edit_country'),
    path('delete_country/<int:pk>/', DeleteCountry.as_view(), name='delete_country'),
    path('search/', search, name='search'),

    path('accounts/profile/', profile, name='profile')
]
