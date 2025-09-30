# PySpark flatMap() Transformation

---

PySpark flatMap() is a transformation operation that flattens the RDD/DataFrame (array/map DataFrame columns) after applying the function on every element and returns a new PySpark RDD/DataFrame. In this article, you will learn the syntax and usage of the PySpark flatMap() with an example.

Advertisements

First, let’s create an RDD from the list.

```

data = ["Project Gutenberg’s",
        "Alice’s Adventures in Wonderland",
        "Project Gutenberg’s",
        "Adventures in Wonderland",
        "Project Gutenberg’s"]
rdd=spark.sparkContext.parallelize(data)
for element in rdd.collect():
    print(element)

```

This yields the below output

rdd output

## flatMap() Syntax

```

flatMap(f, preservesPartitioning=False)

```

## flatMap() Example

Now, let’s see with an example of how to apply a flatMap() transformation on RDD. In the below example, first, it splits each record by space in an RDD and finally flattens it. Resulting RDD consists of a single word on each record.

```

rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)

```

This yields below output.

```

Project
Gutenberg’s
Alice’s
Adventures
in
Wonderland
Project
Gutenberg’s
Adventures
in
Wonderland
Project
Gutenberg’s

```

## Complete PySpark flatMap() example

Below is the complete example of flatMap() function that works with RDD.

```

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = ["Project Gutenberg’s",
        "Alice’s Adventures in Wonderland",
        "Project Gutenberg’s",
        "Adventures in Wonderland",
        "Project Gutenberg’s"]
rdd=spark.sparkContext.parallelize(data)
for element in rdd.collect():
    print(element)

#Flatmap    
rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)

```

## Using flatMap() transformation on DataFrame

Unfortunately, PySpark DataFame doesn’t have flatMap() transformation however, DataFrame has explode() SQL function that is used to flatten the column . Below is a complete example.

```

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()

arrayData = [
        ('James',['Java','Scala'],{'hair':'black','eye':'brown'}),
        ('Michael',['Spark','Java',None],{'hair':'brown','eye':None}),
        ('Robert',['CSharp',''],{'hair':'red','eye':''}),
        ('Washington',None,None),
        ('Jefferson',['1','2'],{})]
df = spark.createDataFrame(data=arrayData, schema = ['name','knownLanguages','properties'])

from pyspark.sql.functions import explode
df2 = df.select(df.name,explode(df.knownLanguages))
df2.printSchema()
df2.show()

```

This example flattens the array column “ knownLanguages ” and yields below output

```

root
 |-- name: string (nullable = true)
 |-- col: string (nullable = true)

+---------+------+
|     name|   col|
+---------+------+
|    James|  Java|
|    James| Scala|
|  Michael| Spark|
|  Michael|  Java|
|  Michael|  null|
|   Robert|CSharp|
|   Robert|      |
|Jefferson|     1|
|Jefferson|     2|
+---------+------+

```

#### Conclusion

In conclusion, you have learned how to apply a PySpark flatMap() transformation to flattens the array or map columns and also learned how to use alternatives for DataFrame.

## Related Articles
- PySpark Convert DataFrame Columns to MapType (Dict)
- PySpark Convert Dictionary/Map to Multiple Columns
- How to Convert PySpark Column to List?
- PySpark map() Transformation
- Dynamic way of doing ETL through Pyspark
- PySpark RDD Transformations with examples
- PySpark distinct vs dropDuplicates
- Pyspark Select Distinct Rows

Happy Learning !!

