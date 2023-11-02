import csv

class Contact:
      """Création et gestion d'un contact. Voici les informations disponibles pour un contact :
      - nom
      - numero
      - email
      - groupes"""
      def __init__(self,
                  nom = "SansNom",
                  numero = ["inconnu"],
                  email = [],
                  groupes = []):
        
            self.nom = nom
            self.numero = numero
            self.email = email
            self.groupes = groupes


      def __str__(self):
            ligneNom = f"Nom : {self.nom}"

            if len(self.numero) == 1:
                  ligneNumero = f"Numéro de téléphone : {self.numero[0]}"
            else:
                  ligneNumero = f"Numéros de téléphone : {self.numero[0]}"
                  for num in range(1, len(self.numero)):
                        ligneNumero += f" ; {self.numero[num]}"
            
            if len(self.email) == 0:
                  mail = False
            elif len(self.email) == 1:
                  mail = True
                  ligneMail = f"Adresse mail : {self.email[0]}"
            else:
                  mail = True
                  ligneMail = f"Adresses mail : {self.email[0]}"
                  for adr in range(1, len(self.email)):
                        ligneMail += f" ; + {self.email[adr]}"

            if mail == True:
                  return f"""{ligneNom}
{ligneNumero}
{ligneMail}
"""
            else:
                  return f"""{ligneNom}
{ligneNumero}
""" 


      def ajouter(self, groupesCrees = []):
            """Ajouter un contact à la liste des contacts"""
            self.nom = input("Nom : ")
            
            reponse = "O" #Initialiser la réponse de l'utilisateur par O pour créer un premier numéro
            while reponse == "O":
                  self.numero.append(input("Numéro : "))
                  reponse = input("Voulez-vous ajouter un autre numero ? (O / N)").upper()
                  while reponse != "O" and reponse != "N":
                        reponse = input("Veuillez saisir une lettre valide. (O / N)").upper()
            if self.numero[0] == "inconnu":
                  del self.numero[0]

            reponse = input("Voulez-vous ajouter une adresse e-mail ? (O / N)").upper()
            while reponse != "O" and reponse != "N":
                  reponse = input("Veuillez saisir une lettre valide. (O / N)").upper()
            while reponse == "O":
                  self.email.append(input("Adresse e-mail : "))
                  reponse = input("Voulez-vous ajouter une autre adresse e-mail ? (O / N)").upper()
                  while reponse != "O" and reponse != "N":
                        reponse = input("Veuillez saisir une lettre valide. (O / N)").upper()
            
            if groupesCrees:
                  print("Dans quel(s) groupe(s) souhaitez vous ajouter le contact ? Tapez le(s) chiffre(s) correspondant(s) sans espaces, ou ne tapez rien si vous ne souhaitez pas l'ajouter dans un groupe :")
                  for i in range(len(groupesCrees)):
                        print(f"{groupesCrees[i].nom} : {i + 1}")
                  groupesChoisis = input()
                  for chiffre in groupesChoisis:
                        if 0 <= int(chiffre) - 1 <= len(groupesCrees):
                              group = groupesCrees[int(chiffre) - 1]
                              group.contacts.append(self)
                              self.groupes.append(group.nom)
                        else:
                              print(f"Le chiffre {chiffre} ne correspond à aucun groupe, le contact n'a donc pas été ajouté dans celui-ci.")

            self.enregistrer()
            

      def enregistrer(self):
            """Enregistrement dans le fichier contacts.csv."""
            with open('contacts.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Créer une liste avec les valeurs du contact à écrire dans le fichier CSV
                contact_data = [
                    self.nom,
                    ','.join(self.numero),
                    ','.join(self.email),
                    ','.join(self.groupes)
                ]
                # Écrire les valeurs dans le fichier CSV
                writer.writerow(contact_data)


      def modif(self):
            """Mettre à jour les informations d'un contact."""
            reponse = input("""Que souhaitez-vous modifier ?
  Nom : 1
  Numero : 2
  Email : 3
  Groupes : 4
  Abandonner : STOP
""")
            
            if reponse == '1':
                  self.nom = input("Nouveau nom : ")

            elif reponse == '2':
                  if self.numero[0] == "inconnu":
                        self.numero[0] = input("Nouveau numero : ")
                  elif len(self.numero) == 1:
                        choix = input("""Que souhaitez-vous faire ? :
  Modifier le numéro : 1
  Ajouter un numéro : 2
  Abandonner : STOP
""")
                        if choix == '1':
                              self.numero[0] = input("Nouveau numero : ")
                        elif choix == '2':
                              self.numero.append(input("Nouveau numéro : "))
                        elif choix == 'STOP':
                              pass
                        else:
                              print("Merci d'écrire un chiffre valide.")
                  else:
                        choix = input("""Que souhaitez-vous faire ? :
  Modifier le numéro : 1
  Ajouter un numéro : 2
  Supprimer un numéro : 3
  Abandonner : STOP
""")
                        if choix == '1':
                              print("Liste des numéros :")
                              for i in range(len(self.numero)):
                                    print(f"""  {self.numero[i]} : {i + 1}""")
                              modif = input("Quel numéro souhaitez-vous modifier ? (Entrer le chiffre correspondant)")
                              if 1 <= int(modif) <= len(self.numero):
                                    self.numero[modif - 1] = input("Nouveau numero : ")
                        elif choix == '2':
                              self.numero.append(input("Nouveau numéro : "))
                        elif choix == '3':
                              print("Liste des numéros :")
                              for i in range(len(self.numero)):
                                    print(f"""  {self.numero[i]} : {i + 1}""")
                              suppression = input("Quel numéro souhaitez-vous supprimer ? (Entrer le chiffre correspondant)")
                              if 1 <= int(suppression) <= len(self.numero):
                                    del self.numero[suppression - 1]
                                    print("Le numéro a bien été supprimé.")
                              else:
                                    print("Merci d'écrire un chiffre valide.")
                        elif choix == 'STOP':
                              pass
                        else:
                              print("Merci d'écrire un chiffre valide.")

            elif reponse == '3':
                  if not self.email:
                        self.numero[0] = input("Nouvelle adresse mail : ")
                  elif len(self.numero) == 1:
                        choix = input("""Que souhaitez-vous faire ? :
  Modifier l'adresse mail : 1
  Ajouter une adresse mail : 2
  Abandonner : STOP
""")
                        if choix == '1':
                              self.email[0] = input("Nouvelle adresse mail : ")
                        elif choix == '2':
                              self.email.append(input("Nouvelle adresse mail : "))
                        elif choix == 'STOP':
                              pass
                        else:
                              print("Merci d'écrire un chiffre valide.")
                  else:
                        choix = input("""Que souhaitez-vous faire ? :
  Modifier l'adresse mail : 1
  Ajouter une adresse mail : 2
  Supprimer une adresse mail : 3
  Abandonner : STOP
""")
                        if choix == '1':
                              print("Liste des adresses mail :")
                              for i in range(len(self.email)):
                                    print(f"""  {self.email[i]} : {i + 1}""")
                              modif = input("Quelle adresse mail souhaitez-vous modifier ? (Entrer le chiffre correspondant)")
                              if 1 <= int(modif) <= len(self.email):
                                    self.email[modif - 1] = input("Nouvelle adresse mail : ")
                        elif choix == '2':
                              self.email.append(input("Nouvelle adresse mail : "))
                        elif choix == '3':
                              print("Liste des adresses mail :")
                              for i in range(len(self.email)):
                                    print(f"""  {self.email[i]} : {i + 1}""")
                              suppression = input("Quelle adresse mail souhaitez-vous supprimer ? (Entrer le chiffre correspondant)")
                              if 1 <= int(suppression) <= len(self.email):
                                    del self.email[suppression - 1]
                                    print("L'adresse mail a bien été supprimée.")
                              else:
                                    print("Merci d'écrire un chiffre valide.")
                        elif choix == 'STOP':
                              pass
                        else:
                              print("Merci d'écrire un chiffre valide.")
            
            elif reponse == '4':
                  pass

            elif reponse == 'STOP':
                  pass
            
            else:
                  print("Merci d'écrire un chiffre valide.")


            
class Groupe:
      def __init__(self, nom = "Sans Nom", contacts = []):
            self.nom = nom
            self.contacts = contacts

      
      def __str__(self):
            message = f"""   {self.nom} :
"""
            for contact in self.contacts:
                  message += f"""- {contact}
"""
            return message