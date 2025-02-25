import sys, csv
from pathlib import Path
import ipaddress
import json

def est_ip_valide(ard_ip):
    try:
        ipaddress.ip_address((ard_ip))
        return True
    except ValueError:
        return False

if len(sys.argv)<4:
    print("Erreur: Nombre d'argumens incorecte...")
    print("Usage: python ip_log.py fichier -ip adresse_ip")
    exit(1)

if sys.argv[2] != "-ip":
    print("Erreur: Le second argument doit etre '-ip'...")
    print("Usage: python ip_log.py fichier -ip adresse_ip")
    exit(1)
f_path=Path(sys.argv[1])
trouve_ip=sys.argv[3]
if not est_ip_valide(trouve_ip):
    print("Erreur: Adresse IP non valide...")
    print("Usage: python ip_log.py fichier -ip adresse_ip")
    exit(1)

try:
    compteur_ip=0
    with open(f_path,'r',encoding='utf-8') as fichier_csv:
        lignes_csv=csv.reader(fichier_csv)
        for ligne in lignes_csv:
            if trouve_ip==ligne[0]:
                compteur_ip+=1
    print(f"Nombre d'occurences de l'adresse IP {trouve_ip} : {compteur_ip}")
except FileNotFoundError:
    print(f"Erreur: Le fichier '{f_path} est introuvable.")


try:
    dico_json=(trouve_ip : compteur_ip)
    with open('ip.json',mode='a',encoding='utf-8')as fichier_json:
        json.dump(dico_json,fichier_json,indent=4)
except Exception as e:
    print(f"erreur: {type(e)}")