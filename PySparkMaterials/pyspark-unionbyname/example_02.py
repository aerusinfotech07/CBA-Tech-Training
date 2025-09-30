# Example 02 from: PySpark unionByName()

# Create DataFrames with different column names
df1 = spark.createDataFrame([[5, 2, 6]], ["col0", "col1", "col2"])
df2 = spark.createDataFrame([[6, 7, 3]], ["col1", "col2", "col3"])

# Using allowMissingColumns
df3 = df1.unionByName(df2, allowMissingColumns=True)
df3.printSchema
df3.show()
