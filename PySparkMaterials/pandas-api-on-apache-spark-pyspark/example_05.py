# Example 05 from: Pandas API on Spark | Explained With Examples

# Convert Pandas DataFrame to Pandas API on Spark DataFrame
psdf = ps.from_pandas(pdf)
print(type(psdf))

# Output
# <class 'pyspark.pandas.frame.DataFrame'>
