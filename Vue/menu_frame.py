from tkinter import Label, Button
from Vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_menu()

    def create_menu(self):
        self.title = Label(self, text="Bienvenue chez ZoZan Kebab")
        self.sign_in = Button(self, text="S'identifier", width=30, command=self._root_frame.sign_in)
        self.sign_up = Button(self, text="S'inscrire", width=30, command=self._root_frame.sign_up)
        self.order = Button(self, text="Commander", width=30, command=self._root_frame.order)
        self.quit = Button(self, text="Quitter", fg="red", width=30, command=self._root_frame.quit)
        self.title.pack(side="top")
        self.sign_in.pack()
        self.sign_up.pack()
        self.quit.pack(side="bottom")
