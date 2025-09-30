# Example 05 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

# Create DataFrame in PySpark
data = [("James","Smith","USA","CA",200000),
    ("Michael","Rose","USA","NY",150000),
    ("Robert","Williams","USA","CA",120000),
    ("Maria","Jones","USA","NY",130000),
    ("Ramana","Madala","India","AP",40000),
    ("Chandra","Potte","India","AP",50000),
    ("Krishna","Murugan","India","TN",40000),
    ("Saravanan","Murugan","India","TN",40000),
  ]
columns = ["firstname","lastname","country","state","salary"]
df = spark_ai._spark.createDataFrame(data, schema=columns)
df.show()

# Output:
#+---------+--------+-------+-----+------+
#|firstname|lastname|country|state|salary|
#+---------+--------+-------+-----+------+
#|    James|   Smith|    USA|   CA|200000|
#|  Michael|    Rose|    USA|   NY|150000|
#|   Robert|Williams|    USA|   CA|120000|
#|    Maria|   Jones|    USA|   NY|130000|
#|   Ramana|  Madala|  India|   AP| 40000|
#|  Chandra|   Potte|  India|   AP| 50000|
#|  Krishna| Murugan|  India|   TN| 40000|
#|Saravanan| Murugan|  India|   TN| 40000|
#+---------+--------+-------+-----+------+
