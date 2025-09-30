# Example 05 from: PySpark SQL expr() (Expression) Function

#Use expr()  to filter the rows
from pyspark.sql.functions import expr
data=[(100,2),(200,3000),(500,500)] 
df=spark.createDataFrame(data).toDF("col1","col2") 
df.filter(expr("col1 == col2")).show()

+----+----+
|col1|col2|
+----+----+
| 500| 500|
+----+----+
