print("Bienvenue dans le jeu du Pendu")
play=int(input("Tape 1 si tu veux jouer ! \n "))
if play == 1 :
    prénom=input("Quel est ton nom ?")
    print("\n")
    print("Salut", prénom)
import random
liste_mots=["ligotter","meurtre","projet","stylo","informatique","loup","joystick","pouvoir","jouer","dedicasse"]


while play == 1 :
        vie = 13
        mot=(liste_mots[random.randint(0,10)])
        longueur=len(mot)
        barre=["_ "]
        barre=barre*longueur
        grandeur=longueur

while vie!=0 and grandeur!=0 :
    lettre_choisi = input("Choisi une lettre  ")
    print("\n")
if lettre_choisi in mot :
    print("Bravo!")
if lettre_choisi in barre:
    print ("Tu l'as déja dit !")
    resultat = ' '.join(barre)
    print(resultat)
else:
        position=int(mot.index(lettre_choisi))
        barre.pop(position)
        barre.insert(position,lettre_choisi)
        resultat = ' '.join(barre)
        print(resultat)
        grandeur=grandeur-1
else:
    print("Raté")
if grandeur==longueur :
    print(longueur*"_ ")
else:
    print (resultat)
        vie=vie-1
    print("Il te reste",vie,"vies")
    print("\n")


if vie== 0:
    print("Dommage,tu as perdu")
elif grandeur== 0:
    print("Bravo ! Tu as trouvé le mot !")
replay=int(input("Tape 1 pour rejouer, et sur 2 si tu veux quitter le jeu   "))
if replay != 1 :
        break
print(prénom,"vous avez un score de ",score)
