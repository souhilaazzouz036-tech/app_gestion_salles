from Data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()


def ajouter_salle(self, salle):
    if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
        return False, "Tous les champs sont obligatoires"