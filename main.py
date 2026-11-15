taches = []  # chaque tâche : {"numero": int, "titre": str}
prochain_numero = 1


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")

def ajouter_tache():
    global prochain_numero
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append({"numero": prochain_numero, "titre": titre})
    prochain_numero += 1
    print("Tâche ajoutée avec succès.")

def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche dans la liste.")
        return
    for tache in taches:
        print(f"{tache['numero']} - {tache['titre']}")

