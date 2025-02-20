import sys
from pathlib import Path

if len(sys.argv) < 5:
    print("Erreur : Vous devez fournir au moins 4 arguments : nom du fichier, nom, prénom, et au moins une note.")
    sys.exit(1)

f_path = Path(sys.argv[1]).resolve()
nom = sys.argv[2].upper()
prenom = sys.argv[3].capitalize()

try:
    notes = list(map(float, sys.argv[4:]))
except ValueError:
    print("Erreur : Toutes les notes doivent être des nombres valides.")
    sys.exit(1)

moyenne = sum(notes) / len(notes)
moyenne_formatee = f"{moyenne:.1f}"

with open(f_path, mode='a', newline='') as file:
    file.writelines(f"{nom}, {prenom}, {moyenne_formatee}\n")

print(f"La moyenne de {prenom} {nom} a été mise dans {str(f_path)}")
