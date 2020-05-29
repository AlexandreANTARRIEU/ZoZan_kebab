from Controller.Membercontrolleur import MemberControlleur

def main():
    mbctrl = MemberControlleur()
    mbctrl.create_member("Alexandre", "Antarrieu", "antarrieu@et.esiea.fr", "mmonzboub", "mmonzboub")


if __name__ == "__main__":
    main()