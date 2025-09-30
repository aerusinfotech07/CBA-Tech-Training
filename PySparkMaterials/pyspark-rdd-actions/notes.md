# PySpark RDD Actions with examples

---

RDD actions are PySpark operations that return the values to the driver program. Any function on RDD that returns other than RDD is considered as an action in PySpark programming. In this tutorial, I will explain the most used RDD actions with examples.

Advertisements

Action functions trigger the transformations to execute. As mentioned in RDD Transformations , all transformations are lazy evaluation meaning they do not get executed right away, and action trigger them to execute.

## PySpark RDD Actions Example

Before we start explaining RDD actions with examples, first, let’s create an RDD.

```

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data=[("Z", 1),("A", 20),("B", 30),("C", 40),("B", 30),("B", 60)]
inputRDD = spark.sparkContext.parallelize(data)
  
listRdd = spark.sparkContext.parallelize([1,2,3,4,5,3,2])

```

Note that we have created two RDDs in the above code snippet and we use these two as and when necessary to demonstrate the RDD actions.

### aggregate – action

Aggregate the elements of each partition, and then the results for all the partitions, using a given combine functions “combOp” and a neutral “zero value.”

The first function (seqOp) can return a different result type, U, than the type of this RDD. Thus, we need one operation for merging a T into an U and one operation for merging two U

syntax: aggregate ( zeroValue , seqOp , combOp )

Example 1

```

#aggregate
seqOp = (lambda x, y: x + y)
combOp = (lambda x, y: x + y)
agg=listRdd.aggregate(0, seqOp, combOp)
print(agg) # output 20

```

Example 2

```

#aggregate 2
seqOp2 = (lambda x, y: (x[0] + y, x[1] + 1))
combOp2 = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
agg2=listRdd.aggregate((0, 0), seqOp2, combOp2)
print(agg2) # output (20,7)

```

### treeAggregate – action

treeAggregate() – Aggregates the elements of this RDD in a multi-level tree pattern. The output of this function will be similar to the aggregate function.

Syntax: treeAggregate ( zeroValue , seqOp , combOp , depth=2 )

```

#treeAggregate. This is similar to aggregate
seqOp = (lambda x, y: x + y)
combOp = (lambda x, y: x + y)
agg=listRdd.treeAggregate(0, seqOp, combOp)
print(agg) # output 20

```

### fold – action

fold() – Aggregate the elements of each partition, and then the results for all the partitions.

```

#fold
from operator import add
foldRes=listRdd.fold(0, add)
print(foldRes)

```

### reduce

reduce() – Reduces the elements of the dataset using the specified binary operator.

```

#reduce
redRes=listRdd.reduce(add)
print(redRes) # output 20

```

### treeReduce

treeReduce() – Reduces the elements of this RDD in a multi-level tree pattern.

```

#treeReduce. This is similar to reduce
add = lambda x, y: x + y
redRes=listRdd.treeReduce(add)
print(redRes) # output 20

```

### collect

collect() -Return the complete dataset as an Array.

```

#Collect
data = listRdd.collect()
print(data)

```

### count, countApprox, countApproxDistinct

count() – Return the count of elements in the dataset.

countApprox() – Return approximate count of elements in the dataset, this method returns incomplete when execution time meets timeout.

countApproxDistinct() – Return an approximate number of distinct elements in the dataset.

```

#count, countApprox, countApproxDistinct
print("Count : "+str(listRdd.count()))
#Output: Count : 20
print("countApprox : "+str(listRdd.countApprox(1200)))
#Output: countApprox : (final: [7.000, 7.000])
print("countApproxDistinct : "+str(listRdd.countApproxDistinct()))
#Output: countApproxDistinct : 5
print("countApproxDistinct : "+str(inputRDD.countApproxDistinct()))
#Output: countApproxDistinct : 5

```

### countByValue

countByValue() – Return Map[T,Long] key representing each unique value in dataset and value represents count each value present.

```

#countByValue, countByValueApprox
print("countByValue :  "+str(listRdd.countByValue()))

```

### first

first() – Return the first element in the dataset.

```

#first
print("first :  "+str(listRdd.first()))
#Output: first :  1
print("first :  "+str(inputRDD.first()))
#Output: first :  (Z,1)

```

### top

top() – Return top n elements from the dataset.

Note: Use this method only when the resulting array is small, as all the data is loaded into the driver’s memory.

```

#top
print("top : "+str(listRdd.top(2)))
#Output: take : 5,4
print("top : "+str(inputRDD.top(2)))
#Output: take : (Z,1),(C,40)

```

### min

min() – Return the minimum value from the dataset.

```

#min
print("min :  "+str(listRdd.min()))
#Output: min :  1
print("min :  "+str(inputRDD.min()))
#Output: min :  (A,20)  

```

### max

max() – Return the maximum value from the dataset.

```

#max
print("max :  "+str(listRdd.max()))
#Output: max :  5
print("max :  "+str(inputRDD.max()))
#Output: max :  (Z,1)

```

### take, takeOrdered, takeSample

take() – Return the first num elements of the dataset.

takeOrdered() – Return the first num (smallest) elements from the dataset and this is the opposite of the take() action. Note: Use this method only when the resulting array is small, as all the data is loaded into the driver’s memory.

takeSample() – Return the subset of the dataset in an Array. Note: Use this method only when the resulting array is small, as all the data is loaded into the driver’s memory.

```

#take, takeOrdered, takeSample
print("take : "+str(listRdd.take(2)))
#Output: take : 1,2
print("takeOrdered : "+ str(listRdd.takeOrdered(2)))
#Output: takeOrdered : 1,2
print("take : "+str(listRdd.takeSample()))

```

## PySpark Actions – Complete example

```

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data=[("Z", 1),("A", 20),("B", 30),("C", 40),("B", 30),("B", 60)]
inputRDD = spark.sparkContext.parallelize(data)
  
listRdd = spark.sparkContext.parallelize([1,2,3,4,5,3,2])

#aggregate
seqOp = (lambda x, y: x + y)
combOp = (lambda x, y: x + y)
agg=listRdd.aggregate(0, seqOp, combOp)
print(agg) # output 20

#aggregate 2
seqOp2 = (lambda x, y: (x[0] + y, x[1] + 1))
combOp2 = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
agg2=listRdd.aggregate((0, 0), seqOp2, combOp2)
print(agg2) # output (20,7)

agg2=listRdd.treeAggregate(0,seqOp, combOp)
print(agg2) # output 20

#fold
from operator import add
foldRes=listRdd.fold(0, add)
print(foldRes) # output 20

#reduce
redRes=listRdd.reduce(add)
print(redRes) # output 20

#treeReduce. This is similar to reduce
add = lambda x, y: x + y
redRes=listRdd.treeReduce(add)
print(redRes) # output 20

#Collect
data = listRdd.collect()
print(data)

#count, countApprox, countApproxDistinct
print("Count : "+str(listRdd.count()))
#Output: Count : 20
print("countApprox : "+str(listRdd.countApprox(1200)))
#Output: countApprox : (final: [7.000, 7.000])
print("countApproxDistinct : "+str(listRdd.countApproxDistinct()))
#Output: countApproxDistinct : 5
print("countApproxDistinct : "+str(inputRDD.countApproxDistinct()))
#Output: countApproxDistinct : 5

#countByValue, countByValueApprox
print("countByValue :  "+str(listRdd.countByValue()))

#first
print("first :  "+str(listRdd.first()))
#Output: first :  1
print("first :  "+str(inputRDD.first()))
#Output: first :  (Z,1)

#top
print("top : "+str(listRdd.top(2)))
#Output: take : 5,4
print("top : "+str(inputRDD.top(2)))
#Output: take : (Z,1),(C,40)

#min
print("min :  "+str(listRdd.min()))
#Output: min :  1
print("min :  "+str(inputRDD.min()))
#Output: min :  (A,20)  

#max
print("max :  "+str(listRdd.max()))
#Output: max :  5
print("max :  "+str(inputRDD.max()))
#Output: max :  (Z,1)

#take, takeOrdered, takeSample
print("take : "+str(listRdd.take(2)))
#Output: take : 1,2
print("takeOrdered : "+ str(listRdd.takeOrdered(2)))
#Output: takeOrdered : 1,2
print("take : "+str(listRdd.takeSample()))

```

## Conclusion:

RDD actions are operations that return non-RDD values, since RDDs are lazy they do not execute the transformation functions until we call PySpark actions. hence, all these functions trigger the transformations to execute and finally return the value of the action functions to the driver program.

## Related Articles
- PySpark RDD Transformations with examples
- Convert PySpark RDD to DataFrame
- PySpark Create RDD with Examples
- PySpark Convert DataFrame to RDD
- PySpark Row using on DataFrame and RDD
- PySpark – Create an Empty DataFrame & RDD
- PySpark parallelize() – Create RDD from a list data

## References
- Spark RDD API Guide

