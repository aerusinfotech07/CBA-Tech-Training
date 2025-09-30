# Example 01 from: PySpark SQL expr() (Expression) Function

#Concatenate columns using || (sql like)
data=[("James","Bond"),("Scott","Varsa")] 
df=spark.createDataFrame(data).toDF("col1","col2") 
df.withColumn("Name",expr(" col1 ||','|| col2")).show()

+-----+-----+-----------+
| col1| col2|       Name|
+-----+-----+-----------+
|James| Bond| James,Bond|
|Scott|Varsa|Scott,Varsa|
+-----+-----+-----------+
