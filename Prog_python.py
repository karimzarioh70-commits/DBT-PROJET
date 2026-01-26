message = input("Quel est ton nom ? ")
age = input("Quel est ton âge ? ")

print(f"Salut {message} ! Prêt pour le défi ?")
print("Je vais te faire un petit jeu...")

# L'utilisateur choisit les nombres au départ
num = int(input("Donne-moi le premier nombre : "))
num2 = int(input("Donne-moi le deuxième nombre : "))
resultat_reel = num * num2

print(f"Quel est le produit de {num} x {num2} ? Tu as 5 essais !")

# Boucle de 5 tentatives (0, 1, 2, 3, 4)
for i in range(5):
    tentative = int(input(f"Essai n°{i+1} : "))
    
    if tentative == resultat_reel:
        print(f"Félicitations {message} ! Tu as trouvé la bonne réponse ! 🏆")
        break
    
    else:
        # Si ce n'est pas la dernière tentative (i < 4)
        if i < 3:
            print("C'est faux, réessaie !")
        elif i == 3:
            print("Attention... C'est ta DERNIÈRE chance !")
        else:
            print(f"Dommage ! Le temps est écoulé. La réponse était {resultat_reel}.")