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
# TODO : Valider spo2, tension_syst, douleur, age de la meme facon
# --- TRIAGE (S3 nouveau : conditions composees avec or) --
# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit (or)
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Medecin present immediatement — code ROUGE active'
# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif ___:
    niveau_triage  = '2 — URGENT'
    couleur_triage = ___
    delai_pec      = ___
    action_triage  = ___
# Niveau 3 : URGENT DIFFERE
elif ___:
    niveau_triage  = ___
    couleur_triage = ___
    delai_pec      = ___
    action_triage  = ___
# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage  = ___
    couleur_triage = ___
    delai_pec      = ___
    action_triage  = ___
# --- AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings) --
print()
print('=' * 55)
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
# TODO : Afficher tous les parametres vitaux et le resultat du triage