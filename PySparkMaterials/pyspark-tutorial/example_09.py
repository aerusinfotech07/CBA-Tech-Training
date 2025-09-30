# Example 09 from: PySpark 4.0 Tutorial For Beginners with Examples

# Rename columns using AI
df2 = df.ai.transform("rename column name from firstname to first_name and lastname to last_name")
df2.printSchema()
df2.show()
