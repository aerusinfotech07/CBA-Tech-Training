# Example 01 from: PySpark to_date() – Convert Timestamp to Date

df=spark.createDataFrame(
        data = [ ("1","2019-06-24 12:01:19.000")],
        schema=["id","input_timestamp"])
df.printSchema()

#Displays
root
 |-- id: string (nullable = true)
 |-- input_timestamp: string (nullable = true)
