from django.urls import path
from commerce import views


urlpatterns = [
    path('',views.accueil,name='accueil')
]
