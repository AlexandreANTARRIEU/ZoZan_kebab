from tkinter import *

from Vue.menu_frame import MenuFrame
from Vue.commande_frames.order_frame import OrderFrame
from Vue.commande_frames.valid_order_frame import ValidOrderFrame
from Vue.commande_frames.pay_frame import PayFrame
from Vue.member_frames.new_member_frame import NewMemberFrame
from Vue.member_frames.login_member_frame import LoginMemberFrame


class RootFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self._menu_frame = MenuFrame(self)
        self._frames = []

    def order(self):
        self.hide_menu()
        order_frame = OrderFrame(self)
        order_frame.show()
        self._frames.append(order_frame)

    def new_order(self):
        self.cancel()
        self.hide_menu()
        order_frame = OrderFrame(self)
        order_frame.show()
        self._frames.append(order_frame)

    def login_user(self):
        self.hide_menu()
        login_member_frame = LoginMemberFrame(self)
        login_member_frame.show()
        self._frames.append(login_member_frame)

    def new_user(self):
        self.hide_menu()
        new_member_frame = NewMemberFrame(self)
        new_member_frame.show()
        self._frames.append(new_member_frame)

    # def new_user(self):
    #   self.hide_menu()
    #   new_member_frame = NewMemberFrame(self._person_controller, self)
    #   new_member_frame.show()
    #   self._frames.append(new_member_frame)

    def valid_order(self):
        self.hide_frames()
        valid_order_frame = ValidOrderFrame(self)
        valid_order_frame.show()
        self._frames.append(valid_order_frame)

    def pay(self):
        self.hide_frames()
        pay_frame = PayFrame(self)
        pay_frame.show()
        self._frames.append(pay_frame)

    def hide_frames(self):
        for frame in self._frames:
            frame.hide()

    def show_menu(self):
        for frame in self._frames:
            frame.destroy()
        self._frames = []
        self._menu_frame.show()

    def hide_menu(self):
        self._menu_frame.hide()

    def back(self):
        if len(self._frames) <= 1:
            self.show_menu()
            return
        last_frame = self._frames[-1]
        last_frame.destroy()
        del(self._frames[-1])
        last_frame = self._frames[-1]
        last_frame.show()

    def cancel(self):
        self.show_menu()

    def quit(self):
        self.master.destroy()