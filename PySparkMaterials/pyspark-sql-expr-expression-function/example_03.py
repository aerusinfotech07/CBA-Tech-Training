# Example 03 from: PySpark SQL expr() (Expression) Function

from pyspark.sql.functions import expr
data=[("2019-01-23",1),("2019-06-24",2),("2019-09-20",3)] 
df=spark.createDataFrame(data).toDF("date","increment") 

#Add Month value from another column
df.select(df.date,df.increment,
     expr("add_months(date,increment)")
  .alias("inc_date")).show()

+----------+---------+----------+
|      date|increment|  inc_date|
+----------+---------+----------+
|2019-01-23|        1|2019-02-23|
|2019-06-24|        2|2019-08-24|
|2019-09-20|        3|2019-12-20|
+----------+---------+----------+
