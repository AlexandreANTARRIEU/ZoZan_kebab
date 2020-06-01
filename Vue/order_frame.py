from tkinter import *

from Vue.base_frame import BaseFrame


class OrderFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_order()

    def create_order(self):
        Label(self, text="Créer votre menu", font='bold', justify="center").grid(row=0, sticky='w')
        Label(self, text="Pain :").grid(row=1, sticky='w')
        valuepain = StringVar(value="classique")
        valuepain.set("classique")
        Radiobutton(self, text="Classique", variable=valuepain, value="classique", tristatevalue="x").grid(row=2, column=0, sticky='w')
        Radiobutton(self, text="Pita", variable=valuepain, value="pita", tristatevalue="x").grid(row=2, column=1, sticky='w')
        Radiobutton(self, text="Wrap", variable=valuepain, value="wrap", tristatevalue="x").grid(row=2, column=2, sticky='w')

        Label(self, text="Viande :").grid(row=3, sticky='w')
        valueviande = StringVar(value="kebab")
        valueviande.set("kebab")
        Radiobutton(self, text="Kebab", variable=valueviande, value="kebab", tristatevalue="y").grid(row=4, column=0, sticky='w')
        Radiobutton(self, text="Steack", variable=valueviande, value="steack", tristatevalue="y").grid(row=4, column=1, sticky='w')
        Radiobutton(self, text="Merguez", variable=valueviande, value="merguez", tristatevalue="y").grid(row=4, column=2, sticky='w')
        Radiobutton(self, text="Poulet", variable=valueviande, value="poulet", tristatevalue="y").grid(row=4, column=3, sticky='w')

        Label(self, text="Crudités :").grid(row=5, sticky='w')
        salade = StringVar()
        tomate = StringVar()
        oignon = StringVar()
        Checkbutton(self, text="Salade", variable=salade, onvalue="salade", offvalue="no_salade").grid(row=6, column=0, sticky='w')
        Checkbutton(self, text="Tomate", variable=tomate, onvalue="tomate", offvalue="no_tomate").grid(row=6, column=1, sticky='w')
        Checkbutton(self, text="Oignon", variable=oignon, onvalue="oignon", offvalue="no_oignon").grid(row=6, column=2, sticky='w')

        Label(self, text="Sauce :").grid(row=7, sticky='w')
        valuesauce = StringVar(value="blanche")
        valuesauce.set("blanche")
        Radiobutton(self, text="Blanche", variable=valuesauce, value="blanche", tristatevalue="x").grid(row=8, column=0, sticky='w')
        Radiobutton(self, text="Ketchup", variable=valuesauce, value="ketchup", tristatevalue="x").grid(row=8, column=1, sticky='w')
        Radiobutton(self, text="Samourai", variable=valuesauce, value="samourai", tristatevalue="x").grid(row=8, column=2, sticky='w')
        Radiobutton(self, text="Algérienne", variable=valuesauce, value="algerienne", tristatevalue="x").grid(row=8, column=3, sticky='w')

        Button(self, text="Valider", fg="green", command=self.back).grid(row=10, column=1, sticky='w')
        Button(self, text="Annuler", fg="red", command=self.back).grid(row=10, column=2, sticky='w')