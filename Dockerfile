# l'image de base Python 3.9
FROM python:3.9-alpine

# configuration du répertoire de travail
WORKDIR /usr/src/app


# variables d'environnements
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_SDN $SENTRY_SDN
ENV PORT 8080

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt ./

# Copiez le reste de l'application
COPY . .

# Installez les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Exécutez la commande de démarrage de l application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]