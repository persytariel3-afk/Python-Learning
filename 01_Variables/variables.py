'''
=========================================================
EXERCICES - CHAPITRE 2 : VARIABLES ET OPÉRATIONS EN PYTHON
=========================================================

Exercice 1 : Les nombres de Friedman

Les nombres de Friedman sont des nombres qui peuvent être exprimés
en utilisant tous leurs chiffres dans une expression mathématique.

Exemple :
347 = 4 + 7**3

Consigne :

Déterminez si les expressions suivantes correspondent
à des nombres de Friedman.

Pour cela :

1. Écrivez chaque expression en Python.
2. Exécutez-la.
3. Vérifiez si le résultat correspond au nombre formé
   par les chiffres utilisés.
'''

print("========== Exercice 1 ==========\n")

print("Question 1 : 7 + 3**6")

# Je pense que Python va d'abord calculer 3**6
# puis ajouter 7 au résultat.

print("Résultat :", 7 + 3**6)

print("\n---------------------------------\n")

print("Question 2 : (3 + 4)**3")

# Je pense que Python va calculer l'addition
# entre 3 et 4 avant d'élever le résultat
# à la puissance 3.

print("Résultat :", (3 + 4)**3)

print("\n---------------------------------\n")

print("Question 3 : 3**6 - 5")

# Python calcule d'abord 3**6
# puis soustrait 5.

print("Résultat :", 3**6 - 5)

print("\n---------------------------------\n")

print("Question 4 : (1 + 2**8) * 5")

# Python calcule d'abord 2**8.
# Ensuite il additionne 1.
# Enfin il multiplie le résultat par 5.

print("Résultat :", (1 + 2**8) * 5)

print("\n---------------------------------\n")

print("Question 5 : (2 + 1**8)**7")

# Python calcule d'abord 1**8.
# Ensuite il additionne 2.
# Enfin il élève le résultat à la puissance 7.

print("Résultat :", (2 + 1**8)**7)

print("\n\n")

'''
=========================================================
Exercice 2 : Prédire le résultat des opérations
=========================================================

Consigne :

Essayez de prédire le résultat de chaque instruction
avant de l'exécuter dans Python.

Ensuite, comparez votre réponse avec le résultat obtenu.
'''

print("========== Exercice 2 ==========\n")

print("Question 1 : (1 + 2) ** 3")

# Python effectue d'abord l'addition.
# Ensuite il élève le résultat à la puissance 3.

print("Résultat :", (1 + 2) ** 3)

print("\n---------------------------------\n")

print('Question 2 : "Da" * 4')

# Python répète la chaîne "Da"
# quatre fois.

print("Résultat :", "Da" * 4)

print("\n---------------------------------\n")

print('Question 3 : "Da" + 3')

# Je pense qu'il y aura une erreur.
# En Python, on ne peut pas additionner
# une chaîne de caractères (str)
# avec un entier (int).

# print("Da" + 3)

print("Résultat attendu : TypeError")

print("\n---------------------------------\n")

print('Question 4 : ("Pa" + "La") * 2')

# Python concatène d'abord les deux chaînes.
# Ensuite il répète le résultat deux fois.

print("Résultat :", ("Pa" + "La") * 2)

print("\n---------------------------------\n")

print('Question 5 : ("Da" * 4) / 2')

# Je pense qu'il y aura une erreur.
# La division n'est pas autorisée
# sur une chaîne de caractères.

# print(("Da" * 4) / 2)

print("Résultat attendu : TypeError")

print("\n---------------------------------\n")

print("Question 6 : 5 / 2")

# La division classique retourne
# toujours un nombre décimal.

print("Résultat :", 5 / 2)

print("\n---------------------------------\n")

print("Question 7 : 5 // 2")

# La division entière retourne
# uniquement la partie entière.

print("Résultat :", 5 // 2)

print("\n---------------------------------\n")

print("Question 8 : 5 % 2")

# L'opérateur modulo retourne
# le reste de la division.

print("Résultat :", 5 % 2)

print("\n\n")

'''
=========================================================
Exercice 3 : Opérations et conversions de types
=========================================================

Consigne :

Prédisez le résultat de chaque instruction
avant son exécution.

Ensuite, vérifiez votre réponse.
'''

print("========== Exercice 3 ==========\n")

print('Question 1 : str(4) * int("3")')

# int("3") donne 3.
# str(4) donne "4".
# Python répète donc la chaîne "4"
# trois fois.

print("Résultat :", str(4) * int("3"))

print("\n---------------------------------\n")

print('Question 2 : int("3") + float("3.2")')

# int("3") devient 3.
# float("3.2") devient 3.2.
# Python effectue ensuite l'addition.

print("Résultat :", int("3") + float("3.2"))

print("\n---------------------------------\n")

print('Question 3 : str(3) * float("3.2")')

# Je pense qu'il y aura une erreur.
# Une chaîne ne peut pas être multipliée
# par un nombre décimal (float).

# print(str(3) * float("3.2"))

print("Résultat attendu : TypeError")

print("\n---------------------------------\n")

print("Question 4 : str(3 / 4) * 2")

# Python calcule d'abord 3/4.
# Il convertit ensuite le résultat en chaîne.
# Enfin il répète cette chaîne deux fois.

print("Résultat :", str(3 / 4) * 2)
