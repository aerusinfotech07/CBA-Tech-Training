# Example 08 from: PySpark 4.0 Tutorial For Beginners with Examples

# Using groupby
groupDF = spark.sql("SELECT gender, count(*) from PERSON_DATA group by gender")
groupDF.show()
