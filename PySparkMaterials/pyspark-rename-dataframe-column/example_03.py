# Example 03 from: PySpark withColumnRenamed to Rename Column on DataFrame

from pyspark.sql.functions import *
df.select(col("name.firstname").alias("fname"), \
  col("name.middlename").alias("mname"), \
  col("name.lastname").alias("lname"), \
  col("dob"),col("gender"),col("salary")) \
  .printSchema()
