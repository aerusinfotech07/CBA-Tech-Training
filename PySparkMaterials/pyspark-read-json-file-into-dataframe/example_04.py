# Example 04 from: PySpark Read JSON file into DataFrame

# Read multiple files
df2 = spark.read.json(
    ['resources/zipcode1.json','resources/zipcode2.json'])
df2.show()
