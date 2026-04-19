from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()
try:
    conn = dao.get_connection()
    print("Connexion réussie à la base de données")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)

