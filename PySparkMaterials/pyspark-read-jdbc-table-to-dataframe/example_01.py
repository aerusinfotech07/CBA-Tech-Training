# Example 01 from: PySpark Query Database Table using JDBC

# Imports
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
           .appName('SparkByExamples.com') \
           .config("spark.jars", "mysql-connector-java-8.0.13.jar") \
           .getOrCreate()

# Query table using jdbc()
df = spark.read \
    .jdbc("jdbc:mysql://localhost:3306/emp", "employee", \
          properties={"user": "root", "password": "root", "driver":"com.mysql.cj.jdbc.Driver"})

# show DataFrame
df.show()
