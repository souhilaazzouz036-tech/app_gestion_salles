import customtkinter as ctk
from services.services_salle import ServiceSalle
from tkinter import messagebox
from models.salle import Salle

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")
        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code :")
        self.label_code.grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé :")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=10)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=10)
        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type :")
        self.label_type.grid(row=2, column=0, padx=10, pady=10)
        self.entry_type = ctk.CTkEntry(self.cadreInfo)
        self.entry_type.grid(row=2, column=1, padx=10, pady=10)
        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacite :")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")
        self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)
        self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)
        self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)
        self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)
        self.btn_ajouter.configure(command=self.ajouter_salle)
        self.btn_modifier.configure(command=self.modifier_salle)
        self.btn_supprimer.configure(command=self.supprimer_salle)
        self.btn_rechercher.configure(command=self.rechercher_salle)

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )
        succes, message = self.service_salle.ajouter_salle(salle)
        messagebox.showinfo("Ajout", message)
        if succes:
            self.lister_salles()






