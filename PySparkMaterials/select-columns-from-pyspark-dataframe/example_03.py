# Example 03 from: PySpark Select Columns From DataFrame

# Select All columns from List
df.select(*columns).show()

# Select All columns
df.select([col for col in df.columns]).show()
df.select("*").show()
