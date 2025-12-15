#coding:utf-8

identifiant = "vivien"
mot_de_passe = "1234"

while True:
    user_id = input("Entrez votre identifiant : ")
    user_password = input("Entrez votre mot de passe : ")

    if user_id == identifiant and user_password == mot_de_passe:
        print("Connexion réussie !")
        break
    else:
        print("Identifiant ou mot de passe incorrect. Réessayez.\n")
