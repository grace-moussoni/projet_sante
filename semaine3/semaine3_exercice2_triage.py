#------------------------------------------------------------------------------------
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not

#------------------------------------------------------------------------------------
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()

# SAISIE DES DONNEES PATIENT (S2 reutilise : input(), conversion)
nom_patient   = input('Nom du patient : ')
age_patient   = int(input('Age (annees) : '))
temperature   = float(input('Temperature (degres C, ex: 38.4) : '))
spo2          = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst  = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur       = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

#------------------------------------------------------------------------------------
# VALIDATION DES PLAGES (S2 + S3 : conditions simples)
# Verifier que la temperature est dans une plage physiologiquement possible
if temperature < 35.0 or temperature > 43.0:
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')
    # Dans une version avancee, on redemanderait la saisie ici

# Verifier que la saturation O2 est dans une plage physiologiquement possible
if spo2 < 50.0 or spo2 > 100.0:
    print('ERREUR : Valeur de saturation O2 impossible — verifier la saisie')
    
# Verifier que la tension systolique est dans une plage physiologiquement possible
if tension_syst < 50 or tension_syst > 250:
    print('ERREUR : Valeur de tension systolique impossible — verifier la saisie')
    
# Verifier que la douleur est dans une plage possible (0-10)
if douleur < 0 or douleur > 10:
    print('ERREUR : Valeur de douleur impossible — verifier la saisie')
    
# Verifier que l'age est dans une plage physiologiquement possible
if age_patient < 0 or age_patient > 120:
    print('ERREUR : Valeur d\'age impossible — verifier la saisie')

# TRIAGE (S3 nouveau : conditions composees avec or)
# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit (or)
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Medecin present immediatement — code ROUGE active'
    
# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif temperature > 38.5 or spo2 < 95 or tension_syst > 160:
    niveau_triage  = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec      = '10 minutes'
    action_triage  = 'Medecin present dans les 10 minutes — code ORANGE active'
    
# Niveau 3 : URGENT DIFFERE
elif temperature > 38.0 or spo2 < 98 or tension_syst > 140:
    niveau_triage  = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec      = '30 minutes'
    action_triage  = 'Medecin present dans les 30 minutes — code JAUNE active'

# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage  = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec      = '1 heure'
    action_triage  = 'Medecin present dans une heure — code VERT active'
    
# AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings)
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()
print(f'Nom du patient : {nom_patient}')
print(f'Age : {age_patient} ans')
print(f'Temperature : {temperature} °C')
print(f'Saturation O2 : {spo2} %')
print(f'Tension systolique : {tension_syst} mmHg')
print(f'Douleur : {douleur} / 10')
print()
print('=' * 55)
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
print('PARAMETRES VITAUX — INTERPRETATION')
print(f'  Temperature : {temperature} °C')
print(f'  Saturation O2 : {spo2} %')
print(f'  Tension systolique : {tension_syst} mmHg')
print(f'  Douleur : {douleur} / 10')
print()
print('-' * 55)
print()
print(f'  Niveau de triage : {niveau_triage} {couleur_triage}')
print(f'  Delai de prise en charge : {delai_pec}')
print(f'  Action a prendre : {action_triage}')
print()
print('-' * 55)
print()
print(f'Motif principal : Temperature {temperature} °C > seuil critique 39.5 °C')
print('=' * 55)