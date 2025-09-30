# PySpark parallelize() – Create RDD from a list data

---

PySpark parallelize() is a function in SparkContext and is used to create an RDD from a list collection. In this article, I will explain the usage of parallelize to create RDD and how to create an empty RDD with a PySpark example.

Advertisements

Before we start let me explain what is RDD, Resilient Distributed Datasets ( RDD ) is a fundamental data structure of PySpark, It is an immutable distributed collection of objects. Each dataset in RDD is divided into logical partitions, which may be computed on different nodes of the cluster.
- PySpark is parallelizing an existing collection in your driver program.

Below is an example of how to create an RDD using a parallelize method from Sparkcontext . sparkContext.parallelize([1,2,3,4,5,6,7,8,9,10]) creates an RDD with a list of Integers.

## Using sc.parallelize on PySpark Shell or REPL

PySpark shell provides SparkContext variable “sc”, use sc.parallelize() to create an RDD.

```

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10])

```

## Using PySpark sparkContext.parallelize() in application

Since PySpark 2.0, First, you need to create a SparkSession which internally creates a SparkContext for you.

```

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
sparkContext=spark.sparkContext

```

Now, use sparkContext.parallelize() to create rdd from a list or collection.

```

rdd=sparkContext.parallelize([1,2,3,4,5])
rddCollect = rdd.collect()
print("Number of Partitions: "+str(rdd.getNumPartitions()))
print("Action: First element: "+str(rdd.first()))
print(rddCollect)

```

By executing the above program you should see below output.

```

Number of Partitions: 4
Action: First element: 1
[1, 2, 3, 4, 5]

```

parallelize() function also has another signature which additionally takes integer argument to specifies the number of partitions. Partitions are basic units of parallelism in PySpark.

Remember, RDDs in PySpark are a collection of partitions.

## create empty RDD by usingsparkContext.parallelize

Some times we may need to create empty RDD and you can also use parallelize() in order to create it.

```

emptyRDD = sparkContext.emptyRDD()
emptyRDD2 = rdd=sparkContext.parallelize([])

print("is Empty RDD : "+str(emptyRDD2.isEmpty()))

```

The complete code can be downloaded from GitHub – PySpark Examples project

## Related Articles
- PySpark Create RDD with Examples
- PySpark Replace Column Values in DataFrame
- PySpark repartition() – Explained with Examples
- What is PySpark DataFrame?
- PySpark RDD Actions with examples
- PySpark RDD Transformations with examples
- Convert PySpark RDD to DataFrame
- PySpark Row using on DataFrame and RDD
- PySpark RDD Actions with examples

