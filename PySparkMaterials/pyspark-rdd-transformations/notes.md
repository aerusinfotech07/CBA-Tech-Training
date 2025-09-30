# PySpark RDD Transformations with examples

---

PySpark RDD Transformations are lazy evaluation and is used to transform/update from one RDD into another. When executed on RDD, it results in a single or multiple new RDD.

Advertisements

Since RDD are immutable in nature, transformations always create a new RDD without updating an existing one hence, a chain of RDD transformations creates an RDD lineage .

RDD Lineage is also known as the RDD operator graph or RDD dependency graph .

In this tutorial, you will learn lazy transformations, types of transformations, a complete list of transformation functions using wordcount example.
- What is a lazy transformation
- Transformation types Narrow transformation Wider transformation
- Transformation functions
- Transformation functions with word count examples

## RDD Transformations are Lazy

RDD Transformations are lazy operations meaning none of the transformations get executed until you call an action on PySpark RDD. Since RDD’s are immutable, any transformations on it result in a new RDD leaving the current one unchanged.

## RDD Transformation Types

There are two types of transformations.

### Narrow Transformation

Narrow transformations are the result of map() and filter() functions and these compute data that live on a single partition meaning there will not be any data movement between partitions to execute narrow transformations.

rdd narrow transformation

Functions such as map() , mapPartition() , flatMap() , filter() , union() are some examples of narrow transformation

### Wider Transformation

Wider transformations are the result of groupByKey() and reduceByKey() functions and these compute data that live on many partitions meaning there will be data movements between partitions to execute wider transformations. Since these shuffles the data, they also called shuffle transformations.

rdd wider transformation

Functions such as groupByKey() , aggregateByKey() , aggregate() , join() , repartition() are some examples of a wider transformations.

Note: When compared to Narrow transformations, wider transformations are expensive operations due to shuffling.

## PySpark RDD Transformation functions
METHODSMETHOD USAGE AND DESCRIPTIONcache()Caches the RDDfilter()Returns a new RDD after applying filter function on source dataset.flatMap()Returns flattern map meaning if you have a dataset with array, it converts each elements in a array as a row. In other words it return 0 or more items in output for each element in dataset.map()Applies transformation function on dataset and returns same number of elements in distributed dataset.mapPartitions()Similar to map, but executs transformation function on each partition, This gives better performance than map functionmapPartitionsWithIndex()Similar to map Partitions, but also provides func with an integer value representing the index of the partition.randomSplit()Splits the RDD by the weights specified in the argument. For example rdd.randomSplit(0.7,0.3)union()Comines elements from source dataset and the argument and returns combined dataset. This is similar to union function in Math set operations.sample()Returns the sample dataset.intersection()Returns the dataset which contains elements in both source dataset and an argumentdistinct()Returns the dataset by eliminating all duplicated elements.repartition()Return a dataset with number of partition specified in the argument. This operation reshuffles the RDD randamly, It could either return lesser or more partioned RDD based on the input supplied.coalesce()Similar to repartition by operates better when we want to the decrease the partitions. Betterment acheives by reshuffling the data from fewer nodes compared with all nodes by repartition.
## PySpark RDD Transformations with Examples

In this section, I will explain a few RDD Transformations with word count example in scala, before we start first, let’s create an RDD by reading a text file . The text file used here is available at the GitHub and, the scala example is available at GitHub project for reference.

```

# Create RDD
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.textFile("/apps/sparkbyexamples/src/pyspark-examples/data.txt")

```

```

# Print RDD
for element in rdd.collect():
    print(element)

```

printing RDD after collect results in.

### flatMap() Transformation

flatMap() transformation flattens the RDD after applying the function and returns a new RDD. In other words, The flatMap() transformation is similar to the map() transformation but with one key difference: it allows each input element to map to zero or more output elements.

```

# Using flatMap()
rdd2=rdd.flatMap(lambda x: x.split(" "))

```

Yields below output. In the above example, it splits the element by space and flattens the data.

```

# Output:
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

### map() Transformation

map() transformation is used the apply any complex operations by applying a function to each element.

In our word count example, we are adding a new column with value 1 for each word, the result of the RDD is PairRDDFunctions which contains key-value pairs, word of type String as Key and 1 of type Int as value.

```

# Using map()
rdd3=rdd2.map(lambda x: (x,1))

```

Collecting and Printing rdd3 yields below output.

pyspark rdd map transformation

### reduceByKey() Transformation

reduceByKey() merges the values for each key with the function specified. In our example, it reduces the word string by applying the sum function on value. The result of our RDD contains unique words and their count.

```

# reduceByKey()
rdd4=rdd3.reduceByKey(lambda a,b: a+b)

```

Collecting and Printing rdd4 yields below output.

### sortByKey() Transformation

sortByKey() transformation is used to sort RDD elements on key. In our example, first, we convert RDD[(String,Int]) to RDD[(Int,String]) using map transformation and later apply sortByKey which ideally does sort on an integer value. And finally, foreach with println statement prints all words in RDD and their count as key-value pair to console.

```

# sortByKey()
rdd5 = rdd4.map(lambda x: (x[1],x[0])).sortByKey()

```

Collecting and Printing rdd5 yields below output. Note the columns order has changed.

pyspark rdd sortbykey

### filter() Transformation

filter() transformation is used to filter the records in an RDD. In our example we are filtering all words starts with “a”.

```

# filter()
rdd6 = rdd5.filter(lambda x : 'a' in x[1])

```

This above statement yields “ (2, 'Wonderland') ” that has a value ‘a’.

## PySpark RDD Transformations complete example

```

package com.sparkbyexamples.spark.rdd

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.textFile("/apps/sparkbyexamples/src/pyspark-examples/data.txt")

for element in rdd.collect():
    print(element)

#Flatmap    
rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)
#map
rdd3=rdd2.map(lambda x: (x,1))
for element in rdd3.collect():
    print(element)
#reduceByKey
rdd4=rdd3.reduceByKey(lambda a,b: a+b)
for element in rdd4.collect():
    print(element)
#map
rdd5 = rdd4.map(lambda x: (x[1],x[0])).sortByKey()
for element in rdd5.collect():
    print(element)
#filter
rdd6 = rdd5.filter(lambda x : 'a' in x[1])
for element in rdd6.collect():
    print(element)

```

## Conclusion

In this PySpark RDD Transformations article, you have learned different transformation functions and their usage with Python examples and GitHub project for quick reference.

Reference: https://spark.apache.org/docs/latest/rdd-programming-guide.html

Happy Learning !!

## Related Articles
- PySpark RDD Actions with examples
- Pyspark – Get substring() from a column
- How to Install PySpark on Windows
- PySpark mapPartitions() Examples
- How to Install PySpark on Mac (in 2022)
- PySpark Shell Command Usage with Examples
- PySpark cache() Explained.
- PySpark createOrReplaceTempView() Explained
- PySpark RDD Actions with examples

