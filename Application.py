from Controller.Membercontrolleur import MemberControlleur
from Controller.kebabcontrolleur import KebabControlleur
from Vue.root_frame import RootFrame


def main():
    #kbabctrl = KebabControlleur()
    #mbctrl = MemberControlleur()
    #mbctrl.create_member("Alexandre", "Antarrieu", "antarrieu@et.esiea.fr", "mmonzboub", "mmonzboub")

    # init vue
    root = RootFrame()
    root.master.title("ZoZan Kebab")
    root.show_menu()

    # start
    root.mainloop()


if __name__ == "__main__":
    main()
