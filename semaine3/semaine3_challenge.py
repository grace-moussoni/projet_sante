#------------------------------------------------------------------------------------
# PROGRAMME DATA SCIENCE - AKIENI ACADEMY
# Fichier : semaine3_challenge.py
# Objectif : Rapport d'état sanitaire comparé pour le Conseil des Ministres

#------------------------------------------------------------------------------------
# 1. DÉCLARATION DES DONNÉES BRUTES DES 5 HÔPITAUX
# CHU Brazzaville
h1_nom = "CHU Brazzaville"
h1_lits_totaux = 320
h1_lits_occupes = 298
h1_medecins = 47
h1_ruptures = 2
h1_alertes = 2

# Hôpital Pointe-Noire
h2_nom = "Hopital Pointe-Noire"
h2_lits_totaux = 180
h2_lits_occupes = 143
h2_medecins = 22
h2_ruptures = 0
h2_alertes = 1

# Hôpital Dolisie
h3_nom = "Hopital Dolisie"
h3_lits_totaux = 95
h3_lits_occupes = 91
h3_medecins = 8
h3_ruptures = 1
h3_alertes = 2

# Hôpital Owando
h4_nom = "Hopital Owando"
h4_lits_totaux = 45
h4_lits_occupes = 32
h4_medecins = 3
h4_ruptures = 3
h4_alertes = 0

# CMS Impfondo
h5_nom = "CMS Impfondo"
h5_lits_totaux = 20
h5_lits_occupes = 19
h5_medecins = 1
h5_ruptures = 2
h5_alertes = 1

#------------------------------------------------------------------------------------
# 2. TRAITEMENT ET LOGIQUE DE CLASSIFICATION (IF/ELIF/ELSE)

# HÔPITAL 1 : CHU Brazzaville
h1_taux = (h1_lits_occupes / h1_lits_totaux) * 100
if h1_taux > 95: h1_tag_occ = "CRI"
elif h1_taux > 85: h1_tag_occ = "ALT"
else: h1_tag_occ = "OK "

if h1_ruptures >= 2 or h1_taux > 95:
    h1_niveau = "CRITIQUE"
elif h1_ruptures >= 1 or h1_taux > 85 or (h1_alertes >= 2 and h1_medecins < 5):
    h1_niveau = "PREOCCUPANT"
else:
    h1_niveau = "SATISFAISANT"

# -HÔPITAL 2 : Hôpital Pointe-Noire
h2_taux = (h2_lits_occupes / h2_lits_totaux) * 100
if h2_taux > 95: h2_tag_occ = "CRI"
elif h2_taux > 85: h2_tag_occ = "ALT"
else: h2_tag_occ = "OK "

if h2_ruptures >= 2 or h2_taux > 95:
    h2_niveau = "CRITIQUE"
elif h2_ruptures >= 1 or h2_taux > 85 or (h2_alertes >= 2 and h2_medecins < 5):
    h2_niveau = "PREOCCUPANT"
else:
    h2_niveau = "SATISFAISANT"

# HÔPITAL 3 : Hôpital Dolisie
h3_taux = (h3_lits_occupes / h3_lits_totaux) * 100
if h3_taux > 95: h3_tag_occ = "CRI"
elif h3_taux > 85: h3_tag_occ = "ALT"
else: h3_tag_occ = "OK "

if h3_ruptures >= 2 or h3_taux > 95:
    h3_niveau = "CRITIQUE"
elif h3_ruptures >= 1 or h3_taux > 85 or (h3_alertes >= 2 and h3_medecins < 5):
    h3_niveau = "PREOCCUPANT"
else:
    h3_niveau = "SATISFAISANT"

# HÔPITAL 4 : Hôpital Owando
h4_taux = (h4_lits_occupes / h4_lits_totaux) * 100
if h4_taux > 95: h4_tag_occ = "CRI"
elif h4_taux > 85: h4_tag_occ = "ALT"
else: h4_tag_occ = "OK "

if h4_ruptures >= 2 or h4_taux > 95:
    h4_niveau = "CRITIQUE"
elif h4_ruptures >= 1 or h4_taux > 85 or (h4_alertes >= 2 and h4_medecins < 5):
    h4_niveau = "PREOCCUPANT"
else:
    h4_niveau = "SATISFAISANT"

# HÔPITAL 5 : CMS Impfondo
h5_taux = (h5_lits_occupes / h5_lits_totaux) * 100
if h5_taux > 95: h5_tag_occ = "CRI"
elif h5_taux > 85: h5_tag_occ = "ALT"
else: h5_tag_occ = "OK "

if h5_ruptures >= 2 or h5_taux > 95:
    h5_niveau = "CRITIQUE"
elif h5_ruptures >= 1 or h5_taux > 85 or (h5_alertes >= 2 and h5_medecins < 5):
    h5_niveau = "PREOCCUPANT"
else:
    h5_niveau = "SATISFAISANT"

#------------------------------------------------------------------------------------
# 3. CALCULS DES INDICATEURS NATIONAUX & BONUS
total_ruptures = h1_ruptures + h2_ruptures + h3_ruptures + h4_ruptures + h5_ruptures

# Compter le nombre d'hôpitaux critiques
nb_critiques = 0
if h1_niveau == "CRITIQUE": nb_critiques += 1
if h2_niveau == "CRITIQUE": nb_critiques += 1
if h3_niveau == "CRITIQUE": nb_critiques += 1
if h4_niveau == "CRITIQUE": nb_critiques += 1
if h5_niveau == "CRITIQUE": nb_critiques += 1

# Calcul du coût estimé des commandes urgentes
COUT_UNITAIRE_EXPRESS = 450000
cout_total_urgences = total_ruptures * COUT_UNITAIRE_EXPRESS

# Détermination de la recommandation nationale prioritaire
if nb_critiques >= 3:
    recommandation = "Mobiliser immédiatement la réserve nationale de la PNA et déployer des médecins militaires."
elif total_ruptures > 0:
    recommandation = "Lancer une procédure d'approvisionnement express pour les médicaments en rupture."
else:
    recommandation = "Poursuivre la surveillance de routine et stabiliser la répartition des lits."


# --- 4. AFFICHAGE DU TABLEAU DE BORD CONSOLIDÉ
print("=" * 72)
print("       TABLEAU DE BORD SANITAIRE — MINISTÈRE DE LA SANTÉ")
print("  Date : 16 janvier 2026  |  Pour le Conseil des Ministres")
print("=" * 72)
print(f"  {'HOPITAL':<26} {'OCCUPATION':<12} {'ALERTES':<10} {'NIVEAU GLOBAL'}")
print("-" * 72)
print(f"  {h1_nom:<26} {h1_taux:>5.1f}% [{h1_tag_occ}]  {h1_ruptures}R + {h1_alertes}A    [{h1_niveau}]")
print(f"  {h2_nom:<26} {h2_taux:>5.1f}% [{h2_tag_occ}]  {h2_ruptures}R + {h2_alertes}A    [{h2_niveau}]")
print(f"  {h3_nom:<26} {h3_taux:>5.1f}% [{h3_tag_occ}]  {h3_ruptures}R + {h3_alertes}A    [{h3_niveau}]")
print(f"  {h4_nom:<26} {h4_taux:>5.1f}% [{h4_tag_occ}]  {h4_ruptures}R + {h4_alertes}A    [{h4_niveau}]")
print(f"  {h5_nom:<26} {h5_taux:>5.1f}% [{h5_tag_occ}]  {h5_ruptures}R + {h5_alertes}A    [{h5_niveau}]")
print("-" * 72)
print(f"  {nb_critiques} hôpitaux sur 5 en situation CRITIQUE")
print(f"  {total_ruptures} ruptures de stock identifiées à l'échelle nationale")
print(f"  Coût estimé des commandes express : {cout_total_urgences:,.0f} FCFA")
print(f"  RECOMMANDATION PRIORITAIRE : {recommandation}")
print("=" * 72)