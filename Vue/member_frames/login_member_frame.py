from tkinter import *
from tkinter import messagebox
from Vue.base_frame import BaseFrame


class LoginMemberFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        #self._person_controller = person_controller
        self.create_widgets()
        self.email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    def create_widgets(self):
        Label(self, text="Informations Utilisateur:", font='bold').grid(row=0, sticky='w')
        self.email_entry = self.create_entry("Email", row=3, validate_callback=self.validate_email)
        self.mdp_entry = self.create_entry("Mot de passe", row=4, validate_callback=self.validate_mdp)

        self.valid = Button(self, text="Valider", fg='green', command=self.valid).grid(row=5,column=1,sticky="w")
        self.cancel = Button(self, text="Annuler", fg='red', command=self.back).grid(row=5,column=2,sticky="w")

    def validate_mdp(self, event, entry=None):
        if len(entry.get) < 6:
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def validate_email(self, event, entry=None):
        if not self.email_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def get_data(self):
        data = dict(email=self.email_entry.get(),
                    mdp=self.mdp_entry.get())
        return data

    def valid(self):
        #data = self.get_data()
        #try :
        #    user_data = self._person_controller.inscription()
        self._root_frame.new_order()
