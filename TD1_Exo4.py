import argparse

parser = argparse.ArgumentParser(
    usage="python calcul_pars.py nombre1 operateur nombre2 [-v] [-f filename.txt]",
    description="Effectue une opération mathématique entre deux nombres."
)

parser.add_argument("nb1", type=float, help="1er nombre (obligatoire)")
parser.add_argument("op", type=str, help="Opérateur mathématique (+, -, *, /) (obligatoire)")
parser.add_argument("nb2", type=float, help="2ème nombre (obligatoire)")
parser.add_argument("-f", type=str, metavar="Fichier", help="Nom du fichier de sortie (facultatif)")
parser.add_argument("-v", action="store_true", help="Active le mode verbeux (facultatif)")

arguments = parser.parse_args()

nb1 = arguments.nb1
nb2 = arguments.nb2
op = arguments.op
verbose = arguments.v
file_name = arguments.f

result = None
if op == "+":
    result = nb1 + nb2
elif op == "-":
    result = nb1 - nb2
elif op == "*":
    result = nb1 * nb2
elif op == "/":
    if nb2 != 0:
        result = nb1 / nb2
    else:
        print("Erreur : Division par zéro.")
        exit(1)
else:
    print("Erreur : Opérateur non valide. Utilisez +, -, * ou /.")
    exit(1)

if verbose:
    print(f"Calcul : {nb1} {op} {nb2} = {result}")
else:
    print(result)

if file_name:
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{nb1} {op} {nb2} = {result}\n")
    if verbose:
        print(f"Résultat enregistré dans {file_name}")
