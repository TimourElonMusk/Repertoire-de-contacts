from repertoireClasses import *
import csv
import time


def importContacts():
      """Importation des contacts depuis le fichier contacts.csv (renvoie une liste des contacts)"""
      contacts = []
      with open('contacts.csv', 'a+') as file: #a+ permet de créer le fichier s'il n'existe pas (si par exemple un malotru l'a supprimé)
            reader = csv.DictReader(file)
            for row in reader:
                  contact = Contact(
                        nom = row['Nom'],
                        numero = row['Numero'].split(','),
                        email = row['E-mail'].split(','),
                        groupes = row['Groupes'].split(','),
                  )
                  contacts.append(contact)
      return contacts

def importGroupes():
      """Importation des groupes depuis le fichier groupes.csv (renvoie une liste des groupes)"""
      groupes = []
      with open('groupes.csv', 'a+') as file: #a+ permet de créer le fichier s'il n'existe pas (si par exemple un garnement l'a supprimé)
            reader = csv.reader(file)
            for row in reader:
                  groupe = Groupe(
                        nom = row['Nom'],
                        contacts = row['Contacts']
                  )
                  groupes.append(groupe)
      return groupes



contacts = importContacts().sort
groupes = importGroupes()

chiffre = input("""==========REPERTOIRE DE CONTACTS==========
Consulter la liste des contacts : 1
Consulter la liste des contacts d'un groupe : 2
Rechercher un contact (puis choisir une action à réaliser sur le contact) : 3
Créer un contact : 4
Créer un groupe : 5
Quitter : STOP
""")

if chiffre == '1':
      print("""=====LISTE DES CONTACTS=====
""")

      for i in range(len(contacts)):
            lettre = contacts[i].nom[0]
            if contacts[i-1].nom[0] != lettre and i-1 >= 0:
                  print(f" =={lettre}==") 
            print(contacts[i])

elif chiffre == '2':
      print("""=====CHOISIR UN GROUPE=====
""")
      for i in range(len(groupes)):
            print(f"""{groupes[i]} : {i + 1}""")
      reponse = input("""
Pour choisir un groupe, écrire le chiffre correspondant. Pour quitter, écrire STOP.
""")
      if 1 <= int(reponse) <= len(groupes):
            print(groupes[reponse - 1])
      else:
            print("Merci d'écrire un chiffre valide.")
      
elif chiffre == '3':
      recherche = input("Rechercher un contact : ")
      resultats = []
      for contact in contacts:
            if contact.nom.lower().find(recherche.lower()) != -1:
                  resultats.append(contact)
      if resultats:
            print(f"{len(resultats)} résultats :")
            for i in range(len(resultats)):
                  print(f"{resultats[i].nom} : {i + 1}")
            reponse = input("""
Pour choisir une action à réaliser sur un contact, écrire le chiffre correspondant au contact. Pour quitter, écrire STOP.
""")
            if 1 <= int(reponse) <= len(resultats):
                  reponse2 = input(f"""{resultats[reponse - 1]}

Appeler : 1
Envoyer un message : 2
Modifier : 3
Supprimer :
""")
                  if reponse2 == '1':
                        if len(resultats[reponse - 1].numero[0]) != "inconnu":
                              for sonnerie in range(3):
                                    print("BIIIP")
                                    time.sleep(2)
                              print(f"Bonjour, vous êtes bien sur le répondeur de {reponse.nom}. Je ne suis pas disponible pour le moment. Merci de me laisser un message après le BIP.")
                              time.sleep(2)
                              print("BIIIIIIP")
                              input()
                        else:
                              print("Le numéro est introuvable.")
                  elif reponse2 == '2':
                        input("Message : ")
                        print("Votre message a bien été envoyé.")
                  elif reponse2 == '3':
                        autreModif = 'O'
                        while autreModif == 'O':
                              pass
                  elif reponse2 == 'STOP':
                        pass
                  else:
                        print("Merci d'écrire un chiffre valide.")
            else: print("Merci d'écrire un chiffre valide.")

      else:
            print(f'Aucun contact trouvé pour la recherche "{recherche}"')

elif chiffre == 'STOP':
      pass

else:
      print("Merci d'écrire un chiffre valide.")