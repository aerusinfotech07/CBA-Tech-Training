# Example 02 from: PySpark When Otherwise | SQL Case When Usage

from pyspark.sql.functions import when
df2 = df.withColumn("new_gender", when(df.gender == "M","Male")
                                 .when(df.gender == "F","Female")
                                 .when(df.gender.isNull() ,"")
                                 .otherwise(df.gender))
df2.show()
+-------+------+------+----------+
|   name|gender|salary|new_gender|
+-------+------+------+----------+
|  James|     M| 60000|      Male|
|Michael|     M| 70000|      Male|
| Robert|  null|400000|          |
|  Maria|     F|500000|    Female|
|    Jen|      |  null|          |
+-------+------+------+----------+
