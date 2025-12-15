#coding:utf-8

# ceci est un commentaire 
""" 
Commentaire sur plusieurs lignes
"""

identifiant = "vivien"
mot_de_passe = "password123"

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

if user_id == identifiant and user_password == mot_de_passe:
    print("Connexion réussie !")

elif user_id != identifiant and user_password != mot_de_passe:
    print("Identifiant et mot de passe incorrects.")

elif user_id != identifiant:
    print("Identifiant incorrect.")

elif user_password != mot_de_passe:
    print("Mot de passe incorrect.")
