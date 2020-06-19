from Controller.Membercontrolleur import MemberControlleur
from Controller.kebabcontrolleur import KebabControlleur
def main():
    kbabctrl = KebabControlleur()
    mbctrl = MemberControlleur()
    mbctrl.create_member("Alexandre", "Antarrieu", "antarrieu@et.esiea.fr", "mmonzboub", "mmonzboub")


if __name__ == "__main__":
    main()