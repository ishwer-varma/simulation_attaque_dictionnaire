# 🔐 Attaque par dictionnaire – Script Python

Ce projet est un petit programme écrit en Python qui simule une **attaque par dictionnaire** sur un mot de passe donné. Il est destiné à des **fins pédagogiques**, pour montrer comment fonctionne ce type d’attaque.

## 📜 Description

Le script demande à l’utilisateur de saisir un mot de passe (en minuscules), puis tente de le deviner en testant **tous les mots** d’un fichier dictionnaire. À chaque tentative, le programme affiche le mot testé. Une fois le mot de passe trouvé, il affiche :

- Le mot trouvé
- Le nombre de tentatives nécessaires
- Le temps total d’exécution

---

## 📂 Fichiers inclus

- `attaque.py` : script principal du programme
- `dictionnaire_francais.txt` : fichier texte contenant un mot par ligne (à fournir)

---

## ▶️ Comment exécuter le programme

1. Assurez-vous d’avoir **Python 3** installé.
2. Placez un fichier nommé `dictionnaire_francais.txt` dans le même dossier que le script.
3. Lancez le programme :

```bash
python attaque.py
```
## 📌 Exemple de sortie

Veuillez donner un mot dans le dictionnaire en miniscule: chat
Lancement de l'attaque par dictionnaire...

Tentative 1: arbre
Tentative 2: avion
Tentative 3: chat

Mot de passe trouvé : chat
Nombre de tentatives : 3
Temps écoulé : 0.01 secondes

