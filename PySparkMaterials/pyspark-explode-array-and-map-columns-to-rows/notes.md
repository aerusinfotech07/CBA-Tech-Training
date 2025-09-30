# PySpark Explode Array and Map Columns to Rows

---

In this article, I will explain how to explode an array or list and map columns to rows using different PySpark DataFrame functions explode() , explore_outer() , posexplode() , posexplode_outer() with Python example.

Advertisements

Before we start, let’s create a DataFrame with array and map fields. In the Below snippet, we create a DataFrame with columns “name” as StringType, “knownLanguage” as ArrayType, and “properties” as MapType.

```

# Create SparkSession and Prepare sample Data
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()

arrayData = [
        ('James',['Java','Scala'],{'hair':'black','eye':'brown'}),
        ('Michael',['Spark','Java',None],{'hair':'brown','eye':None}),
        ('Robert',['CSharp',''],{'hair':'red','eye':''}),
        ('Washington',None,None),
        ('Jefferson',['1','2'],{})

df = spark.createDataFrame(data=arrayData, schema = ['name','knownLanguages','properties'])
df.printSchema()
df.show()

```

```

# Output
root
 |-- name: string (nullable = true)
 |-- knownLanguages: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- properties: map (nullable = true)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)

+----------+--------------+--------------------+
|      name|knownLanguages|          properties|
+----------+--------------+--------------------+
|     James| [Java, Scala]|[eye -> brown, ha...|
|   Michael|[Spark, Java,]|[eye ->, hair -> ...|
|    Robert|    [CSharp, ]|[eye -> , hair ->...|
|Washington|          null|                null|
| Jefferson|        [1, 2]|                  []|
+----------+--------------+--------------------+

```

## 1. explode() – PySpark explode array or map column to rows

PySpark function explode(e: Column) is used to explode or create array or map columns to rows. When an array is passed to this function, it creates a new default column “col1” and it contains all array elements. When a map is passed, it creates two new columns one for key and one for value and each element in map split into the rows.

This will ignore elements that have null or empty. from the above example, Washington and Jefferson have null or empty values in array and map, hence the following snippet out does not contain these rows.

### 1.1explode – array column example

```

# explode() on array column
from pyspark.sql.functions import explode
df2 = df.select(df.name,explode(df.knownLanguages))
df2.printSchema()
df2.show()

```

```

# Output
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

### 1.2explode – map column example

```

# explode() on map column
from pyspark.sql.functions import explode
df3 = df.select(df.name,explode(df.properties))
df3.printSchema()
df3.show()

```

```

# Output
root
 |-- name: string (nullable = true)
 |-- key: string (nullable = false)
 |-- value: string (nullable = true)

+-------+----+-----+
|   name| key|value|
+-------+----+-----+
|  James| eye|brown|
|  James|hair|black|
|Michael| eye| null|
|Michael|hair|brown|
| Robert| eye|     |
| Robert|hair|  red|
+-------+----+-----+

```

## 2. explode_outer() – Create rows for each element in an array or map.

PySpark SQL explode_outer(e: Column) function is used to create a row for each element in the array or map column. Unlike explode, if the array or map is null or empty, explode_outer returns null.

```

# explode_outer() on array and map column
from pyspark.sql.functions import explode_outer
df.select(df.name,explode_outer(df.knownLanguages)).show()
df.select(df.name,explode_outer(df.properties)).show()

```

```

# DataFrame after explode_outer() on knownLanguages
+-----------+--------+
|name       |language|
+-----------+--------+
|James      |Java    |
|James      |Scala   |
|Michael    |Spark   |
|Michael    |Java    |
|Michael    |null    |
|Robert     |CSharp  |
|Robert     |        |
|Washington |null    |
|Jefferson  |1       |
|Jefferson  |2       |
+-----------+--------+

```

```

# DataFrame after explode_outer() on properties
+-----------+------------+--------------+
|name       |property_key|property_value|
+-----------+------------+--------------+
|James      |hair        |black         |
|James      |eye         |brown         |
|Michael    |hair        |brown         |
|Michael    |eye         |null          |
|Robert     |hair        |red           |
|Robert     |eye         |              |
|Washington |null        |null          |
|Jefferson  |            |              |
+-----------+------------+--------------+

```

## 3. posexplode() – explode array or map elements to rows

posexplode(e: Column) creates a row for each element in the array and creates two columns “pos’ to hold the position of the array element and the ‘col’ to hold the actual array value. And when the input column is a map, posexplode function creates 3 columns “pos” to hold the position of the map element, “key” and “value” columns.

This will ignore elements that have null or empty. Since the Washington and Jefferson have null or empty values in array and map, the following snippet out does not contain these.

```

# posexplode() on array and map
from pyspark.sql.functions import posexplode
df.select(df.name,posexplode(df.knownLanguages)).show()
df.select(df.name,posexplode(df.properties)).show()

```

```

# DataFrame after posexplode() on knownLanguages
+-----------+--------+--------+
|name       |position|language|
+-----------+--------+--------+
|James      |0       |Java    |
|James      |1       |Scala   |
|Michael    |0       |Spark   |
|Michael    |1       |Java    |
|Michael    |2       |null    |
|Robert     |0       |CSharp  |
|Robert     |1       |        |
|Jefferson  |0       |1       |
|Jefferson  |1       |2       |
+-----------+--------+--------+

```

```

# DataFrame after posexplode() on properties
+-----------+--------+------------+--------------+
|name       |position|property_key|property_value|
+-----------+--------+------------+--------------+
|James      |0       |hair        |black         |
|James      |1       |eye         |brown         |
|Michael    |0       |hair        |brown         |
|Michael    |1       |eye         |null          |
|Robert     |0       |hair        |red           |
|Robert     |1       |eye         |              |
|Washington |null    |null        |null          |
|Jefferson  |null    |null        |null          |
+-----------+--------+------------+--------------+

```

## 4. posexplode_outer() – explode array or map columns to rows.

Spark posexplode_outer(e: Column) creates a row for each element in the array and creates two columns “pos’ to hold the position of the array element and the ‘col’ to hold the actual array value. Unlike posexplode, if the array or map is null or empty, posexplode_outer function returns null, null for pos and col columns. Similarly for the map, it returns rows with nulls.

```

# posexplode_outer() on array and map 
from pyspark.sql.functions import posexplode_outer
df.select($"name",posexplode_outer($"knownLanguages")).show()
df.select(df.name,posexplode_outer(df.properties)).show()

```

```

# DataFrame after posexplode_outer() on knownLanguages
+-----------+--------+--------+
|name       |position|language|
+-----------+--------+--------+
|James      |0       |Java    |
|James      |1       |Scala   |
|Michael    |0       |Spark   |
|Michael    |1       |Java    |
|Michael    |2       |null    |
|Robert     |0       |CSharp  |
|Robert     |1       |        |
|Washington |null    |null    |
|Jefferson  |0       |1       |
|Jefferson  |1       |2       |
+-----------+--------+--------+

```

## Frequently Asked Questions on explode()

How does explode() handle null values? If the input column is null, the explode() function returns no rows for that particular record. If you want to handle null values gracefully, we should consider using explode_outer() . Can we use explode() on columns other than arrays or maps? explode() is specifically designed for columns containing arrays or maps. If you want to unnest other types of nested structures, we may need to use different functions or consider transforming the data to fit the array or map structure. How can I use explode() with multiple columns? You can use explode() on one column at a time. If you need to explode multiple columns simultaneously, you can chain multiple select() statements.

#### Conclusion

In this article, you have learned how to explode or convert array or map DataFrame columns to rows using explode and posexplode PySpark SQL functions and their’s respective outer functions and also learned differences between these functions using Python example.

## Related Articles
- PySpark Get Number of Rows and Columns
- PySpark Find Maximum Row per Group in DataFrame
- PySpark – explode nested array into rows
- PySpark MapType (Dict) Usage with Examples
- PySpark Convert Dictionary/Map to Multiple Columns
- PySpark ArrayType Column With Examples
- PySpark map() Transformation
- PySpark array_contains() function with examples.
- Explain PySpark element_at() with Examples
- Iterate over Elements of Array in PySpark DataFrame

