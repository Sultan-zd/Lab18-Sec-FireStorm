# FireStorm Lab 18 - Dynamic Instrumentation & Cloud Exploitation

Une analyse de sécurité dynamique (Audit DAST et Cloud Security) de l'application vulnérable Android "FireStorm". Ce projet illustre le passage de l'analyse statique classique à l'instrumentation dynamique de la mémoire pour forcer l'exécution de code inactif, suivi de l'exploitation d'une base de données cloud mal configurée.

### Fonctionnalités de l'Audit

* **Analyse Statique et Fuite d'Informations :** Décompilation de l'APK via JADX pour identifier l'existence d'une méthode de génération de mot de passe (`Password()`) inactive, et extraction d'identifiants critiques codés en dur (Clé API Google et URL Firebase).
* **Instrumentation Dynamique (Hooking) :** Déploiement d'un environnement d'audit via ADB et injection du serveur Frida sur un émulateur Android avec privilèges Root.
* **Exécution Forcée en Mémoire :** Création d'un script JavaScript (Frida) pour s'attacher au processus, intercepter l'instance `MainActivity` et forcer l'appel de la fonction cachée s'appuyant sur la bibliothèque native (`libfirestorm.so`) afin de récupérer le mot de passe généré en clair.
* **Exploitation Cloud (Firebase) :** Création d'un script Python pour automatiser l'authentification via l'API Google Identity Toolkit avec les identifiants compromis, suivi d'un dump complet de la base de données (`/.json`) pour récupérer le flag final.

### Technologies & Outils

* **Outils d'Analyse :** JADX-GUI (Décompilateur Java), Frida (Framework d'instrumentation dynamique), ADB (Android Debug Bridge), Android Studio (Émulation AOSP).
* **Langages :** JavaScript (Script de hooking), Python (Script d'exploitation d'API).
* **Concepts de Sécurité :** Dynamic Application Security Testing (DAST), Hooking de méthodes inactives, API Key Leakage, Insecure Cloud Database Configuration (Firebase).
* **Environnement :** Windows

### Démonstration & Rapport

Le compte-rendu détaillé de la méthodologie (analyse de surface, configuration de l'environnement, création des scripts Frida/Python et recommandations de remédiation) est disponible directement dans le fichier `rapport.pdf`.

### Installation & Reproductibilité

Clonez le dépôt pour auditer l'application vous-même :
```cmd
git clone https://github.com/Sultan-zd/Lab18-Sec.FireStorm.git
```
Pour exécuter l'injection dynamique (nécessite l'application FireStorm active sur un émulateur rooté) depuis l'invite de commandes Windows (CMD ou PowerShell) :
```cmd
python -m frida_tools.repl -U -l solve.js -n FireStorm
```
Pour exécuter le script d'exploitation de la base de données Firebase et récupérer le flag :
```cmd
python get_flag.py
