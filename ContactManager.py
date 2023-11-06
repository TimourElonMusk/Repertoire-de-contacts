import csv
import os
import time
from Contact import *

class ContactManager:
    '''GESTIONNAIRE DE CONTACTS :
- liste_contacts() -> Imprimer la liste de tous les contacts.
- liste_contacts_groupe() -> Choisir un groupe puis imprimer la liste des contacts du groupe.
- rechercher_contact() -> Rechercher un contact, pour ensuite l'appeler, lui envoyer un message, le modifier ou le supprimer.
- ajouter_contact() -> Ajouter un contact.'''

    FILE_NAME = 'contacts.csv' 
    def __init__(self):
        self.fieldnames = ['nom', 'numero', 'email', 'groupe']

    def __getFile(self, mode='r', newline=False):
        '''Retourne le fichier contacts.csv, en le créant avec le header s'il n'existe pas.'''
        if not os.path.isfile(self.FILE_NAME) or os.path.getsize(self.FILE_NAME) == 0:
            with open(self.FILE_NAME, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
        if newline:
            return open(self.FILE_NAME, mode, newline='')
        else:
            return open(self.FILE_NAME, mode)
        
    
    def __importer_contacts(self):
        '''Importe les contacts du fichier contacts.csv dans une liste et retourne cette liste.'''
        contacts = []
        file = self.__getFile()
        reader = csv.DictReader(file)
        for row in reader:
            if row['groupe'] == '[]':
                contacts.append(Contact(
                    nom=row['nom'],
                    numero=row['numero'],
                    email=row['email']
                ))
            else:
                listeGroupes = []
                groupeEnCours = ""
                for lettre in row['groupe']:
                    if lettre not in ['[',']']:
                        if lettre != ',':
                            groupeEnCours += lettre
                        else:
                            listeGroupes.append(groupeEnCours)
                            groupeEnCours = ""
                contacts.append(Contact(
                    nom=row['nom'],
                    numero=row['numero'],
                    email=row['email'],
                    groupe=listeGroupes
                ))
                        
                        
        return(contacts)
    
    def __sauvegarder_contacts(self):
        '''Si un contact est modifié, le fichier contacts.csv est mis à jour en étant réécrit en entier.'''
        contacts = self.__importer_contacts()
        for contact in contacts:
            contact.groupe = '[' + ','.join(contact.groupe) + ']'
        data = [self.fieldnames, ([contact.nom, contact.numero, contact.email, contact.groupe] for contact in contacts)]
        with open(self.FILE_NAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    
    def liste_contacts(self):
        '''Imprimer la liste de tous les contacts.'''
        contacts = self.__importer_contacts()
        print("""
=====LISTE DES CONTACTS=====
""")
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Aucun contact.")
        time.sleep(0.5)
    
    def liste_contacts_groupe(self):
        '''Choisir un groupe puis imprimer la liste des contacts du groupe.'''
        dicoGroupes = {}
        contacts = self.__importer_contacts()
        for contact in contacts:
            if contact.groupe:
                for groupe in contact.groupe:
                    if groupe in dicoGroupes.keys():
                        dicoGroupes[groupe].append(contact.nom)
                    else:
                        dicoGroupes[groupe] = [contact.nom]
        if not dicoGroupes:
            print("Aucun groupe. Recherchez un contact pour l'ajouter dans un nouveau groupe.")
        else:
            choix1 = 'a'
            while not choix1.isnumeric():
                print("""
=====CHOISIR UN GROUPE=====
""")
                listeNomsGroupes = []
                i = 1
                for groupe in dicoGroupes.keys():
                    print(f"{groupe} : {i}")
                    listeNomsGroupes.append(groupe)
                    i += 1
                choix1 = input("""ECRIRE "STOP" POUR ANNULER
""")
                if choix1.isnumeric():
                    if 1 <= int(choix1) <= len(dicoGroupes):
                        print(f"==={listeNomsGroupes[i-1]}===")
                        for contact in dicoGroupes[listeNomsGroupes[i-1]]:
                            print(f"{contact.nom} ({contact.numero})")
                    else:
                        print("Merci d'écrire un chiffre valide.")
                elif choix1.upper() == 'STOP':
                    break
                else:
                    print("Merci d'écrire un chiffre valide.")
                    choix1 = 'a'
        time.sleep(0.5)

    def rechercher_contact(self):
        '''Rechercher un contact, pour ensuite l'appeler, lui envoyer un message, le modifier ou le supprimer.'''
        contacts = self.__importer_contacts()
        recherche = input("Rechercher un contact : ")
        resultats = []
        for contact in contacts:
            if contact.nom.lower().find(recherche.lower()) != -1:
                resultats.append(contact)
        if resultats:
            if len(resultats) == 1:
                print(f"{len(resultats)} RESULTAT :")
            else:
                print(f"{len(resultats)} RESULTATS :")
            for i in range(len(resultats)):
                print(f"{resultats[i].nom} ({resultats[i].numero}) : {i + 1}")
            choix1 = input("""
Pour choisir une action à réaliser sur un contact, écrire le chiffre correspondant au contact. Pour annuler, écrire STOP.
""").upper()
            if choix1.isnumeric():
                choix1 = int(choix1)
                if 1 <= int(choix1) <= len(resultats):
                    choix2 = input(f"""{resultats[choix1-1].nom} ({resultats[choix1-1].numero})

Appeler : 1
Envoyer un message : 2
Modifier : 3
Supprimer : 4
Annuler : STOP
""")   
                    if choix2 == '1':
                        for sonnerie in range(3):
                            print("BIIIP")
                            time.sleep(2)
                        print(f"Bonjour, vous êtes bien sur le répondeur de {resultats[choix1-1].nom}. Je ne suis pas disponible pour le moment. Merci de me laisser un message après le BIP.")
                        time.sleep(3)
                        print("BIIIIIIP")
                        input()
                    elif choix2 == '2':
                        input("Message : ")
                        print("Votre message a bien été envoyé.")
                    elif choix2 == '3':
                        autreModif = 'O'
                        while autreModif == 'O':
                            choix3 = input("""Que souhaitez-vous modifier ?
Nom : 1
Numero : 2
Adresse email : 3
Groupe(s) : 4
Annuler : STOP
""")
                            if choix3 == '1':
                                resultats[choix1-1].nom = input("Nouveau nom : ")
                            elif choix3 == '2':
                                resultats[choix1-1].numero = input("Nouveau numero : ")
                            elif choix3 == '3':
                                if resultats[choix1-1].email:
                                    choix4 = input("""Souhaitez-vous modifier l'adresse mail ou la supprimer ?
Modifier : 1
Supprimer : 2
Annuler : STOP
""")
                                    if choix4 == '1':
                                        resultats[choix1-1].email = input("Adresse mail : ")
                                    elif choix4 == '2':
                                        resultats[choix1-1].email = ""
                                    elif choix4.upper() == 'STOP':
                                        pass
                                    else:
                                        print("Merci d'écrire un chiffre valide.")
                                else:
                                    resultats[choix1-1].email = input("Adresse mail : ")
                            elif choix3 == '4':
                                dicoGroupes = {}
                                for contact in contacts:
                                    for groupe in contact.groupe:
                                        if contact.groupe in dicoGroupes.keys():
                                            dicoGroupes[contact.groupe].append(contact.nom)
                                        else:
                                            dicoGroupes[contact.groupe] = [contact.nom]
                                if dicoGroupes:
                                    if resultats[choix1-1].groupe:
                                        choix4 = input("""Voulez-vous ajouter le contact dans un groupe ou le supprimer d'un groupe ?
Ajouter : 1
Supprimer : 2
Annuler : STOP""")
                                        if choix4 == '1':
                                            groupesSansContact = []
                                            for groupe in dicoGroupes.keys():
                                                if contact.nom not in dicoGroupes[groupe]:
                                                    groupesSansContact.append(dicoGroupes[groupe])
                                            print("""   Choisir un groupe (écrire "STOP" pour annuler) :""")
                                            for i in range(len(groupesSansContact)):
                                                print(f"{groupesSansContact[i]} : {i+1}")
                                            print(f"AJOUTER UN NOUVEAU GROUPE : {len(groupesSansContact)+1}")
                                            choix5 = input()
                                            if choix5.isnumeric():
                                                if 1 <= int(choix5) <= len(groupesSansContact):
                                                    resultats[choix1-1].groupe.append(groupesSansContact[choix5-1])
                                                    print(f'"Le contact a bien été ajouté dans le groupe "{groupesSansContact[choix5-1]}"')
                                                elif int(choix5) == len(groupesSansContact)+1:
                                                    nom = input("Nom du groupe :")
                                                    resultats[choix1-1].groupe.append(nom)
                                                else:
                                                    print("Merci d'écrire un chiffre valide")
                                            elif choix5.upper() == 'STOP':
                                                pass
                                            else:
                                                print("Merci d'écrire un chiffre valide")
                                        elif choix4 == '2':
                                            print("""   Choisir un groupe (écrire "STOP" pour annuler) :""")
                                            for i in range(len(resultats[choix1-1].groupe)):
                                                print(f"{resultats[choix1-1].groupe[i]} : {i+1}")
                                            choix5 = input()
                                            if choix5.isnumeric():
                                                if 1 <= int(choix5) <= len(resultats[choix1-1].groupe):
                                                    groupeAEnlever = resultats[choix1-1].groupe[i-1]
                                                    resultats[choix1-1].groupe.remove(groupeAEnlever)
                                                    print(f'"Le contact a bien été retiré du groupe "{groupeAEnlever}"')
                                                else:
                                                    print("Merci d'écrire un chiffre valide")
                                            elif choix5.upper() == 'STOP':
                                                pass
                                            else:
                                                print("Merci d'écrire un chiffre valide.")
                                        elif choix4.upper() == 'STOP':
                                            pass
                                        else:
                                            print("Merci d'écrire un chiffre valide.")
                                else:
                                    nom = input("Aucun groupe. Créez votre premier groupe : ")
                                    while not nom:
                                        nom = input("Merci d'écrire un nom : ")
                                    resultats[choix1-1].groupe.append(nom)
                            elif choix3.upper() == 'STOP':
                                pass
                            else:
                                print("Merci d'écrire un chiffre valide.")
                            autreModif = input("Voulez-vous modifier autre chose ? (O / N)")
                            while autreModif.upper() not in ['O','N']:
                                autreModif = input("Merci d'écrire une lettre valide. (O / N)")
                        self.__sauvegarder_contacts()
                    elif choix2.upper() == 'STOP':
                        pass
                    else:
                        print("Merci d'écrire un chiffre valide.")
                        time.sleep(0.5)
                else:
                    print("Merci d'écrire un chiffre valide.")
                    time.sleep(0.5)
            elif choix1.upper() == 'STOP':
                pass
            else:
                print("Merci d'écrire un chiffre valide.")
                time.sleep(0.5)
        else:
            print(f'Aucun contact trouvé pour la recherche "{recherche}".')
            time.sleep(0.5)

    def ajouter_contact(self, contact: Contact):
        '''Ajouter un contact. Prend en argument un contact appartenant à la classe Contact.'''
        existing_contacts = self.__importer_contacts()
        file = self.__getFile('w', newline=True)
        writer = csv.DictWriter(file, fieldnames=self.fieldnames)
        writer.writeheader()
        for existing_contact in existing_contacts:
            writer.writerow(existing_contact.toRow())
        writer.writerow(contact.toRow())
