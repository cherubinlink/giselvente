from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta

# Create your models here.


CHOICES_CMDE = (
    ('Accepter', 'Accepter'),
    ('Livrer', 'Livrer'),
    ('Pas_livrer', 'Pas_livrer'),
    ('Annuler', 'Annuler')
)

STATUS_PRODUIT = (
    ('Nouveaute', 'Nouveaute'),
    ('Top', 'Top'),
    ('Promotion', 'Promotion')
)

CHOICES_VILLE = (
    ('Douala','Douala'),
    ('Yaounde','Yaounde'),
    ('Bafoussam','Bafoussam'),
    ('Edea','Edea'),
    ('Buea','Buea'),
    ('Bameda','Bameda'),
    ('Dschang','Dschang')
)


# categories
class Categorie(models.Model):
    mons_cat = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.noms_cat

# sous categories
class SousCategorie(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom

# info client 
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noms = models.CharField(max_length=200)
    prenoms = models.CharField(max_length=200)
    ville = models.CharField(max_length=200, choices=CHOICES_VILLE)
    telephone = models.CharField(max_length=15)
    quartier = models.CharField(max_length=100)
    
    def __str__(self):
        return self.noms
    
# produit
class Produit(models.Model):
    produit_image = models.ImageField(upload_to='media/produit_image')
    noms_prod = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    cmde_min = models.PositiveIntegerField(default=1)
    dure_vie = models.PositiveIntegerField()
    stocke = models.PositiveIntegerField()
    status_produit = models.CharField(max_length=200, choices=STATUS_PRODUIT)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.noms_prod
    
# panier
class Panier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)  # Date d'ajout à la date

    def est_expire(self):
        expiration_delay = timezone.timedelta(hours=24)  # Exemple: 24 heures d'expiration
        return timezone.now() > self.date_ajout + expiration_delay

    def __str__(self):
        return f"{self.user} - {self.produit} ({self.quantite})"


# commande
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_cmde = models.DateTimeField(auto_now_add=True)
    status_cmde = models.CharField(max_length=200, choices=CHOICES_CMDE)
 
    
# historisques des commandes
class HistoriqueCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_changement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=200, choices=CHOICES_CMDE)
    
    def __str__(self):
        return f"{self.commande.id} - {self.statut} on {self.date_changement}"
    
