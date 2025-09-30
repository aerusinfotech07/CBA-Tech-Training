# Example 01 from: PySpark Read JSON file into DataFrame

# Read JSON file into dataframe
df = spark.read.json("resources/zipcodes.json")
df.printSchema()
df.show()
