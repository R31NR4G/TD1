import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage : extract_log_v.py nom_fichier.log mot_cle [-v]")
    sys.exit(1)

f_path = Path(sys.argv[1]).resolve()
mot_cle = sys.argv[2].upper()
flag_verbose = False

if len(sys.argv) == 4:
    if sys.argv[3] != "-v":
        print("Erreur : Le troisième argument doit être '-v' pour l'affichage détaillé.")
        sys.exit(1)
    flag_verbose = True

if not f_path.exists():
    print(f"Erreur : Le fichier '{f_path}' n'existe pas.")
    sys.exit(1)

if not f_path.is_file():
    print(f"Erreur : '{f_path}' n'est pas un fichier valide.")
    sys.exit(1)

if mot_cle not in ["ERROR", "WARNING", "INFO"]:
    print("Erreur : Le mot clé doit être 'ERROR', 'WARNING' ou 'INFO'.")
    sys.exit(1)

compteur = 0
with open(f_path, mode='r', encoding='utf-8') as file:
    for ligne in file:
        if mot_cle in ligne:
            compteur += 1
            if flag_verbose:
                print(ligne.strip())

print(f"Le nombre de lignes contenant {mot_cle} est : {compteur}")