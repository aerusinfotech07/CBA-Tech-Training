# Example 04 from: PySpark Create DataFrame with Examples

rowData = map(lambda x: Row(*x), data) 
dfFromData3 = spark.createDataFrame(rowData,columns)
