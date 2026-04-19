import mysql.connector
import json


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection


def insert_salle(self, salle):
    connection = self.get_connection()
    cursor = connection.cursor()

    req = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
    valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)

    cursor.execute(req, valeurs)
    connection.commit()

    cursor.close()
    connection.close()
    def update_salle(self, salle):
        connection = self.get_connection()
        cursor = connection.cursor()

        req = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)

        cursor.execute(req, valeurs)
        connection.commit()

        cursor.close()
        connection.close()