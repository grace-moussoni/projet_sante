#------------------------------------------------------------------------------------
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# + S3 (if/elif/else, conditions composees)


#------------------------------------------------------------------------------------
# DONNEES S2 : Variables medicaments

#------------------------------------------------------------------------------------
# Je declare les variables pour 5 medicaments avec leurs stocks, seuils de rupture 
# et couts unitaires
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA

m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0

#------------------------------------------------------------------------------------
# CLASSIFICATION MEDICAMENT 1 : Artemether-Lumefantrine 
# S3 (nouveau) : if / elif / else
# S2 (reutilise) : operateurs arithmetiques pour calcul des seuils

# Je determine le statut du medicament 1 selon son stock et son seuil de rupture
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = "ALERTE STOCK"
    m1_couleur = '[ORANGE]'
    m1_action  = 'commande urgente a declencher'
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = "ALERTE STOCK"
    m1_couleur = '[JAUNE]'
    m1_action  = 'surveillance renforcee'
else:
    m1_statut  = "STOCK SUFFISANT"
    m1_couleur = '[VERT]'
    m1_action  = 'Aucune action requise'
    
# Je reproduits la meme logique pour le medicament 2
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = "ALERTE STOCK"
    m2_couleur = '[ORANGE]'
    m2_action  = 'commande urgente a declencher'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = "ALERTE STOCK"
    m2_couleur = '[JAUNE]'
    m2_action  = 'surveillance renforcee'
else:
    m2_statut  = "STOCK SUFFISANT"
    m2_couleur = '[VERT]'
    m2_action  = 'Aucune action requise'
    
# Je reproduits la meme logique pour le medicament 3
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = "ALERTE STOCK"
    m3_couleur = '[ORANGE]'
    m3_action  = 'commande urgente a declencher'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = "ALERTE STOCK"
    m3_couleur = '[JAUNE]'
    m3_action  = 'surveillance renforcee'
else:
    m3_statut  = "STOCK SUFFISANT"
    m3_couleur = '[VERT]'
    m3_action  = 'Aucune action requise'
    
# Je reproduits la meme logique pour le medicament 4
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = "ALERTE STOCK"
    m4_couleur = '[ORANGE]'
    m4_action  = 'commande urgente a declencher'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = "ALERTE STOCK"
    m4_couleur = '[JAUNE]'
    m4_action  = 'surveillance renforcee'
else:
    m4_statut  = "STOCK SUFFISANT"
    m4_couleur = '[VERT]'
    m4_action  = 'Aucune action requise'

# Je reproduits la meme logique pour le medicament 5
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = "ALERTE STOCK"
    m5_couleur = '[ORANGE]'
    m5_action  = 'commande urgente a declencher'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = "ALERTE STOCK"
    m5_couleur = '[JAUNE]'
    m5_action  = 'surveillance renforcee'
else:
    m5_statut  = "STOCK SUFFISANT"
    m5_couleur = '[VERT]'
    m5_action  = 'Aucune action requise'

#------------------------------------------------------------------------------------
# COMPTAGE DES ALERTES
# S2 (reutilise) : variables numeriques
# S3 (nouveau) : conditions pour compter
nb_ruptures_critiques = 0
nb_alertes_stock      = 0

# Je compte le nombre de medicaments en rupture critique
if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
if m2_statut == 'RUPTURE CRITIQUE': 
    nb_ruptures_critiques = nb_ruptures_critiques + 1
if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques = nb_ruptures_critiques + 1
    
# Je compte le nombre de medicaments en alerte stock
if m1_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
if m2_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
if m3_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
if m4_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1
if m5_statut == 'ALERTE STOCK':
    nb_alertes_stock = nb_alertes_stock + 1

#------------------------------------------------------------------------------------
# AFFICHAGE RAPPORT
# S2 (reutilise) : f-strings structurees
# S3 (nouveau) : statuts et couleurs determines par les conditions

# J'affiche le rapport de la PNA avec les medicaments et leur statut
print('=' * 65)
print('  RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print('  Date : 15 janvier 2026')
print('=' * 65)

# J'affiche le medicament 1 avec son statut et sa couleur
print(f'  {m1_couleur} {m1_nom}')
print(f'      Stock : {m1_stock} unites | Seuil : {m1_seuil_rupture}')
print(f'      Statut : {m1_statut}')
print(f'      Action : {m1_action}')
print('-' * 65)

# J'affiche le medicament 2 avec son statut et sa couleur
print(f'  {m2_couleur} {m2_nom}')
print(f'      Stock : {m2_stock} unites | Seuil : {m2_seuil_rupture}')
print(f'      Statut : {m2_statut}')
print(f'      Action : {m2_action}')
print('-' * 65)

# J'affiche le medicament 3 avec son statut et sa couleur
print(f'  {m3_couleur} {m3_nom}')
print(f'      Stock : {m3_stock} unites | Seuil : {m3_seuil_rupture}')
print(f'      Statut : {m3_statut}')
print(f'      Action : {m3_action}')
print('-' * 65)

# J'affiche le medicament 4 avec son statut et sa couleur
print(f'  {m4_couleur} {m4_nom}')
print(f'      Stock : {m4_stock} unites | Seuil : {m4_seuil_rupture}')
print(f'      Statut : {m4_statut}')
print(f'      Action : {m4_action}')
print('-' * 65)

# J'affiche le medicament 5 avec son statut et sa couleur
print(f'  {m5_couleur} {m5_nom}')
print(f'      Stock : {m5_stock} unites | Seuil : {m5_seuil_rupture}')
print(f'      Statut : {m5_statut}')
print(f'      Action : {m5_action}')

print('=' * 65)
# J'affiche le bilan final avec le nombre de ruptures critiques et d'alertes stock
print("BILAN STOCK — PNA CONGO")

print(f'  Ruptures critiques : {nb_ruptures_critiques} ({m1_nom if m1_statut == "RUPTURE CRITIQUE" else ""} {m2_nom if m2_statut == "RUPTURE CRITIQUE" else ""} {m3_nom if m3_statut == "RUPTURE CRITIQUE" else ""} {m4_nom if m4_statut == "RUPTURE CRITIQUE" else ""} {m5_nom if m5_statut == "RUPTURE CRITIQUE" else ""})')
print(f'  Alertes stock : {nb_alertes_stock} ({m1_nom if m1_statut == "ALERTE STOCK" else ""} {m2_nom if m2_statut == "ALERTE STOCK" else ""} {m3_nom if m3_statut == "ALERTE STOCK" else ""} {m4_nom if m4_statut == "ALERTE STOCK" else ""} {m5_nom if m5_statut == "ALERTE STOCK" else ""})')
print(f'  Stocks normaux : {5 - nb_ruptures_critiques - nb_alertes_stock}')

print('=' * 65)
print (f'  Alerte prioritaire : {nb_ruptures_critiques} medicament(s) en rupture critique')
print ("  Transmettre immediatement au Dr. MOUKALA (PNA)")
print('=' * 65)