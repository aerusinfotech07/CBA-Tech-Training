# Example 03 from: Pandas vs PySpark DataFrame With Examples

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
               .appName('SparkByExamples.com') \
               .getOrCreate()

data = [("James","","Smith",30,"M",60000),
        ("Michael","Rose","",50,"M",70000),
        ("Robert","","Williams",42,"",400000),
        ("Maria","Anne","Jones",38,"F",500000),
        ("Jen","Mary","Brown",45,"F",0)]

columns = ["first_name","middle_name","last_name","Age","gender","salary"]
pysparkDF = spark.createDataFrame(data = data, schema = columns)
pysparkDF.printSchema()
pysparkDF.show(truncate=False)
