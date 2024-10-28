from django.contrib import admin
from commerce.models import Categorie,SousCategorie,Client,Produit,Commande,Panier,HistoriqueCommande
# Register your models here.


@admin.register(Categorie)
class CategorieModelAdmin(admin.ModelAdmin):
    list_display = ['mons_cat']
