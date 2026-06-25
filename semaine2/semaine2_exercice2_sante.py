# j'importe la classe Hopital du fichier sante_variables.py
from sante_variables import Hopital

# je cree un hopital avec les informations suivantes
hopital = Hopital(
    "Hopital General de Pointe-Noire", # nom_hopital
    "Pointe-Noire", # ville_hopital
    180, # nb_lits_total
    143, # nb_lits_occupes
    22, # nb_medecins_actifs
    87_450_000, # budget_fcfa
    4823, # nb_consultations_ext
    1247, # nb_hospitalisations
    18, # nb_deces
    58, # nb_infirmiers
    128_000 # population_dept
)

# j'affiche le rapport de l'hopital
hopital.afficher_rapport()