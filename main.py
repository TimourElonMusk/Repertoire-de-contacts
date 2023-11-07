from Contact import *
from ContactManager import*
import time
import re


contactManager = ContactManager()

stop = False
while not stop:
    choix1 = input("""
==========REPERTOIRE DE CONTACTS==========
1 : Consulter la liste des contacts
2 : Consulter la liste des contacts d'un groupe
3 : Rechercher un contact (puis choisir une action à réaliser sur le contact)
4 : Créer un contact
STOP : Quitter
""")


    if choix1 == '1':
        contactManager.liste_contacts()

    elif choix1 == '2':
        contactManager.liste_contacts_groupe()
        
    elif choix1 == '3':
        contactManager.rechercher_contact()

    elif choix1 == '4':
        print("""
=====AJOUTER UN CONTACT=====""")
        nom = input("Nom : ")
        while not nom:
            nom = input("Merci d'écrire un nom (OBLIGATOIRE) : ")
        numero = input("Numéro : ")
        while not numero.isnumeric():
            numero = input("Merci d'écrire un numéro valide : ")
        choix2 = input("Voulez-vous ajouter une adresse mail ? (O / N)").upper()
        while choix2 not in ['O','N']:
            choix2 = input("Merci d'écrire une lettre valide. (O / N)")
        if choix2 == 'O':
            patternEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            email = input("Adresse mail : ")
            while not re.match(patternEmail, email) and email != "":
                email = input("Merci d'écrire un email valide (exemple : test@exemple.com) : ")

        else:
            email = ""
        nouveauContact = Contact(
            nom=nom,
            numero=numero,
            email=email
        )
        contactManager.ajouter_contact(nouveauContact)
        print("Contact ajouté. Pour le modifier (et éventuellement l'ajouter dans un groupe), passez par la recherche de contact.")
        time.sleep(0.5)
        
    elif choix1.upper() == 'STOP':
        print("A bientôt !")
        stop = True

    else:
        print("Merci d'écrire un chiffre valide.")
        time.sleep(0.5)
