## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---
## Déploiement

### Description du fonctionnement du Pipeline CircleCi

#### Commit sur n'importe quelle branche autre que la master :
- Lancement du job :
    - build-and-test: 
      - créer le build, lance le linter et effectue les tests
      - 
#### Commit sur la branche master :
   
- Lancement des jobs :
     - build-and-test
     - si ok, lancement du job containerize :
        - Cela va créer une image docker et l'uploader sur le docker hub.
## CircleCi :

[https://app.circleci.com/pipelines/github/CharkaouiSalwa](https://app.circleci.com/pipelines/github/CharkaouiSalwa)


Création des variables d'environnement au niveau du projet :

- Dans **Projets**:
- Cliquez sur `Project Settings`  (Les 3 petits points)
- Cliquez sur `Environment Variables`  
- Cliquez sur `Add Environment Variables`  

| Nom des Variables | Valeurs                                                                            |  
|-------------------|------------------------------------------------------------------------------------------------|  
| SECRET_KEY        | 'fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'                                           |  
| DOCKER_PASSWORD   | `Salwa-Pass-1994`                                                                              |  
| DOCKER_USERNAME   | `salwacharkaoui`                                                                               |  
| SENTRY_DSN        | `https://ec3f44c42aca39c986d142dcdb4d5372@o4506071063789568.ingest.sentry.io/4506179316875264` |  
| DOCKER_REPO       | `myapp`                                                                                        |
---
## Docker Hub :

- Télécharger et installer [Docker](https://docs.docker.com/get-docker/)
- Se rendre dans le répertoire du projet `cd /path/to/Python-OC-Lettings-FR`
- Créer l'image `docker build -t <image-name> .` 
- Lancer le conteneur `docker run -d -p 8080:8080 <image-name>`
- Lancer un navigateur avec l'adresse http://127.0.0.1:8080/
---
