import json
import random
from datetime import datetime


# Lire Json :
def charger_recettes():
    with open("recipes.json", "r", encoding="UTF-8") as f:
        return json.load(f)


# -------> UTILISATEUR :

# PILIER  "MOI" (Identité) ALLERGENE RESTRICTION REGIME ALIMENTAIRE


def demander_allergene():
    print("Avez vous des allergies ? ")
    print("1 - Gluten")
    print("2-Fruits à coques")
    print("3 - Crustacés")
    print("4 - Oeufs")
    print("5 - Poissons")
    print("6 - Soja")
    print("7 - Lait")
    print("8 - Arachides")

    choix_allergene = input("Avez vous des allergenes  (choix 1 à 8 ) ? ")

    match choix_allergene:
        case "1":
            return "Gluten"
        case "2":
            return "Fruits à coques"
        case "3":
            return "Crustacés"
        case "4":
            return "Oeufs"
        case "5":
            return "Poissons"
        case "6":
            return "Soja"
        case "7":
            return "Lait"
        case "8":
            return "Arachides"
        case _:
            return None


def demander_regime_particulier():
    print("Avez-vous un regime alimentaire particulier ? ")
    print("1 - Végétarien -Veggie")
    print("2- Végétalien- 100% Végétal")
    print("3 - Remise en forme - Light")
    print("4 - Sportif - riche en proteines")
    print("5 - Bébé - Premier âge")
    print("6 - Gourmand - Cheat meal ")
    choix_regime = input("Quel est votre régime spécifique ?(choix 1/6)")

    match choix_regime:
        case "1":
            return "Végétarien"
        case "2":
            return "Végétalien"
        case "3":
            return "Remise en forme"
        case "4":
            return "Sportif"
        case "5":
            return "Bébé"
        case "6":
            return "Gourmand"
        case "7":
            return "Lait"
        case "8":
            return "Arachides"
        case _:
            return None


def demander_restrictions():
    print("Avez-vous des restrictions alimentaire ? ")
    print("1 - Sans porc")
    print("2-  Halal")
    print("3 - Kasher")
    choix_restrictions = input("Quel sont vos restrictions?(choix 1/6)")

    match choix_restrictions:
        case "1":
            return "Sans porc"
        case "2":
            return "Halal"
        case "3":
            return "Kasher"
        case _:
            return None


# PILIER "MON MOMENT" (Logistique) : Temps disponible, Vaisselle, Budget#


def demander_nombre_repas():
    print("Combien de repas voulez-vous /semaine ?")
    print("1- 5repas")
    print("2- 7 repas")
    print("3- 10 repas")
    print("4 - 14 repas ")
    choix_frequence = input("Combien de repas ? (choix 1/4)")

    match choix_frequence:
        case "1":
            return 5
        case "2":
            return 7
        case "3":
            return 10
        case "4":
            return 14


def demander_budget():
    print("Quel est votre budget ?")
    print("1 - Prix malin")
    print("2 - Petit plaisir")
    choix_budget = input("Quel est votre buget ? (choix 1/2)")

    match choix_budget:
        case "1":
            return "Prix malin"
        case "2":
            return "Petit plaisir"
        case _:
            return None


def demander_temps_utilisateur():
    print("Combien de temps as-tu ?")
    print("1 - Je suis pressé (10 min)")
    print("2 - J'ai un peu de temps (20 min)")
    print("3 - Je prends mon temps (30 min et +)")

    choix_utilisateur = input("Quel est ton choix 1,2,3 ?")

    match choix_utilisateur:
        case "1":
            return 10
        case "2":
            return 20
        case "3":
            return 999  # inclus tout
        case _:
            return None


def demander_energie():
    print("Ton état d'esprit")
    print("1 - Énergie Zéro (Zéro vaisselle, zéro cuisson)")
    print("2 - Efficace (Une seule poêle / casserole)")
    print("3 - Chef cuistot (Je suis motivé, peu importe la vaisselle !)")

    choix_energie = input("Réponse (1, 2 ou 3) : ")
    match choix_energie:
        case "1":
            return "Energie Zéro"
        case "2":
            return "Efficace"
        case "3":
            return "Chef cuistot"
        case _:
            return None


# PILIER "MA PLANETE" (Valeurs) : Saison, Organition(Zéro Gâchis), Local
def demander_organisation():
    print("Quel est votre préference ?")
    print("1- Famille nombreuse")
    print("2- Zero gachis")
    choix_orga = input("Quel est votre ")

    match choix_orga:
        case "1":
            return "Famille nombreuse"
        case "2":
            return "Zero gachis"
        case _:
            return None


def obtenir_saison_actuelle():
    maintenant = datetime.now()
    numero_mois = maintenant.month
    match numero_mois:
        case 3 | 4 | 5:
            return "printemps"
        case 6 | 7 | 8:
            return "été"
        case 9 | 10 | 11:
            return "automne"
        case 12 | 1 | 2:
            return "hiver"
        case _:
            return "Erreur : mois inconnu"


def demander_exigence_planete():
    print("Impact Planète")
    print("1 - Peu importe")
    print("2 - Je veux des recettes avec un bon score (Éco-responsable)")
    print("3 - Champion de la planète uniquement (Score maximum)")
    choix_planete = input("Votre choix (1, 2 ou 3) : ")
    return choix_planete


# ----------> FONCTION FILTRAGE :
# --------->>>PILIER  "MOI" (Identité) ALLERGENE RESTRICTION REGIME ALIMENTAIRE<<<--------#
# Filtrer par allergene


def filtrer_par_allergene(liste_a_trier, allergene_exclu):
    if allergene_exclu is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if allergene_exclu not in recette["allergènes"]:
            resultat.append(recette)
    return resultat


# Filtrer Restriction
def filtrer_par_restrication(liste_a_trier, choix_utilisateur):
    if choix_utilisateur is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if choix_utilisateur in recette["restrictions"]:
            resultat.append(recette)
    return resultat


# Filtrer regimes particulier
def filtrer_par_regime(liste_a_trier, regime):
    if regime is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if regime in recette["regime"]:
            resultat.append(recette)
    return resultat


# --------------> PILIER "MON MOMENT" (Logistique) : Temps disponible, Vaisselle, Budget<---#


# Filtrer Temps de preparation
def filtrer_par_temps(liste_a_trier, temps_max):
    resultat = []

    for recette in liste_a_trier:
        if recette["temps"] <= temps_max:
            resultat.append(recette)
    return resultat


# Filtrer Budget
def filtrer_par_budget(liste_a_trier, prix):
    if prix is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if recette["budget"] == prix:
            resultat.append(recette)
    return resultat


# Filtrer Vaisselle:
def filtrer_vaisselle(liste_a_trier, energie):
    if energie is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if recette["energie"] == energie:
            resultat.append(recette)
    return resultat


# ---------> PILIER "MA PLANETE" (Valeurs) : Saison, Zéro Gâchis, Local <----------#
# Filtrer Saison :
def saison(liste_complete, obtenir_saison_actuelle):
    resultat = []
    for recette in liste_complete:
        if (
            recette["saison"] == obtenir_saison_actuelle
            or recette["saison"] == "toutes"
        ):
            resultat.append(recette)
    return resultat


# Filtrer Organisation :
def filtrer_organisation(liste_a_trier, choix_orga):
    if choix_orga is None:
        return liste_a_trier
    resultat = []
    for recette in liste_a_trier:
        if recette["organisation"] == choix_orga:
            resultat.append(recette)
    return resultat


# Filtrer score planete :
def calculer_score(recette, saison_actuelle):
    score = 0
    if recette["saison"] == saison_actuelle:
        score += 1

    # Point 2 : Est-ce local ?
    if recette.get("est_local") == True:
        score += 1

    # Point 3 : Est-ce Zéro Gâchis ?
    if recette.get("organisation") == "Zero gachis":
        score += 1

    return score


def trier_par_planete(liste_filtree, saison_actuelle):
    # La fonction sorted a besoin d'une "key" (le critère de tri)
    # reverse=True sert à mettre les plus gros scores en premier
    liste_triee = sorted(
        liste_filtree, key=lambda r: calculer_score(r, saison_actuelle), reverse=True
    )

    return liste_triee


# -----------> Moteur:

# 1. INITIALISATION


liste_resultat = charger_recettes()
saison_actuelle = obtenir_saison_actuelle()
# 2. COLLECTE DES INFOS (Tes fonctions "demander_...")
choix_allergene = demander_allergene()
choix_budget = demander_budget()
choix_temps = demander_temps_utilisateur()
choix_regime = demander_regime_particulier()
choix_restrictions = demander_restrictions()
choix_utilisateur = demander_temps_utilisateur()
choix_energie = demander_energie()
choix_orga = demander_organisation()
choix_planete = demander_exigence_planete()

# 3. L'ENTONNOIR DE FILTRAGE (Tes fonctions "filtrer_...")
# Chaque ligne réduit la liste obtenue à la ligne précédente
liste_resultat = filtrer_par_allergene(liste_resultat, choix_allergene)
liste_resultat = filtrer_par_restrication(liste_resultat, choix_restrictions)
liste_resultat = filtrer_par_regime(liste_resultat, choix_regime)

liste_resultat = filtrer_par_temps(liste_resultat, str(choix_utilisateur))
liste_resultat = filtrer_par_budget(liste_resultat, choix_budget)
liste_resultat = filtrer_vaisselle(liste_resultat, choix_energie)

liste_resultat = filtrer_organisation(liste_resultat, choix_orga)
liste_resultat = trier_par_planete(liste_resultat, choix_planete)

# 4. L'INTELLIGENCE (Le tri)
liste_resultat = trier_par_planete(liste_resultat, saison_actuelle)
nb_repas_voulu = demander_nombre_repas()


# 5. L'AFFICHAGE DU RÉSULTAT
def affichage(nombre_a_afficher):

    if len(liste_resultat) > 0:
        menu_final = liste_resultat[:nombre_a_afficher]
        for recette in menu_final:
            score = calculer_score(recette, saison_actuelle)
            print(
                f"- {recette['nom']} | Temps: {recette['temps']} min | Score Planète: {score}/3"
            )
    else:
        print(" Désolé, aucune recette ne correspond à tous vos critères.")


affichage(nb_repas_voulu)
