FROM python:3.9

WORKDIR /code

# Installer netcat (pour le script wait-for-it.sh)
RUN apt-get update && apt-get install -y netcat-openbsd

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers du projet
COPY . .

# Ajouter et rendre exécutable le script wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Commande de démarrage (utilise wait-for-it.sh pour attendre la base de données)
CMD ["sh", "-c", "./wait-for-it.sh db 5432 -- uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
