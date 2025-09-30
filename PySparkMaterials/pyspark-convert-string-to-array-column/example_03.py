# Example 03 from: PySpark Convert String to Array Column

# Import
from pyspark.sql.functions import split, col

# using split()
df2 = df.select(split(col("name"),",").alias("NameArray"))
df2.printSchema()
df2.show()
