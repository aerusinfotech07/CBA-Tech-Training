# Example 04 from: PySpark where() & filter() for efficient data filtering

# Using array_contains()
from pyspark.sql.functions import array_contains
df.filter(array_contains(df.languages,"Java")) \
    .show(truncate=False)     

# Output
#+----------------+------------------+-----+------+
#|name            |languages         |state|gender|
#+----------------+------------------+-----+------+
#|[James, , Smith]|[Java, Scala, C++]|OH   |M     |
#|[Anna, Rose, ]  |[Spark, Java, C++]|NY   |F     |
#+----------------+------------------+-----+------+
