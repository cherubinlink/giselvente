from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from commerce.models import Categorie,SousCategorie,Produit

# Create your views here.



# def accueil(request):
#     return render(request,'commerce/accueil.html')


class AccueiView(View):
    def get(self, request):
        categories = Categorie.objects.all()
        sous_categories = {categorie: categorie.souscategorie_set.all() for categorie in categories}
        produits = Produit.objects.filter(
            (Q(status_produit='Top') | Q(status_produit='Promotion'))
        ).order_by('-id')
        noveau_produit = Produit.objects.filter(status_produit = 'Nouveaute')
        produit_count = produits.count()
        
        context = {
            'categories':categories,
            'sous_categories':sous_categories,
            'produits':produits,
            'nouveau_produit':noveau_produit,
            'produit_count':produit_count
        }
        return render(request,'commerce/accueil.html',context)
    
# detail produit modal
class ProduitDetailView(View):
    def get(self, request, pk):
        produits = get_object_or_404(Produit, id=pk)
        
        context = {
            'produits':produits
        }
        return render(request,'commerce/detail.html',context)
        
    
