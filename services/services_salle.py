from Data.dao_salle import DataSalle
from models.salle import Salle



class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()


def ajouter_salle(self, salle):
    if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
        return False, "Tous les champs sont obligatoires"
    if  int(salle.capacite) < 1:
        return False, "La capacité doit être supérieure ou égale à 1"

    try:
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès"
    except Exception as e:
        return False, str(e)


def supprimer_salle(self, code):
    try:
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée avec succès"
    except Exception as e:
        return False, str(e)
 def rechercher_salle(self, code):
        try:
            resultat = self.dao_salle.get_salle(code)
            if resultat:
                return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
            return None
        except Exception as e:
            print("Erreur recherche :", e)
            return None
def recuperer_salles(self):
    liste_objets = []
    try:
        resultats = self.dao_salle.get_salles()
    except Exception as e:
        print("Erreur récupération :", e)
    return liste_objets
