from django.contrib import admin
from commerce.models import Categorie,SousCategorie,Client,Produit,Commande,Panier,HistoriqueCommande,Message
# Register your models here.


@admin.register(Categorie)
class CategorieModelAdmin(admin.ModelAdmin):
    list_display = ['mons_cat']
    
@admin.register(SousCategorie)
class SousCategorieModelAdmin(admin.ModelAdmin):
    list_display = ['categorie','nom']


@admin.register(Client)
class ClientModelaAdmin(admin.ModelAdmin):
    list_display = ['user','noms','prenoms','ville','telephone','quartier']
    

@admin.register(Produit)
class ProduitModelAdmin(admin.ModelAdmin):
    list_display = ['noms_prod','produit_image','prix','description','stocke','status_produit']


@admin.register(Commande)
class CommandeMOdelAdmin(admin.ModelAdmin):
    list_display = ['user','client','produit','quantite','date_cmde','status_cmde']
    

@admin.register(Panier)
class PanierModelAdmin(admin.ModelAdmin):
    list_display = ['user','produit','quantite','date_ajout']
    

@admin.register(HistoriqueCommande)
class HistorisqueCommandeModelAdmin(admin.ModelAdmin):
    list_display = ['commande','date_changement','statut']


@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['user','produit','comment','note','date_msg']
