data/
pyspark_jobs/
notebooks/
pip install -r requirements.txt

# Analyse de données Uber avec PySpark

Ce projet analyse des données de trajets Uber à l'aide de PySpark.

L'objectif est de démontrer des compétences en data analytics et big data en construisant un pipeline qui extrait des insights à partir de données de trajets.

---

## Jeu de données

Le dataset Uber contient des informations sur les trajets, notamment :

- Date de début
- Date de fin
- Lieu de départ
- Lieu d'arrivée
- Distance
- Catégorie du trajet
- Motif du trajet

---

## Stack technique

Python  
PySpark  
Apache Spark  
Parquet  
Metabase / Superset  

---

## Structure du projet

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

---

## Questions analytiques

Le projet répond à plusieurs questions :

- Quels sont les motifs de trajets les plus courants ?
- Quels sont les lieux de départ les plus fréquents ?
- Quelle est la distance moyenne d'un trajet ?
- Quelles sont les heures de pointe ?
- Les trajets sont-ils majoritairement professionnels ou personnels ?

---

## Exemples d'insights

- Top lieux de départ
- Top motifs de trajets
- Distance moyenne des trajets
- Répartition des trajets par catégorie

---

## Comment exécuter le projet

1. Créez un environnement virtuel Python :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```


## À quoi sert le dossier data/processed ?

Le dossier `data/processed` contient les données nettoyées et prêtes à l’analyse, générées par le script de nettoyage (`cleaning.py`).

- Le fichier `rides_clean.parquet` est une version optimisée et propre du dataset, au format Parquet (plus rapide et adapté à Spark).
- On l’utilise pour toutes les analyses, ce qui évite de refaire le nettoyage à chaque fois.

---

3. Exécutez les scripts PySpark dans l'ordre suivant :

  a. Ingestion des données (lecture du CSV) :
  ```bash
  python pyspark_jobs/ingestion.py
  ```

  b. Nettoyage et transformation (création du Parquet) :
  ```bash
  python pyspark_jobs/cleaning.py
  ```

  c. Analyses et requêtes :
  ```bash
  python pyspark_jobs/analytics.py
  ```
