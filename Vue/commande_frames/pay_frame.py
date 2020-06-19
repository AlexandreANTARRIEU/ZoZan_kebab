from tkinter import *

from Vue.base_frame import BaseFrame


class PayFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_pay()

    def create_pay(self):
        Label(self, text="Votre payement à bien été effectué.", font='bold', justify="center").grid(row=0, columnspan=2, sticky='w')
        Label(self, text="Votre commande sera prête dans 5 minutes", font='bold').grid(row=1, columnspan=2, sticky='w')

        Button(self, text="Menu principal", command=self.show_menu).grid(row=3, column=0, sticky='w')
        Button(self, text="Nouvelle commande", fg="green", command=self._root_frame.new_order).grid(row=3, column=1, sticky='w')