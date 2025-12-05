class Produit:
    def __init__(self, id=None, nom=None, prix=None):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __repr__(self):
        return f"Produit(id={self.id}, nom='{self.nom}', prix={self.prix})"
