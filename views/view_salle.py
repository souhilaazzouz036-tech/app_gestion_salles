import customtkinter as ctk
from services.services_salle import ServiceSalle

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





