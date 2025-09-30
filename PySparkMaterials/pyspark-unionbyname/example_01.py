# Example 01 from: PySpark unionByName()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Create DataFrame df1 with columns name, and id
data = [("James",34), ("Michael",56), \
        ("Robert",30), ("Maria",24) ]

df1 = spark.createDataFrame(data = data, schema=["name","id"])
df1.printSchema()

# Create DataFrame df2 with columns name and id
data2=[(34,"James"),(45,"Maria"), \
       (45,"Jen"),(34,"Jeff")]

df2 = spark.createDataFrame(data = data2, schema = ["id","name"])
df2.printSchema()
