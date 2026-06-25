# je suis desole, jutilise un clavier anglais, donc je ne peux pas mettre des accents

# -----------------------------------------------------------------------------------
# j'ai choisi de structurer mes donnees dans des "class" parce que c'etait plus
# pratique pour moi, mais je sais que ce n'est pas necessaire pour ce projet

#------------------------------------------------------------------------------------
# 1. class pour stocker les donnees d'un patient
class Patient:

    # constructeur de la classe Patient
    def __init__(
        self,
        nom,
        age,
        sexe,
        departement,
        couverture_sociale
    ):
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.departement = departement
        self.couverture_sociale = couverture_sociale
        
    # methode pour afficher la fiche du patient, de la consultation et de l'hopital
    
    #------------------------------------------------------------------------------------
    # j'ai preferer mettre cette methode dans la classe Patient, parce que c'est 
    # le patient qui est le centre de la fiche, mais on peut aussi la mettre dans une 
    # autre classe si vous voulez ou creer une classe Fiche pour ca, mais je pense que 
    # c'est pas necessaire pour le moment
    
    def afficher_fiche(self, consultation, hopital):
        print("=" * 60)
        print(f"  FICHE PATIENT — {self.nom}")
        print("=" * 60)

        print(f"  Age             : {self.age} ans")
        print(f"  Sexe            : {self.sexe}")
        print(f"  Departement     : {self.departement}")
        print(f"  Couverture      : {self.couverture_sociale}")

        print("-" * 60)

        print("  CONSULTATION")
        print(f"  Type            : {consultation.type_consultation}")
        print(f"  Diagnostic      : {consultation.diagnostic_principal}")
        print(f"  Cout unitaire   : {consultation.cout_consultation_fcfa:,.0f} FCFA")
        print(f"  Remise CNSS     : {consultation.remise_cnss_pct}%")
        print(
            f"  COUT TOTAL      : "
            f"{consultation.calculer_cout_total():,.1f} FCFA"
        )

        print("-" * 60)

        print(f"  HOPITAL : {hopital.nom_hopital}")
        print(f"  Ville           : {hopital.ville_hopital}")

        print(
            f"  Lits occupes    : "
            f"{hopital.nb_lits_occupes} / "
            f"{hopital.nb_lits_total} "
            f"({hopital.calculer_taux_occupation()}%)"
        )

        print(f"  Medecins actifs : {hopital.nb_medecins_actifs}")

        print(
            f"  Ratio consult.  : "
            f"{hopital.calculer_ratio_consultations(120)} "
            f"consultations / medecin ce matin"
        )

        print("=" * 60)
        print("  STATUT : Prise en charge validee")
        print("=" * 60)
        
# 2. class pour stocker les donnees d'une consultation
class Consultation:

    # constructeur de la classe Consultation
    def __init__(
        self,
        type_consultation,
        cout_consultation_fcfa,
        nb_consultations,
        remise_cnss_pct,
        diagnostic_principal
    ):
        self.type_consultation = type_consultation
        self.cout_consultation_fcfa = cout_consultation_fcfa
        self.nb_consultations = nb_consultations
        self.remise_cnss_pct = remise_cnss_pct
        self.diagnostic_principal = diagnostic_principal
    
    #------------------------------------------------------------------------------------    
    # methode pour calculer le cout total de la consultation, en tenant compte du nombre 
    # de consultations et de la remise CNSS
    def calculer_cout_total(self):
        return (
            self.cout_consultation_fcfa
            * self.nb_consultations
            * (1 - self.remise_cnss_pct / 100)
        )

# 3. class pour stocker les donnees d'un hopital
class Hopital:
    
    # constructeur de la classe Hopital
    def __init__(
        self,
        nom_hopital,
        ville_hopital,
        nb_lits_total,
        nb_lits_occupes,
        nb_medecins_actifs
    ):
        self.nom_hopital = nom_hopital
        self.ville_hopital = ville_hopital
        self.nb_lits_total = nb_lits_total
        self.nb_lits_occupes = nb_lits_occupes
        self.nb_medecins_actifs = nb_medecins_actifs

    # methode pour calculer le taux d'occupation des lits de l'hopital
    def calculer_taux_occupation(self):
        return round(
            self.nb_lits_occupes
            / self.nb_lits_total
            * 100,
            1
        )

    # methode pour calculer le ratio de consultations par medecin
    def calculer_ratio_consultations(
        self,
        nb_consultations_hopital
    ):
        return round(
            nb_consultations_hopital
            / self.nb_medecins_actifs,
            1
        )