# PySpark – explode nested array into rows

---

Problem: How to explode & flatten nested array (Array of Array)  DataFrame columns into rows using PySpark.

Advertisements

Solution: PySpark explode function can be used to explode an Array of Array (nested Array) ArrayType(ArrayType(StringType)) columns to rows on PySpark DataFrame using python example.

Before we start, let’s create a DataFrame with a nested array column. From below example column “subjects” is an array of ArraType which holds subjects learned.

```

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()

arrayArrayData = [
  ("James",[["Java","Scala","C++"],["Spark","Java"]]),
  ("Michael",[["Spark","Java","C++"],["Spark","Java"]]),
  ("Robert",[["CSharp","VB"],["Spark","Python"]])
]

df = spark.createDataFrame(data=arrayArrayData, schema = ['name','subjects'])
df.printSchema()
df.show(truncate=False)

```

df.printSchema() and df.show() returns the following schema and table.

```

root
 |-- name: string (nullable = true)
 |-- subjects: array (nullable = true)
 |    |-- element: array (containsNull = true)
 |    |    |-- element: string (containsNull = true)

+-------+-----------------------------------+
|name   |subjects                           |
+-------+-----------------------------------+
|James  |[[Java, Scala, C++], [Spark, Java]]|
|Michael|[[Spark, Java, C++], [Spark, Java]]|
|Robert |[[CSharp, VB], [Spark, Python]]    |
+-------+-----------------------------------+

```

Now, let’s explode “subjects” array column to array rows. after exploding, it creates a new column ‘col’ with rows represents an array.

```

from pyspark.sql.functions import explode
df.select(df.name,explode(df.subjects)).show(truncate=False)

```

Outputs:

```

+-------+------------------+
|name   |col               |
+-------+------------------+
|James  |[Java, Scala, C++]|
|James  |[Spark, Java]     |
|Michael|[Spark, Java, C++]|
|Michael|[Spark, Java]     |
|Robert |[CSharp, VB]      |
|Robert |[Spark, Python]   |
+-------+------------------+

```

If you want to flatten the arrays, use flatten function which converts array of array columns to a single array on DataFrame.

```

from pyspark.sql.functions import flatten
df.select(df.name,flatten(df.subjects)).show(truncate=False)

```

Outputs:

```

+-------+-------------------------------+
|name   |flatten(subjects)              |
+-------+-------------------------------+
|James  |[Java, Scala, C++, Spark, Java]|
|Michael|[Spark, Java, C++, Spark, Java]|
|Robert |[CSharp, VB, Spark, Python]    |
+-------+-------------------------------+

```

Happy Learning !!

## Related Article
- PySpark Explode Array and Map Columns to Rows
- PySpark ArrayType Column With Example
- PySpark Convert Dictionary/Map to Multiple Columns
- PySpark – Convert array column to a String
- PySpark Check Column Exists in DataFrame
- PySpark Select Nested struct Columns
- PySpark Get Number of Rows and Columns
- PySpark Find Maximum Row per Group in DataFrame

