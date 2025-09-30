# Example 04 from: PySpark withColumnRenamed to Rename Column on DataFrame

from pyspark.sql.functions import *
df4 = df.withColumn("fname",col("name.firstname")) \
      .withColumn("mname",col("name.middlename")) \
      .withColumn("lname",col("name.lastname")) \
      .drop("name")
df4.printSchema()
