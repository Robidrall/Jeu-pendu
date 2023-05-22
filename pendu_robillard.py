"""Vous pouvez voir les détails de la fonctionnalité
   du code dans le fichier README.md
   Ce script permet de simuler le jeu du pendu, vous devez deviner un mot parmi
   une liste aléatoire. Testez pour voir si vous serez le grand gagnant."""

#On commence par importer les librairies et variables nécessaires.
import string
import random
alphabet = string.ascii_lowercase
mot_pendu = ""
message_dechiffre = ""

#Nous ouvrons un fichier qui contient les différents mots nécessaires au jeu du pendu.
with open("mots_pendu.txt", "r") as f1:
#Chaque ligne représente un mot différent, il faut en choisir un
    fichier_mots = f1.readlines()
    mot_pendu = random.choice(fichier_mots)
#Le but de ces deux lignes de code est de lire chaque ligne et de prendre un mot au hasard

# L'utilisateur doit rentrer une lettre
#Définition d'une fonction "jeu_du_pendu()" qui pourrait etre optimisé en plusieurs fonctions
def jeu_du_pendu():
#on déclare les variables de la fonction
    essai = 6
    lettres_indiquees = []
#la ligne "tant que" est ici pour lancer le code jusqu'au moment
#ou l'utilisateur n'a plus d'essais, la condition est à la fin
    while True:
        print("Il vous reste", essai, "essais")
        entrez_votre_lettre = input("Entrez une lettre en minuscule : ")
#l'utilisateur doit rentrer une lettre minsucule avec cette ligne

#La variable "lettre_indiquees" est créée dans le but d'enregistrer les lettres inscrites par l'utilisateur
        if entrez_votre_lettre in lettres_indiquees:
            print("Choisissez une autre lettre (lettre déja indiquée).")
            continue

#Cette ligne considère les cas ou l'utilisateur n'entre pas une lettre minuscule
        elif entrez_votre_lettre not in alphabet:
            print("Veuillez entrer une lettre minuscule.")
            continue

#A chaque lettre donnée par l'utilisateur, elle s'ajoute dans la liste
        lettres_indiquees.append(entrez_votre_lettre)
        mot_caché = ""

#Début d'une boucle "for" au cas ou la lettre rentrée est dans le mot.
        for lettre_dechiffre in mot_pendu:
            if lettre_dechiffre in alphabet:
                if lettre_dechiffre in lettres_indiquees:
#Si la lettre rentrée est dans le mot, on remplace le "_" par la lettre.
                    mot_caché += lettre_dechiffre
                else:
#Sinon, le mot caché reste identique et conserve son "_"
                    mot_caché += "_"
            else:
                mot_caché += lettre_dechiffre

        print(mot_caché)

#Si l'utilisateur trouve toutes les lettres :
        if mot_caché == mot_pendu:
            print("Vous avez deviné le mot :", mot_pendu)
            break

#Si la lettre entrée par l'utilisateur n'est pas dans le mot :
        elif entrez_votre_lettre not in mot_pendu:
            essai -= 1
#Un essai est enlevé si la lettre entrée par l'utilisateur n'est pas dans le mot.
            print("La lettre", entrez_votre_lettre, "n'est pas dans le mot.")
#Enfin, si l'utilisateur n'a plus d'essai :
            if essai == 0:
                print("Vous n'avez plus d'essais, vous avez donc perdu.")
                print("Le mot était :", mot_pendu)
                break
        print("Les lettres déja indiquées sont : ", lettres_indiquees)
        print(mot_caché)

jeu_du_pendu()
