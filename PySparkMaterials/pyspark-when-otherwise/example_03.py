# Example 03 from: PySpark When Otherwise | SQL Case When Usage

from pyspark.sql.functions import expr, col

#Using Case When on withColumn()
df3 = df.withColumn("new_gender", expr("CASE WHEN gender = 'M' THEN 'Male' " + 
               "WHEN gender = 'F' THEN 'Female' WHEN gender IS NULL THEN ''" +
               "ELSE gender END"))
df3.show(truncate=False)
+-------+------+------+----------+
|name   |gender|salary|new_gender|
+-------+------+------+----------+
|James  |M     |60000 |Male      |
|Michael|M     |70000 |Male      |
|Robert |null  |400000|          |
|Maria  |F     |500000|Female    |
|Jen    |      |null  |          |
+-------+------+------+----------+

#Using Case When on select()
df4 = df.select(col("*"), expr("CASE WHEN gender = 'M' THEN 'Male' " +
           "WHEN gender = 'F' THEN 'Female' WHEN gender IS NULL THEN ''" +
           "ELSE gender END").alias("new_gender"))
