import re
import random
import hashlib

class MemberControlleur :
    """
    S'occupe de la gestion des membres des inscriptions
    """

    def __init__(self,Member):
        self._member_model_ = Member
        

    def __init__(self):
        self

    def random_string_generator(self):
        chaine = ""
        listecar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        while i < 50:
            i = i+1
            chaine = chaine + random.choice(listecar)
        return chaine


    def inscription(self, name ,firstname, mail, pswd, confirmatio_pswd):
        firstnameok = False
        nameok = False
        mailok = False
        pswdok = False
        creatok = False

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

        epre = ""
        epre = self.random_string_generator()
        pswd_empreinte = pswd + epre

        sha256 = hashlib.sha256(pswd_empreinte.encode('utf-8')).hexdigest()
        if(firstnameok == True & nameok == True & mailok == True & pswdok == True):
            print("entrée valide")
            creatok = True
        else:
            print("entree invalide")
            creatok = False
        return creatok

    def print_member(self):
        return

    def verif_presence(self,mail):
        ok=False
        content =_getmail(mail)
        if(content == mail):
            ok=True
        return ok

    def login(self, name, firstname, mail, pswd):
        ok = False
        content = _getuser(name, firstname, mail, pswd)
        if (content[0] == name & content[1] == firstname & content[2] == mail & content[3] == pswd ):
            ok = True
        return ok
