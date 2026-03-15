from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, when, col, expr


def main():
    spark = SparkSession.builder.appName("Uber Rides Cleaning").getOrCreate()
    # Lire toutes les colonnes en string pour éviter les erreurs de cast
    df = spark.read.csv("data/raw/UberDataset.csv", header=True, inferSchema=False)

    # Remplacer 'Unknown' par None dans toutes les colonnes
    for c in df.columns:
        df = df.withColumn(c, when(col(c) == "Unknown", None).otherwise(col(c)))

    # Caster la colonne MILES en float
    from pyspark.sql.types import FloatType
    df = df.withColumn("MILES", col("MILES").cast(FloatType()))

    # Gérer plusieurs formats de date pour START_DATE et END_DATE
    df = df.withColumn(
        "start_time",
        expr(
            "coalesce(" +
            "try_to_timestamp(START_DATE, 'MM-dd-yyyy HH:mm'), " +
            "try_to_timestamp(START_DATE, 'M/d/yyyy HH:mm'), " +
            "try_to_timestamp(START_DATE, 'M/d/yy H:mm')"
            ")"
        )
    )
    df = df.withColumn(
        "end_time",
        expr(
            "coalesce(" +
            "try_to_timestamp(END_DATE, 'MM-dd-yyyy HH:mm'), " +
            "try_to_timestamp(END_DATE, 'M/d/yyyy HH:mm'), " +
            "try_to_timestamp(END_DATE, 'M/d/yy H:mm')"
            ")"
        )
    )
    df = df.drop("START_DATE", "END_DATE")
    df.write.mode("overwrite").parquet("data/processed/rides_clean.parquet")
    spark.stop()

if __name__ == "__main__":
    main()
