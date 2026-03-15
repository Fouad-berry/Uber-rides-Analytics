from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Uber Rides Analytics").getOrCreate()
    df = spark.read.parquet("data/processed/rides_clean.parquet")
    # Example: Average distance
    df.groupBy().avg("MILES").show()
    # Example: Rides by category
    df.groupBy("CATEGORY").count().show()
    # Example: Top pickup locations
    df.groupBy("START").count().orderBy("count", ascending=False).show(10)
    spark.stop()

if __name__ == "__main__":
    main()
