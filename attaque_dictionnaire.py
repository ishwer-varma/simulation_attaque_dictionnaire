"""
Ce projet est un petit programme en Python qui simule une attaque par dictionnaire sur un mot de passe.
L’utilisateur saisit un mot de passe, et le script tente de le retrouver en testant tous les mots d’un
fichier dictionnaire.

"""

import time  # Pour mesurer le temps d'exécution

# Fonction pour demander à l'utilisateur de définir un mot de passe
def demander_mdp():
    mdp = input("Veuillez donner un mot dans le dictionnaire en miniscule: ")
    return mdp

# Fonction pour importer un dictionnaire depuis un fichier
def importer_dictionnaire(fichier):
    try:
        with open(fichier, 'r') as file: # Ouvre le fichier en mode lecture
            dictionnaire = [line.strip() for line in file.readlines()] # Lit toutes les lignes du fichier, enlève les espaces sauts de ligne et
                                                                       #stocke le tout dans un dictionnaire
        print(f"Dictionnaire importé avec {len(dictionnaire)} mots.") # Test pour confirmé le dictionnaire a été chargé avec succès
        return dictionnaire # renvoie la liste de mots
    except FileNotFoundError:
        print("Erreur : Le fichier dictionnaire n'a pas été trouvé.")
        return []

# Fonction simulant l'attaque par dictionnaire
def attaque_par_dictionnaire(mot_de_passe_correct, dictionnaire):
    print("Lancement de l'attaque par dictionnaire...\n")

    tentatives = 0  # Compteur de tentatives
    start_time = time.time()  # Enregistrer le temps de départ

    for mot in dictionnaire:
        tentatives += 1
        print(f"\rTentative {tentatives}: {mot}")  # Affichage sur la même ligne
        if mot == mot_de_passe_correct:
            end_time = time.time()  # Enregistrer le temps de fin
            elapsed_time = end_time - start_time  # Calcul du temps écoulé
            print(f"\nMot de passe trouvé : {mot}")
            print(f"Nombre de tentatives : {tentatives}")
            print(f"Temps écoulé : {elapsed_time:.2f} secondes")
            return mot

    end_time = time.time()  # Enregistrer le temps de fin
    elapsed_time = end_time - start_time  # Calcul du temps écoulé
    print(f"\nMot de passe introuvable dans le dictionnaire.")
    print(f"Nombre de tentatives : {tentatives}")
    print(f"Temps écoulé : {elapsed_time:.2f} secondes")
    return None


def main():
    # Demander à l'utilisateur de créer un mot de passe
    mot_de_passe = demander_mdp()

    # Le fichier dictionnaire est fixé ici
    fichier_dictionnaire = "dictionnaire_francais.txt"
    dictionnaire = importer_dictionnaire(fichier_dictionnaire)

    if dictionnaire:
        # Lancer l'attaque par dictionnaire
        attaque_par_dictionnaire(mot_de_passe, dictionnaire)

# Lancer le programme principal
if __name__ == "__main__":
    main()
