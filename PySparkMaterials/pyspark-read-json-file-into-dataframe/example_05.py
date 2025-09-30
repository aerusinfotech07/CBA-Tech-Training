# Example 05 from: PySpark Read JSON file into DataFrame

# Read all JSON files from a folder
df3 = spark.read.json("resources/*.json")
df3.show()
