# Example 02 from: How to Install PySpark on Mac (in 2024)

# Create DataFrame in PySpark Shell
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
df = spark.createDataFrame(data)
df.show()
