# Example 06 from: PySpark UDF (User Defined Function)

@udf(returnType=StringType()) 
def upperCase(str):
    return str.upper()

df.withColumn("Cureated Name", upperCase(col("Name"))) \
.show(truncate=False)
