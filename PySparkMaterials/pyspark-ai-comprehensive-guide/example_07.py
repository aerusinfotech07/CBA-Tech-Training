# Example 07 from: PySpark AI (pyspark-ai) – English SDK Comprehensive Guide

# Rename columns using AI
df2 = df.ai.transform("rename column name from firstname to first_name and lastname to last_name")
df2.printSchema()
df2.show()
