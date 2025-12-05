class Client:
    def __init__(self, id=None, nom=None, email=None):
        self.id = id
        self.nom = nom
        self.email = email

    def __repr__(self):
        return f"Client(id={self.id}, nom='{self.nom}', email='{self.email}')"
