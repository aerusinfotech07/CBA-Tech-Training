# Example 01 from: PySpark – Difference between two dates (days, months, years)

# Imports
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, datediff

# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Create DataFrame
data = [("1","2019-07-01"),("2","2019-06-24"),("3","2019-08-24")]
df=spark.createDataFrame(data=data,schema=["id","date"])

# Calculate the difference between two dates
df2 = df.select(
      col("date"),
      current_date().alias("current_date"),
      datediff(current_date(),col("date")).alias("datediff")
    )
df2.show()
