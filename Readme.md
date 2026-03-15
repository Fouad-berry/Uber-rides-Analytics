
# Analyse de données Uber avec PySpark

Ce projet analyse des données de trajets Uber avec PySpark et visualise les insights avec Apache Superset.

L'objectif est de démontrer des compétences en data analytics et data engineering en construisant un pipeline qui nettoie les données, les stocke dans des formats optimisés et crée des dashboards interactifs.

------------------------------------------------------------------------


# Architecture du projet

Uber CSV Dataset\
↓\
Nettoyage PySpark\
↓\
Parquet (Data Lake)\
↓\
Base SQLite\
↓\
Dashboard Apache Superset

------------------------------------------------------------------------


# Stack technique

- Python
- PySpark
- Apache Spark
- Pandas
- SQLite
- Apache Superset
- Parquet

------------------------------------------------------------------------


# Structure du projet

        uber-rides-analytics-pyspark

        data/
            raw/
                UberDataset.csv

            processed/
                rides_clean.parquet

        pyspark_jobs/
            ingestion.py
            cleaning.py
            analytics.py

        notebooks/
            exploration.ipynb

        dashboards/

        requirements.txt
        superset_config.py
        README.md

------------------------------------------------------------------------


# Jeu de données

Le dataset contient des informations sur les trajets Uber, notamment :

- Date de début
- Date de fin
- Lieu de départ
- Lieu d'arrivée
- Distance
- Catégorie du trajet
- Motif du trajet

Colonnes :

    START_DATE
    END_DATE
    CATEGORY
    START
    STOP
    MILES
    PURPOSE

------------------------------------------------------------------------


# Deux environnements Python

Ce projet utilise **deux environnements Python séparés** car :

- PySpark nécessite **pandas \>= 2.2**
- Apache Superset nécessite **pandas \< 2.2**

Pour éviter les conflits de dépendances, on les sépare :

    spark_env → pipeline PySpark
    .venv → Apache Superset

------------------------------------------------------------------------


# 1. Créer l'environnement PySpark

Cet environnement exécute le pipeline de données.

    python3 -m venv spark_env
    source spark_env/bin/activate

Installer les dépendances :

    pip install pyspark pandas>=2.2

------------------------------------------------------------------------


# 2. Exécuter le pipeline PySpark

Dans l'environnement Spark :

    source spark_env/bin/activate

Lancer les scripts :

    python pyspark_jobs/ingestion.py
    python pyspark_jobs/cleaning.py
    python pyspark_jobs/analytics.py

Le script de nettoyage va :

- Nettoyer le dataset
- Sauvegarder les données optimisées en Parquet
- Exporter les données dans une base SQLite (`uber.db`) utilisée par Superset

Fichiers générés :

    data/processed/rides_clean.parquet
    uber.db

------------------------------------------------------------------------


# Pourquoi data/processed existe ?

Le dossier `data/processed` contient les **données nettoyées** prêtes pour l'analyse.

Exemple :

    rides_clean.parquet

Avantages :

- requêtes plus rapides
- optimisé pour Spark
- évite de refaire le nettoyage à chaque fois

------------------------------------------------------------------------


# 3. Créer l'environnement Superset

Superset s'exécute dans un environnement séparé.

    python3 -m venv .venv
    source .venv/bin/activate

Installer Superset :

    pip install apache-superset pandas==2.1.4

------------------------------------------------------------------------


# 4. Initialiser Apache Superset

Avant de lancer Superset, assure-toi qu'il charge la configuration personnalisée :

    export SUPERSET_CONFIG_PATH=$(pwd)/superset_config.py

Initialiser Superset :

    superset db upgrade
    superset fab create-admin
    superset init

Lancer Superset :

    superset run -p 8088 --with-threads --reload --debugger

Ouvre dans ton navigateur :

    http://localhost:8088

------------------------------------------------------------------------


# Connecter Superset à SQLite

Dans Superset :

Settings → Database Connections → Add Database

Connection string :

    sqlite:///uber.db

------------------------------------------------------------------------


# Ajouter le dataset

Datasets → Add Dataset

Choisir :

    uber_rides

------------------------------------------------------------------------


# Créer des graphiques

Graphiques recommandés pour ce dataset :

### Répartition par catégorie

Pie Chart\
Dimension : CATEGORY\
Métrique : COUNT(*)

### Top lieux de départ

Bar Chart\
Dimension : START\
Métrique : COUNT(*)

### Top destinations

Bar Chart\
Dimension : STOP\
Métrique : COUNT(*)

### Distribution des distances

Histogramme\
Colonne : MILES

------------------------------------------------------------------------


# Questions analytiques

Ce projet répond à plusieurs questions métier :

- Quels sont les motifs de trajets les plus courants ?
- Quels sont les lieux de départ les plus fréquents ?
- Quelle est la distance moyenne d'un trajet ?
- Quelles sont les heures de pointe ?
- Les trajets sont-ils majoritairement professionnels ou personnels ?

------------------------------------------------------------------------


# Exemples d'insights

- Top lieux de départ
- Top motifs de trajets
- Distance moyenne des trajets
- Répartition des trajets par catégorie

------------------------------------------------------------------------


# Améliorations futures

Extensions possibles :

- Ajouter Apache Airflow pour l'orchestration du pipeline
- Déployer les dashboards avec Docker
- Stocker les données dans DuckDB ou PostgreSQL
- Construire des pipelines ETL automatisés

------------------------------------------------------------------------


# Auteur

Projet d'analyse de données Uber avec PySpark et Apache Superset.