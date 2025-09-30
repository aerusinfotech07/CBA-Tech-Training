# Example 02 from: PySpark Save DataFrame to Hive Table

columns = ["id", "name","age","gender"]

# Create DataFrame 
data = [(1, "James",30,"M"), (2, "Ann",40,"F"),
    (3, "Jeff",41,"M"),(4, "Jennifer",20,"F")]
sampleDF = spark.sparkContext.parallelize(data).toDF(columns)

# Create Hive Internal table
sampleDF.write.mode('overwrite') \
         .saveAsTable("employee")

# Read Hive table
df = spark.read.table("employee")
df.show()
