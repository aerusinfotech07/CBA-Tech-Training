# Example 03 from: PySpark apply Function to Column

# Apply function using sql()
df.createOrReplaceTempView("TAB")
spark.sql("select Seqno, Name, UPPER(Name) from TAB") \
     .show()
