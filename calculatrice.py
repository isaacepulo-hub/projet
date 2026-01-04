import sys



# Demande de l'opération avec gestion d'erreur
try:
    operation = int(input("""Choisissez une opération :
1 : addition
2 : soustraction
3 : multiplication
4 : division
>>> """))
except ValueError:
    print("Erreur : vous devez entrer un nombre entre 1 et 4.")
    sys.exit()

# Vérifie si le numéro est valide
if operation < 1 or operation > 4:
    print("Erreur : opération invalide. Choisissez entre 1 et 4.")
    sys.exit()

# Boucle principale
while True:
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le second nombre : "))
    except ValueError:
        print("Erreur : vous devez entrer des nombres valides.")
        continue  # recommencer la boucle

    # Fonctions
    def addition():
        return a + b

    def soustraction():
        return a - b

    def multiplication():
        return a * b

    def division():
        try:
            return a / b
        except ZeroDivisionError:
            print("Erreur : division par zéro impossible.")
            return None

    # Calcul en fonction du choix
    if operation == 1:
        print("Résultat de l'addition :", addition())
    elif operation == 2:
        print("Résultat de la soustraction :", soustraction())
    elif operation == 3:
        print("Résultat de la multiplication :", multiplication())
    elif operation == 4:
        result = division()
        if result is not None:
            print("Résultat de la division :", result)

    # Demande à l'utilisateur s'il veut recommencer
    recommencer = input("Voulez-vous recommencer ? (o/n) : ").lower()
    if recommencer != "o":
        print("Merci d'avoir utilisé la calculatrice !")
        break












































































