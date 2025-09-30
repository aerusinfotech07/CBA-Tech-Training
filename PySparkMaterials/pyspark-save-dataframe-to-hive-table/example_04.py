# Example 04 from: PySpark Save DataFrame to Hive Table

# Create temporary view
sampleDF.createOrReplaceTempView("sampleView")

# Create a Database CT
spark.sql("CREATE DATABASE IF NOT EXISTS ct")

# Create a Table naming as sampleTable under CT database.
spark.sql("CREATE TABLE ct.sampleTable (id Int, name String, age Int, gender String)")

# Insert into sampleTable using the sampleView. 
spark.sql("INSERT INTO TABLE ct.sampleTable  SELECT * FROM sampleView")

# Lets view the data in the table
spark.sql("SELECT * FROM ct.sampleTable").show()
