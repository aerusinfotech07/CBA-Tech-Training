# Example 02 from: PySpark Read JSON file into DataFrame

# Read JSON file into dataframe
df = spark.read.format('org.apache.spark.sql.json') \
        .load("resources/zipcodes.json")
