from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp

def main():
    spark = SparkSession.builder.appName("Uber Rides Cleaning").getOrCreate()
    df = spark.read.csv("data/raw/UberDataset.csv", header=True, inferSchema=True)
    df = df.withColumn("start_time", to_timestamp("START_DATE", "MM-dd-yyyy HH:mm"))
    df = df.withColumn("end_time", to_timestamp("END_DATE", "MM-dd-yyyy HH:mm"))
    df = df.drop("START_DATE", "END_DATE")
    df.write.mode("overwrite").parquet("data/processed/rides_clean.parquet")
    spark.stop()

if __name__ == "__main__":
    main()
