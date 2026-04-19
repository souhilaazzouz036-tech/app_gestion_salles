from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()
try:
    conn = dao.get_connection()
    print("Connexion réussie à la base de données")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)
s1 = Salle("A101", "Salle A101", "Classe", 30)
try:
    dao.insert_salle(s1)
    print("Salle ajoutée avec succès")
except Exception as e:
    print("Erreur ajout :", e)
s1_modifie = Salle("A101", "Salle Informatique", "Laboratoire", 35)
try:
    dao.update_salle(s1_modifie)
    print("Salle modifiée avec succès")
except Exception as e:
    print("Erreur modification :", e)

