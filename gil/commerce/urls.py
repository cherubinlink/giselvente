from django.urls import path
from commerce import views


urlpatterns = [
    path('',views.AccueiView.as_view(),name='accueil'),
    
    # detail produit
    path('detail_produit/<int:pk>/',views.ProduitDetailView.as_view(), name='detail-produit'),
]
