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
        nb_lits_total=0,
        nb_lits_occupes=0,
        nb_medecins_actifs=0, # *** voir la note en dessous de la classe svp ***
        budget_fcfa=0,
        nb_consultations_ext=0,
        nb_hospitalisations=0,
        nb_deces=0,
        nb_infirmiers=0,
        population_dept=0
    ):
        # les variables utilisees dans l'exercice 1
        self.nom_hopital = nom_hopital
        self.ville_hopital = ville_hopital
        self.nb_lits_total = nb_lits_total
        self.nb_lits_occupes = nb_lits_occupes
        self.nb_medecins_actifs = nb_medecins_actifs
        
        # les variables introduites dans l'exercice 2
        self.budget_fcfa = budget_fcfa
        self.nb_consultations_ext = nb_consultations_ext
        self.nb_hospitalisations = nb_hospitalisations
        self.nb_deces = nb_deces
        self.nb_infirmiers = nb_infirmiers
        self.population_dept = population_dept

    #------------------------------------------------------------------------------------
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
        
    #------------------------------------------------------------------------------------
    # les methodes introduites dans l'exercice 2
    
    #------------------------------------------------------------------------------------
    # methode pour convertir le budget de l'hopital en euros et en dollars
    def budget_eur(self):
        return round(self.budget_fcfa / 655.957, 2)

    def budget_usd(self):
        return round(self.budget_fcfa / 600.0, 2)
    
    # methode pour calculer la densite medicale
    def densite_medicale(self):
        return round(
            (self.nb_medecins_actifs / self.population_dept) * 1000,
            1
        )

    # methode pour calculer le taux de mortalite
    def taux_mortalite(self):
        return round(
            (self.nb_deces / self.nb_hospitalisations) * 100,
            1
        )

    # methode pour calculer le taux d'occupation des lits de l'hopital
    def taux_occupation(self):
        return round(
            (self.nb_lits_occupes / self.nb_lits_total) * 100,
            1
        )
        
    # ------------------------------------------------------------------------------------
    # j'ai preferer ajouter une methode budget_medicaments pour calculer le budget alloue 
    # aux medicaments, au lieu de le calculer directement dans la methode jours_stock, 
    # parce que c'est plus clair et plus facile a comprendre mais on peut aussi le calculer 
    # directement dans la methode jours_stock si vous voulez
    
    # methode pour calculer le budget alloue aux medicaments, en supposant que 35% du budget
    def budget_medicaments(self):
        return int(self.budget_fcfa * 0.35)

    # ------------------------------------------------------------------------------------
    # methode pour calculer les jours de rupture de stock de medicaments, en sachant que 
    # le cout journalier des medicaments est de 450 000 FCFA
    def jours_stock(self):
        return self.budget_medicaments() // 450_000 # cout journalier des medicaments = 450 000 FCFA

    # methode pour calculer le reste du budget alloue aux medicaments
    def jours_restants(self):
        return self.budget_medicaments() % 450_000
    
    # methode pour savoir si le nombre de consultations est pair ou impair
    def consultations_paires(self):
        return self.nb_consultations_ext % 2 == 0
    
    # ------------------------------------------------------------------------------------
    # methode pour calculer le budget de l'hopital pour l'annee n+2, en supposant que le 
    # budget augmente de 8% par an
    def budget_n_plus_2(self):
        return round(
            self.budget_fcfa * (1.08 ** 2),
            2
        )
    
    # ------------------------------------------------------------------------------------
    # methode pour generer une alerte si la densite medicale est inferieure a 2.3 pour 
    # 1000 habitants ou si le taux de mortalite est superieur a 2%    
    def generer_alerte(self):

        if self.densite_medicale() < 2.3:
            return (
                f"ALERTE : Densite medicale CRITIQUE "
                f"({self.densite_medicale()} pour 1000 hab "
                f"— norme OMS : 2.3)"
            )

        if self.taux_mortalite() > 2:
            return (
                f"ALERTE : Taux de mortalite critique "
                f"({self.taux_mortalite()}%)"
            )

        return "Aucune alerte"
    
    def afficher_rapport(self):

        print(
            f"=== RAPPORT TRIMESTRIEL Q4 2025 - {self.nom_hopital} ==="
        )

        print("BUDGET")

        print(
            f"  Depenses Q4       : "
            f"{self.budget_fcfa:,.0f} FCFA"
        )

        print(
            f"  En euros          : "
            f"{self.budget_eur():,.2f} EUR"
        )

        print(
            f"  En dollars        : "
            f"{self.budget_usd():,.2f} USD"
        )

        print()

        print("INDICATEURS OMS")

        print(
            f"  Densite medicale  : "
            f"{self.densite_medicale()} medecins / 1000 hab  "
            f"[Norme OMS : >= 2.3]"
        )

        print(
            f"  Taux mortalite    : "
            f"{self.taux_mortalite()}%                      "
            f"[Seuil alerte : > 2%]"
        )

        print(
            f"  Taux occupation   : "
            f"{self.taux_occupation()}%                     "
            f"[Optimal : 70-85%]"
        )

        print()

        print("ANALYSE PHARMACIE")

        print(
            f"  Budget medicaments: "
            f"{self.budget_medicaments():,.0f} FCFA"
        )

        print(
            f"  Jours de stock    : "
            f"{self.jours_stock()} jours"
        )

        print(
            f"  Jours depassement : "
            f"{self.jours_restants()} jours"
        )

        print()

        print("PROJECTION")

        print(
            f"  Budget N+2 (8%/an): "
            f"{self.budget_n_plus_2():,.1f} FCFA"
        )

        print()

        print(self.generer_alerte())
        
#------------------------------------------------------------------------------------
# *** NOTE IMPORTANTE ***
# j'ai choisi de mettre nb_medecins_actifs dans la classe Hopital au lieu de
# nb_medecins, parce que je l'ai deja utilise dans l'exercice 1 et comme ma structure
# de donnees est basee sur des classes, je ne voulais pas changer le nom de la variable
# *** FIN DE LA NOTE IMPORTANTE ***