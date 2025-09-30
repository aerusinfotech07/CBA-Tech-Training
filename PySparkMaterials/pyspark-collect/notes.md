# PySpark Collect()  – Retrieve data from DataFrame

---

PySpark RDD/DataFrame collect() is an action operation that is used to retrieve all the elements of the dataset (from all nodes) to the driver node. We should use the collect() on smaller dataset usually after filter() , group() e.t.c. Retrieving larger datasets results in OutOfMemory error.

Advertisements

In this PySpark article, I will explain the usage of collect() with DataFrame example, when to avoid it, and the difference between collect() and select() .

Related Articles:
- How to Iterate PySpark DataFrame through Loop
- How to Convert PySpark DataFrame Column to Python List

In order to explain with an example, first, let’s create a DataFrame .

```

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.show(truncate=False)

```

show() function on DataFrame prints the result of DataFrame in a table format . By default, it shows only 20 rows. The above snippet returns the data in a table.

```

+---------+-------+
|dept_name|dept_id|
+---------+-------+
|Finance  |10     |
|Marketing|20     |
|Sales    |30     |
|IT       |40     |
+---------+-------+

```

Now, let’s use the collect() to retrieve the data.

```

dataCollect = deptDF.collect()
print(dataCollect)

```

deptDF.collect() retrieves all elements in a DataFrame as an Array of Row type to the driver node. printing a resultant array yields the below output.

```

[Row(dept_name='Finance', dept_id=10), 
Row(dept_name='Marketing', dept_id=20), 
Row(dept_name='Sales', dept_id=30), 
Row(dept_name='IT', dept_id=40)]

```

Note that collect() is an action hence it does not return a DataFrame instead, it returns data in an Array to the driver. Once the data is in an array, you can use python for loop to process it further.

```

for row in dataCollect:
    print(row['dept_name'] + "," +str(row['dept_id']))

```

If you wanted to get first row and first column from a DataFrame.

```

#Returns value of First Row, First Column which is "Finance"
deptDF.collect()[0][0]

```

Let’s understand what’s happening on above statement.
- deptDF.collect() returns Array of Row type.
- deptDF . collect()[0] returns the first element in an array (1st row).
- deptDF . collect[0][0] returns the value of the first row & first column.

In case you want to just return certain elements of a DataFrame, you should call PySpark select() transformation first.

```

dataCollect = deptDF.select("dept_name").collect()

```

## When to avoid Collect()

Usually, collect() is used to retrieve the action output when you have very small result set and calling collect() on an RDD/DataFrame with a bigger result set causes out of memory as it returns the entire dataset (from all workers) to the driver hence we should avoid calling collect() on a larger dataset.

## collect () vs select ()

select() is a transformation that returns a new DataFrame and holds the columns that are selected whereas collect() is an action that returns the entire data set in an Array to the driver.

## Complete Example of PySpark collect()

Below is complete PySpark example of using collect() on DataFrame, similarly you can also create a program using collect() with RDD.

```

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

dataCollect = deptDF.collect()

print(dataCollect)

dataCollect2 = deptDF.select("dept_name").collect()
print(dataCollect2)

for row in dataCollect:
    print(row['dept_name'] + "," +str(row['dept_id']))

```

This example is also available at PySpark Github project.

## Conclusion

In this PySpark article, you have learned the collect() function of the RDD/DataFrame is an action operation that returns all elements of the DataFrame to spark driver program and also learned it’s not a good practice to use it on the bigger dataset.

Happy Learning !!

## Related Articles
- PySpark distinct vs dropDuplicates
- Pyspark Select Distinct Rows
- PySpark cache() Explained.
- PySpark SparkContext Explained
- PySpark JSON Functions with Examples
- AttributeError: ‘DataFrame’ object has no attribute ‘map’ in PySpark
- PySpark Convert DataFrame to RDD
- PySpark – Loop/Iterate Through Rows in DataFrame
- Extract First and last N rows from PySpark DataFrame

