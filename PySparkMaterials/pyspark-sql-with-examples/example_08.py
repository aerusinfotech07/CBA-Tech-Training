# Example 08 from: PySpark SQL Tutorial with Examples

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com') \
                    .getOrCreate()
                    
# Create DataFrame
df = spark.read \
          .option("header",True) \
          .csv("/Users/admin/simple-zipcodes.csv")
df.printSchema()
df.show()

# Create SQL table
spark.read \
          .option("header",True) \
          .csv("/Users/admin/simple-zipcodes.csv") \
          .createOrReplaceTempView("Zipcodes")
          
# Select query
df.select("country","city","zipcode","state") \
     .show(5)

spark.sql("SELECT  country, city, zipcode, state FROM ZIPCODES") \
     .show(5)
     
# where
df.select("country","city","zipcode","state") \
  .where("state == 'AZ'") \
  .show(5)

spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state = 'AZ' """) \
     .show(5)
     
# sorting
df.select("country","city","zipcode","state") \
  .where("state in ('PR','AZ','FL')") \
  .orderBy("state") \
  .show(10)
  
spark.sql(""" SELECT  country, city, zipcode, state FROM ZIPCODES 
          WHERE state in ('PR','AZ','FL') order by state """) \
     .show(10)

# grouping
df.groupBy("state").count() \
  .show()

spark.sql(""" SELECT state, count(*) as count FROM ZIPCODES 
          GROUP BY state""") \
     .show()
