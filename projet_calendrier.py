#Projet fait en décembre 2021

"""
Utilisation : Jour [numéro du mois] Mois [numéro de l'année]
ex : Mardi 21 Décembre 2021
"""


def bissextile(annee):
  if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    return True
  else:
    return False


def nbjoursAnnee(annee):
  if bissextile(annee) == True:
    return 366
  else:
    return 365


def nbjoursMois(mois, annee):
  anneeClassique = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if bissextile(annee):
    anneeClassique[1] += 1
  return anneeClassique[mois - 1]



def ageJours(jour_naissance, mois_naissance, annee_naissance, jour_actuel, mois_actuel, annee_actuel):
  #Afin d'éviter des décalages de jours entre certaines années, nous posons la base des années bissextiles.
  difference = 0
  if annee_naissance == annee_actuel:  #Après de nombreux bugs rajoutant 1 année_naissance complet en plus, de créer une condition retirant 1 année complète du comptage sinon on continue dans la lancée
    if bissextile(annee_naissance):
      difference -= 366
    else:
      difference -= 365
  else:
    for i in range(annee_naissance + 1, annee_actuel):
      if bissextile(i):
        difference += 366
      else:
        difference += 365
    for loop in range(1, mois_actuel):
      difference += nbjoursMois(loop, annee_actuel)
    difference += jour_actuel
    for j in range(12, mois_naissance, -1):
      difference += nbjoursMois(j, annee_naissance)
    difference += nbjoursMois(mois_naissance, annee_naissance) - jour_naissance
    return difference



def dateEnSemaine(jour_semaine, jour_arrivee, mois_arrivee, annee_arrivee, jour_depart, mois_depart, annee_depart):
  jour = ageJours(jour_depart, mois_depart, annee_depart, jour_arrivee, mois_arrivee, annee_arrivee)
  difference = jour % 7
  if difference == 0:
    jour_semaine = [jour_semaine - 1]
  elif difference == 1:
    jour_semaine = [jour_semaine - 2]
  elif difference == 2:
    jour_semaine = [jour_semaine - 3]
  elif difference == 3:
    jour_semaine = [jour_semaine - 4]
  elif difference == 4:
    jour_semaine = [jour_semaine - 5]
  elif difference == 5:
    jour_semaine = [jour_semaine - 6]
  elif difference == 6:
    jour_semaine = [jour_semaine - 7]
  return jour_semaine[0]


def calendrier(annee, today):
  date = today.split()  #On produit une liste permettant de séparer les éléments indiquer par l'utilisateur
  #Jour, numéro du jour, mois, année du calendrier souhaité

  listeMois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août",
            "Septembre", "Octobre", "Novembre", "Décembre"]
  
  listeJours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]


  mois = listeMois.index(date[2])
  mois += 1

  jourSemaine = listeJours.index(date[0])
  jourSemaine += 1

  jour = int(date[1])
  annee = int(date[3])

  
  for loop in range(1, 13):  #Boucle printant les mois de l'année du calendrier en question
    print(listeMois[loop - 1], ":")
    print()
    #Boucle permettant l'affiche de tous les besoins demandées dans ce projet
    for k in range(1, nbjoursMois(loop, annee) + 1):
      print(listeJours[dateEnSemaine(jourSemaine, jour, mois, annee, k, loop, annee)], k, listeMois[loop - 1], annee)
    for loop in range(2):
      print()


sortieAnnee = int(input("Calendrier de l'année: "))
aujourdhui = input("Date d'aujourd'hui: ")
print(calendrier(sortieAnnee, aujourdhui))













#Premier essai de la fonction qui fût non-conluant mais peut être utile à mieux comprendre la démarche
"""
def ageJours(jour_naissance,mois_naissance,année_naissance,jour_actuel,mois_actuel,année_actuel):
  difference=0
  if année_naissance==année_actuel:
    if bissextile(année_naissance):
      difference-=366
    else:
      difference-=365
  else:
    for i in range(année_naissance+1,année_actuel):
      if bissextile(i):
        difference+=366
      else:
        difference+=365

  for loop in range(année_naissance+1,année_actuel):
      difference+=nbjoursAnnee(loop)
  for loop in range(mois_naissance+1,13):
      difference+=nbjoursMois(année_naissance,loop)
  for k in range(1,mois_actuel):
      difference+=nbjoursMois(année_actuel,k)
  
  difference+=nbjoursMois(année_naissance,mois_naissance)-jour_naissance
  difference+=jour_actuel
  return difference
"""
