class Product:
    def __init__(self, name, price, dlc_date, quantity, available):
        self.name = name
        self.price = price
        self.dlc_date = dlc_date
        self.quantity = quantity
        self.available = available

    def _listProduct(self):
        return

    """
    Pour modifier un produit -> Array['name','price','quantity','dlc_date','available']
    """

    def _modifyProduct(self, args):
        self._modifyName(args[0])
        self._modifyPrice(args[1])
        self._modifyDLC(args[2])
        self._modifyQuantity(args[3])
        self._setAvailable(args[4])

    def _modifyPrice(self, price):
        return

    def _modifyName(self, name):
        return

    def _modifyDLC(self, dlc_date):
        return

    def _modifyQuantity(self, quantity):
        return

    def _setAvailable(self, state):
        return
