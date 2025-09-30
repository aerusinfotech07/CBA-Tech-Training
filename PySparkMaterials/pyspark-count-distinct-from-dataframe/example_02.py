# Example 02 from: PySpark Count Distinct from DataFrame

from pyspark.sql.functions import countDistinct
df2=df.select(countDistinct("Dept", "Salary"))
df2.show()
