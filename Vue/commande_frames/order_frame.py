from tkinter import *

from Vue.base_frame import BaseFrame


class OrderFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_order()

    def create_order(self):
        Label(self, text="Commande", font='bold', justify="center").grid(row=0, sticky='w')
        Label(self, text="Pain :").grid(row=1, sticky='w')
        self.valuepain = StringVar(value="classique")
        Radiobutton(self, text="Classique", variable=self.valuepain, value="classique", tristatevalue="x").grid(row=2, column=0, sticky='w')
        Radiobutton(self, text="Pita", variable=self.valuepain, value="pita", tristatevalue="x").grid(row=2, column=1, sticky='w')
        Radiobutton(self, text="Wrap", variable=self.valuepain, value="wrap", tristatevalue="x").grid(row=2, column=2, sticky='w')

        Label(self, text="Viande :").grid(row=3, sticky='w')
        self.kebab = IntVar(value=1)
        self.steack = IntVar(value=0)
        self.merguez = IntVar(value=0)
        self.poulet = IntVar(value=0)
        Checkbutton(self, text="Kebab", variable=self.kebab, onvalue=1, offvalue=0).grid(row=4, column=0, sticky='w')
        Checkbutton(self, text="Steack", variable=self.steack, onvalue=1, offvalue=0).grid(row=4, column=1, sticky='w')
        Checkbutton(self, text="Merguez", variable=self.merguez, onvalue=1, offvalue=0).grid(row=4, column=2, sticky='w')
        Checkbutton(self, text="Poulet", variable=self.poulet, onvalue=1, offvalue=0).grid(row=4, column=3, sticky='w')

        Label(self, text="Crudités :").grid(row=5, sticky='w')
        self.salade = IntVar(value=1)
        self.tomate = IntVar(value=1)
        self.oignon = IntVar(value=1)
        Checkbutton(self, text="Salade", variable=self.salade).grid(row=6, column=0, sticky='w')
        Checkbutton(self, text="Tomate", variable=self.tomate).grid(row=6, column=1, sticky='w')
        Checkbutton(self, text="Oignon", variable=self.oignon).grid(row=6, column=2, sticky='w')

        Label(self, text="Sauce :").grid(row=7, sticky='w')
        self.blanche = IntVar(value=1)
        self.ketchup = IntVar(value=0)
        self.samourai = IntVar(value=0)
        self.algerienne = IntVar(value=0)
        Checkbutton(self, text="Blanche", variable=self.blanche, onvalue=1, offvalue=0).grid(row=8, column=0, sticky='w')
        Checkbutton(self, text="Ketchup", variable=self.ketchup, onvalue=1, offvalue=0).grid(row=8, column=1, sticky='w')
        Checkbutton(self, text="Samourai", variable=self.samourai, onvalue=1, offvalue=0).grid(row=8, column=2, sticky='w')
        Checkbutton(self, text="Algérienne", variable=self.algerienne, onvalue=1, offvalue=0).grid(row=8, column=3, sticky='w')

        Button(self, text="Valider", fg="green", command=self._root_frame.valid_order).grid(row=10, column=1, sticky='w')
        Button(self, text="Annuler", fg="red", command=self.back).grid(row=10, column=2, sticky='w')