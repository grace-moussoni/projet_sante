#------------------------------------------------------------------------------------
# ici je vais importer les variables et les classes que j'ai cree dans le fichier 
# sante_variables.py
from sante_variables import (
    Patient,
    Consultation,
    Hopital,
)

# 1. je cree un patient avec les informations suivantes
patient = Patient(
    "MAVOUNGOU Celestine",
    42,
    "F",
    "Brazzaville",
    "CNSS"
)

# 2. je cree une consultation avec les informations suivantes
consultation = Consultation(
    "Urgences",
    15000.0,
    1,
    30.0,
    "Paludisme grave"
)

# 3. je cree un hopital avec les informations suivantes
hopital = Hopital(
    "CHU de Brazzaville",
    "Brazzaville",
    320,
    284,
    47
)

# 4. j'affiche la fiche du patient, de la consultation et de l'hopital
patient.afficher_fiche(
    consultation, 
    hopital
)