

class KebabControlleur:
    """
    Gère les commandes de kebab
    """
    """
    def __init__(self,kebabmodel):
        self._kebab_model_ = kebabmodel
    """

    def __init__(self):
        self

    def listpain(self):
        return
    def listviande(self):
        return
    def listcrudite(self):
        return
    def listsauce(self):
        return

    def get_ingredient(self):
        pain = self.listpain()
        viande = self.listviande()
        crudite = self.listcrudite()
        sauce = self.listsauce()

        return pain, viande, crudite, sauce
