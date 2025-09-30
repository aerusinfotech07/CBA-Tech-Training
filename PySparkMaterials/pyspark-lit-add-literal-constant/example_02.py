# Example 02 from: PySpark lit() – Add Literal or Constant to DataFrame

# Usage of lit() 
from pyspark.sql.functions import col,lit
df2 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
df2.show(truncate=False)
