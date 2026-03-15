from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Uber Rides Analytics").getOrCreate()
    df = spark.read.csv("data/raw/UberDataset.csv", header=True, inferSchema=True)
    df.show(5)
    spark.stop()

if __name__ == "__main__":
    main()
