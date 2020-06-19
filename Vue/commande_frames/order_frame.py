from tkinter import *

from Vue.base_frame import BaseFrame


class OrderFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.listeSauce = {"Blanche" : IntVar(value=1), "Ketchup" : IntVar(value=0), "Samourai" : IntVar(value=0), "Algérienne" : IntVar(value=0)}
        self.listeCrudite = {"Salade" : IntVar(value=1), "Tomate" : IntVar(value=1), "Oignon" : IntVar(value=1)}
        self.listeViande = {"Kebab" : IntVar(value=1), "Steack" : IntVar(value=0), "Merguez" : IntVar(value=0), "Poulet" : IntVar(value=0)}
        self.listePain = {"Classique" : "classique", "Pita" : "pita", "Wrap" : "wrap"}
        self.valuepain = StringVar(value=self.listePain.get("Classique"))
        self.create_widget()

    def create_widget(self):
        Label(self, text="Commande", font='bold', justify="center").grid(row=0, sticky='w')
        Label(self, text="Pain :").grid(row=1, sticky='w')
        column = 0
        for (text, value) in self.listePain.items():
            Radiobutton(self, text=text, variable=self.valuepain, value=value, tristatevalue="x").grid(row=2, column=column, sticky='w')
            column += 1

        Label(self, text="Viande :").grid(row=3, sticky='w')
        column = 0
        for (text, value) in self.listeViande.items():
            Checkbutton(self, text=text, variable=self.listeViande.get(text), onvalue=1, offvalue=0).grid(row=4, column=column, sticky='w')
            column += 1

        Label(self, text="Crudités :").grid(row=5, sticky='w')
        column = 0
        for (text, value) in self.listeCrudite.items():
            Checkbutton(self, text=text, variable=self.listeCrudite.get(text), onvalue=1, offvalue=0).grid(row=6, column=column, sticky='w')
            column += 1

        Label(self, text="Sauce :").grid(row=7, sticky='w')
        column = 0
        for (text, value) in self.listeSauce.items():
            Checkbutton(self, text=text, variable=self.listeSauce.get(text), onvalue=1, offvalue=0).grid(row=8, column=column, sticky='w')
            column += 1

        Button(self, text="Valider", fg="green", command=self.create_order).grid(row=10, column=1, sticky='w')
        Button(self, text="Annuler", fg="red", command=self.back).grid(row=10, column=2, sticky='w')

    def create_order(self):
        menu = [self.valuepain.get()]

        for (text, value) in self.listeViande.items():
            if value.get() == 1:
                menu.append(text)

        for (text, value) in self.listeCrudite.items():
            if value.get() == 1:
                menu.append(text)

        for (text, value) in self.listeSauce.items():
            if value.get() == 1:
                menu.append(text)

        self._root_frame.valid_order()