from tkinter import *

from Vue.base_frame import BaseFrame


class OrderFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_order()

    def create_order(self):
        Label(self, text="Commande", font='bold', justify="center").grid(row=0, sticky='w')
        Label(self, text="Pain :").grid(row=1, sticky='w')
        valuepain = StringVar(value="classique")
        valuepain.set("classique")
        Radiobutton(self, text="Classique", variable=valuepain, value="classique", tristatevalue="x").grid(row=2, column=0, sticky='w')
        Radiobutton(self, text="Pita", variable=valuepain, value="pita", tristatevalue="x").grid(row=2, column=1, sticky='w')
        Radiobutton(self, text="Wrap", variable=valuepain, value="wrap", tristatevalue="x").grid(row=2, column=2, sticky='w')

        Label(self, text="Viande :").grid(row=3, sticky='w')
        kebab = IntVar()
        steack = IntVar()
        merguez = IntVar()
        poulet = IntVar()
        Checkbutton(self, text="Kebab", variable=kebab, onvalue=1, offvalue=0).grid(row=4, column=0, sticky='w')
        Checkbutton(self, text="Steack", variable=steack, onvalue=1, offvalue=0).grid(row=4, column=1, sticky='w')
        Checkbutton(self, text="Merguez", variable=merguez, onvalue=1, offvalue=0).grid(row=4, column=2, sticky='w')
        Checkbutton(self, text="Poulet", variable=poulet, onvalue=1, offvalue=0).grid(row=4, column=3, sticky='w')

        Label(self, text="Crudités :").grid(row=5, sticky='w')
        salade = IntVar(value=1)
        tomate = IntVar(value=1)
        oignon = IntVar(value=1)
        Checkbutton(self, text="Salade", onvalue=1, offvalue=0, variable=salade).grid(row=6, column=0, sticky='w')
        Checkbutton(self, text="Tomate", onvalue=1, offvalue=0, variable=tomate).grid(row=6, column=1, sticky='w')
        Checkbutton(self, text="Oignon", onvalue=1, offvalue=0, variable=oignon).grid(row=6, column=2, sticky='w')

        Label(self, text="Sauce :").grid(row=7, sticky='w')
        blanche = IntVar()
        ketchup = IntVar()
        samourai = IntVar()
        algerienne = IntVar()
        Checkbutton(self, text="Blanche", variable=blanche, onvalue=1, offvalue=0).grid(row=8, column=0, sticky='w')
        Checkbutton(self, text="Ketchup", variable=ketchup, onvalue=1, offvalue=0).grid(row=8, column=1, sticky='w')
        Checkbutton(self, text="Samourai", variable=samourai, onvalue=1, offvalue=0).grid(row=8, column=2, sticky='w')
        Checkbutton(self, text="Algérienne", variable=algerienne, onvalue=1, offvalue=0).grid(row=8, column=3, sticky='w')

        Button(self, text="Valider", fg="green", command=self._root_frame.valid_order).grid(row=10, column=1, sticky='w')
        Button(self, text="Annuler", fg="red", command=self.back).grid(row=10, column=2, sticky='w')