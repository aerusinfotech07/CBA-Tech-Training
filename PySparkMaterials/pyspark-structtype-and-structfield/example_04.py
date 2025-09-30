# Example 04 from: PySpark StructType & StructField Explained with Examples

# Loading json schema to create DataFrame
import json
schemaFromJson = StructType.fromJson(json.loads(schema.json))
df3 = spark.createDataFrame(
        spark.sparkContext.parallelize(structureData),schemaFromJson)
df3.printSchema()
