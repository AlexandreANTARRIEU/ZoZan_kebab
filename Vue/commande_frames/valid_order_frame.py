from tkinter import *

from Vue.base_frame import BaseFrame


class ValidOrderFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_valid_order()

    def create_valid_order(self):
        Label(self, text="ZoZan Kebab vous remercie pour votre commande.", font='bold', justify="center").grid(row=0, columnspan=2, sticky='w')
        Label(self, text="Le montant de la commande d'élève à :", font='bold').grid(row=1, columnspan=2, sticky='w')

        Button(self, text="Payer", command=self._root_frame.pay).grid(row=3, column=0, sticky='w')
        Button(self, text="Modifier commande", fg="green", command=self.back).grid(row=3, column=1, sticky='w')