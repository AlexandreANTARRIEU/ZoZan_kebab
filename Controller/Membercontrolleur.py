import re
import random

class MemberControlleur :
    """
    S'occupe de la gestion des membres des inscriptions
    """
    def __init__(self,membermodel):
        self._member_model_ = membermodel

    def random_string_generator(self):
        chaine = ""
        listecar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        while i < 50:
            i = i+1
            chaine += listecar[random.choice(listecar)]

        return chaine


    def create_member(self, firstname, name, mail, pswd, confirmatio_pswd):
        firstnameok = False
        nameok = False
        mailok = False
        pswdok = False

        x = re.search("^[A-Z][a-z]*$", firstname)
        if x:
            firstnameok =True

        x = re.search("^[A-Z][a-z]*$", name)
        if x:
            nameok = True

        x = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", mail)
        if x:
            mailok = True

        if(pswd == confirmatio_pswd):
            pswdok = True
