from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Uber Rides Analytics").getOrCreate()
    df = spark.read.parquet("data/processed/rides_clean.parquet")
    # Distance moyenne des trajets
    df.groupBy().avg("MILES").show()

    # Nombre de trajets par catégorie
    df.groupBy("CATEGORY").count().show()

    # Top lieux de départ
    df.groupBy("START").count().orderBy("count", ascending=False).show(10)

    # Heures de pointe (extraction de l'heure depuis start_time)
    from pyspark.sql.functions import hour
    df.groupBy(hour("start_time").alias("heure")).count().orderBy("count", ascending=False).show(10)

    # Motifs des trajets (PURPOSE)
    df.groupBy("PURPOSE").count().orderBy("count", ascending=False).show(10)
    spark.stop()

if __name__ == "__main__":
    main()
