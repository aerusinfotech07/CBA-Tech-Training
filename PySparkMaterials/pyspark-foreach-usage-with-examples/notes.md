# PySpark foreach() Usage with Examples

---

PySpark foreach() is an action operation that is available in RDD, DataFram to iterate/loop over each element in the DataFrmae, It is similar to for with advanced concepts. This is different than other actions as foreach() function doesn’t return a value instead it executes the input function on each element of an RDD, DataFrame

Advertisements

## 1. PySpark DataFrame foreach()

### 1.1 foreach() Syntax

Following is the syntax of the foreach() function

```

# Syntax
DataFrame.foreach(f)

```

### 1.2 PySpark foreach() Usage

When foreach() applied on PySpark DataFrame, it executes a function specified in for each element of DataFrame. This operation is mainly used if you wanted to manipulate accumulators , save the DataFrame results to RDBMS tables, Kafka topics, and other external sources.

In this example, to make it simple we just print the DataFrame to the console.

```

# Import
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com') \
                    .getOrCreate()

# Prepare Data
columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

# Create DataFrame
df = spark.createDataFrame(data=data,schema=columns)
df.show()

# foreach() Example
def f(df):
    print(df.Seqno)
df.foreach(f)

```

Using foreach() to update the accumulator shared variable.

```

# foreach() with accumulator Example
accum=spark.sparkContext.accumulator(0)
df.foreach(lambda x:accum.add(int(x.Seqno)))
print(accum.value) #Accessed by driver

```

## 2. PySpark RDD foreach() Usage

The foreach() on RDD behaves similarly to DataFrame equivalent, hence the same syntax and it is also used to manipulate accumulators from RDD , and write external data sources.

### 2.1Syntax

```

# Syntax
RDD.foreach(f: Callable[[T], None]) → None

```

### 2.2 RDD foreach() Example

```

# foreach() with RDD example
accum=spark.sparkContext.accumulator(0)
rdd=spark.sparkContext.parallelize([1,2,3,4,5])
rdd.foreach(lambda x:accum.add(x))
print(accum.value) #Accessed by driver

```

## Conclusion

In conclusion, PySpark foreach() is an action operation of RDD and DataFrame which doesn’t have any return type and is used to manipulate the accumulator and write any external data sources.

## Related Articles
- PySpark map() Transformation
- PySpark mapPartitions()
- PySpark Pandas UDF Example
- PySpark between() range of values
- PySpark max() – Different Methods Explained
- PySpark sum() Columns Example
- PySpark union two DataFrames
- PySpark Broadcast Variable
- PySpark Broadcast Join
- PySpark persist() Example
- PySpark lag() Function
- PySpark Random Sample with Example
- PySpark Apply Function to Column
- PySpark Apply udf to Multiple Columns

Happy Learning !!

