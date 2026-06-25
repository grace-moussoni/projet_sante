# j'importe la classe Hopital du fichier sante_variables.py
from sante_variables import Hopital

# je cree les trois hopitaux avec les informations suivantes

# 1. Hopital de Kinkala
kinkala = Hopital(
    nom_hopital="Hopital District Kinkala",
    ville_hopital="Kinkala",
    nb_lits_total=11,
    nb_lits_occupes=35,
    nb_medecins_actifs=33,
    budget_fcfa=12_500_000,
    nb_consultations_ext=1847,
    nb_hospitalisations=1234,
    nb_deces=201,
    nb_infirmiers=0,
    population_dept=2
)

# 2. Hopital de Vindza
vindza = Hopital(
    nom_hopital="CMS de Vindza",
    ville_hopital="Vindza",
    nb_lits_total=45,
    nb_lits_occupes=41,
    nb_medecins_actifs=3,
    budget_fcfa=6_800_000,
    nb_consultations_ext=923,
    nb_hospitalisations=312,
    nb_deces=8,
    nb_infirmiers=0,
    population_dept=85_000
)

# 3. Hopital de Kindamba
kindamba = Hopital(
    nom_hopital="Hopital de Kindamba",
    ville_hopital="Kindamba",
    nb_lits_total=20,
    nb_lits_occupes=14,
    nb_medecins_actifs=1,
    budget_fcfa=9_200_000,
    nb_consultations_ext=87,
    nb_hospitalisations=87,
    nb_deces=2,
    nb_infirmiers=0,
    population_dept=67_000
)

# j'affiche le rapport de chaque hopital
print ("=" * 80)
print("\n************* RAPPORT DE L'HOPITAL DE KINKALA *************")
print ("=" * 80)
kinkala.afficher_rapport()

print ("=" * 80)
print("\n************* RAPPORT DE L'HOPITAL DE VINDZA *************")
print ("=" * 80)
vindza.afficher_rapport()

print ("=" * 80)
print("\n************* RAPPORT DE L'HOPITAL DE KINDAMBA *************")
print ("=" * 80)
kindamba.afficher_rapport()

# je traite la question du bonus
hopitaux = [kinkala, vindza, kindamba]

#----------------------------------------------------------------------------
# je cree la methode pour calculer si le budget total des hopitaux est 
# suffisant pour passer a 5 medecins par hopital

def budget_suffisant(_hopitaux):
    # cout d'un medecin par trimestre (3 mois) = 1_200_000 FCFA
    cout_medecin = 1_200_000

    total_medecins_supp = 5 * len(_hopitaux)

    cout_total_recrutement = total_medecins_supp * cout_medecin

    budget_total = sum(h.budget_fcfa for h in _hopitaux)

    if budget_total >= cout_total_recrutement:
        print("\nBONUS : Budget suffisant pour recrutement")
    else:
        print("\nBONUS : Budget insuffisant")
        
# appel de la methode pour traiter le bonus
print ("=" * 105)
print("\n ************* BONUS : Verification du budget pour recrutement de 5 medecins par hopital *************")
print ("=" * 105)
budget_suffisant(hopitaux)