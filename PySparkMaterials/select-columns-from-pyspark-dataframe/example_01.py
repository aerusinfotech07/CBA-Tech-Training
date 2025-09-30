# Example 01 from: PySpark Select Columns From DataFrame

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Data
data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]

# Column names
columns = ["firstname","lastname","country","state"]

# Create DataFrame
df = spark.createDataFrame(data = data, schema = columns)
df.show(truncate=False)
