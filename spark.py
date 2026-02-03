import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()   
print("DataFrame loaded successfully")
print("DataFrame loaded successfully")