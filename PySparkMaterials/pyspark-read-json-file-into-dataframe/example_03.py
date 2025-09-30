# Example 03 from: PySpark Read JSON file into DataFrame

# Read multiline json file
multiline_df = spark.read.option("multiline","true") \
      .json("resources/multiline-zipcode.json")
multiline_df.show()
