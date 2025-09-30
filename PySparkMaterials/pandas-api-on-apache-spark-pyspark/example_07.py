# Example 07 from: Pandas API on Spark | Explained With Examples

# Convert a Spark Dataframe into a Pandas API on Spark Dataframe
psdf = sdf.pandas_api()
print(type(psdf))

# (or)
# to_pandas_on_spark() is depricated
psdf = sdf.to_pandas_on_spark()
print(type(psdf))

# Output
<class 'pyspark.pandas.frame.DataFrame'>
