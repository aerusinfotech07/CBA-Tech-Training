# Example 06 from: PySpark Read JSON file into DataFrame

# Define custom schema
schema = StructType([
      StructField("RecordNumber",IntegerType(),True),
      StructField("Zipcode",IntegerType(),True),
      StructField("ZipCodeType",StringType(),True),
      StructField("City",StringType(),True),
      StructField("State",StringType(),True),
      StructField("LocationType",StringType(),True),
      StructField("Lat",DoubleType(),True),
      StructField("Long",DoubleType(),True),
      StructField("Xaxis",IntegerType(),True),
      StructField("Yaxis",DoubleType(),True),
      StructField("Zaxis",DoubleType(),True),
      StructField("WorldRegion",StringType(),True),
      StructField("Country",StringType(),True),
      StructField("LocationText",StringType(),True),
      StructField("Location",StringType(),True),
      StructField("Decommisioned",BooleanType(),True),
      StructField("TaxReturnsFiled",StringType(),True),
      StructField("EstimatedPopulation",IntegerType(),True),
      StructField("TotalWages",IntegerType(),True),
      StructField("Notes",StringType(),True)
  ])

df_with_schema = spark.read.schema(schema) \
        .json("resources/zipcodes.json")
df_with_schema.printSchema()
df_with_schema.show()
