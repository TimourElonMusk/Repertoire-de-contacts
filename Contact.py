class Contact:
    '''Classe Contact, incluant la méthode ToRow() utilisée pour ajouter un contact dans le fichier csv.'''
    def __init__(self, nom, numero, email="", groupe=[]):
        self.nom = nom
        self.numero = numero
        self.email = email
        self.groupe = groupe

    def __str__(self):
        if len(self.email) > 0:
            return(f"{self.nom}, {self.numero} ({self.email})")
        else:
            return(f"{self.nom}, {self.numero}")

    def toRow(self):
        return {
            "nom": self.nom,
            "email": self.email,
            "numero": self.numero,
            "groupe": self.groupe
        }
