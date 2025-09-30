# Example 03 from: PySpark Save DataFrame to Hive Table

# Create database 
spark.sql("CREATE DATABASE IF NOT EXISTS emp")

# Create Hive Internal table
sampleDF.write.mode('overwrite') \
    .saveAsTable("emp.employee")
