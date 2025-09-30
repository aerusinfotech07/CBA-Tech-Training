# Pandas API on Spark | Explained With Examples

---

Pandas API on Apache Spark (PySpark) enables data scientists and data engineers to run their existing pandas code on Spark. Prior to this API, you had to do a significant code rewrite from pandas DataFrame to PySpark DataFrame which is time-consuming and error-prone. With this API, users don’t have to do this time-consuming process anymore to run their pandas programs on PySpark (Spark with Python).

Advertisements

## 1. What is Pandas?

Before we jump further into the discussion let’s understand what is Python pandas? You can jump into the next section if you already knew this. Python pandas is the most popular open-source library in the Python programming language, it runs on a single machine and is single-threaded. Pandas is a widely used and defacto framework for data science, data analysis, and machine learning applications. For detailed examples refer to the pandas Tutorial .

Pandas is built on top of another popular package named Numpy , which provides scientific computing in Python and supports multi-dimensional arrays.

## 2. What is Apache Spark & PySpark?

In very simple words Pandas run operations on a single machine so it doesn’t scale whereas Apache Spark runs on multiple machines so it is easy to scale. If you are working on a Machine Learning application where you are dealing with larger datasets, Spark with Python a.k.a PySpark is the best choice where you need to process operations many times(100x) faster than Pandas.

PySpark is a Spark library written in Python to run Python applications using Apache Spark capabilities. Using PySpark we can run applications parallelly on the distributed cluster (multiple nodes) or even on a single node. For more details refer to PySpark Tutorial with Examples . For Apache Spark architecture and its usage refer to Apache Spark Tutorial .

## 3. What is the Challenge of using PySpark?

If you don’t have prior knowledge on Pandas and your project not using it then there is no challenge, you can learn PySpark and start using PySpark DataFrame to run your bigger loads and even scale when required. However, if you already have prior knowledge of pandas or have been using pandas on your project and wanted to run bigger loads using Apache Spark architecture, you need to rewrite your code to use PySpark DataFrame (For Python programmers).

This is the biggest challenge for data scientists and data engineers as you need to learn a new framework and rewrite your code to this framework.

Using Pandas API on Apache Spark solves this problem. With this, you don’t have to rewrite your code instead using this API you can run Pandas DataFrame on Apache Spark by utilizing Spark capabilities.

## 4. History of Pandas API on Spark

Prior to Spark 3.2 release if you wanted to use pandas API on PySpark (Spark with Python) you have to use the Koalas project. Koalas is an open source project announced in Spark + AI Summit 2019 (Apr 24, 2019) that enables running pandas dataframe operations on PySpark. Fast forward now Koalas project is now part of Apache Spark and release in Spark 3.2 release.

## 5. Using Pandas API on PySpark (Spark with Python)

Using Pandas API on PySpark enables data scientists and data engineers who have prior knowledge of pandas more productive by running the pandas DataFrame API on PySpark by utilizing its capabilities and running pandas operations 10 x faster for big data sets.

pandas DataFrame is the de facto option for data scientists and data engineers whereas Apache Spark (PySpark) framework is the de facto to run large datasets.

By running pandas API on PySpark you will overcome the following challenges.
- Avoids learning a new framework
- More productive
- Maintain single codebase
- Time-consuming to rewrite & testing
- Confusion between pandas vs Spark API
- Finally Error prone

Note that pandas API on Spark is an added advantage to Spark as it makes many features that were hard to do in Spark actually makes it available through pandas, for example plotting data directly from a PySpark DataFrame.

## 6. Importing PySpark Pandas

If you are using PySpark version > 3.2 then, just import PySpark Pandas as below. You are not required to install anything.

```

# Import PySpark Pandas
import pyspark.pandas as ps

```

If you are using an older Spark version < 3.2, then you need to install Koalas open source project in order to use Pandas on PySpark. The new version of open source Koalas only supports Python version 3.6 or newer.

```

# Install koalas
pip install koalas

```

## 7. Create Pandas DataFrame

First, let’s create a pandas DataFrame and run some operations. Use import pandas as pd to import pandas.

```

# Import pandas
import pandas as pd

# Create pandas DataFrame
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)

```

Run pandas groupby operation.

```

# Use groupby() to compute the sum
df2 = df.groupby(['Courses']).sum()
print(df2)

```

Yields below output.

```

# Output
           Fee  Discount
Courses                 
Hadoop   48000    1000.0
NA        1500       0.0
Pandas   26000    2500.0
PySpark  25000    2300.0
Python   46000    2800.0
Spark    47000    2400.0

```

## 8. Run Pandas API DataFrame on PySpark (Spark with Python)

Use the above created pandas DataFrame and run it on PySpark. In order to do so, you need to use import pyspark.pandas as ps instead of import pandas as pd . And use ps.DataFrame() to create a DataFrame.

```

# Import pyspark.pandas
import pyspark.pandas as ps

# Create pandas DataFrame
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = ps.DataFrame(technologies)
print(df)

# Use groupby() to compute the sum
df2 = df.groupby(['Courses']).sum()
print(df2)

```

Note that here, df and df2 objects are not Spark DataFrame instead they are objects of pyspark.pandas.frame.DataFrame .  This DataFrame corresponds to pandas DataFrame logically and it holds Spark DataFrame internally. In other words, it is a wrapper class for Spark DataFrame to behave similarly to pandas DataFrame.

Run this program on an environment that has PySpark and you should get the same output as above. I have executed the above code in the pyspark shell , you can refer to the output below.

pandas api on spark
Running pandas on Apache Spark (PySpark)
If you try to run df.show() or df.printSchema() you will get errors.

Run pandas on pyspark

## 9. Convert DataFrame between Pandas, Spark & Pandas API on Spark

After completing all your operations running on Spark you might be required to convert the result to pandas DataFrame for further processing or to return to UI e.t.c, You can convert this pyspark.pandas.frame.DataFrame object to pandas.core.frame.DataFrame (Convert Pandas API on Spark to Pandas DataFrame) by using ps.to_pandas() .

```

# Convert Pandas API on Spark to Pandas DataFrame
pdf = df.to_pandas()
print(type(pdf))

# Output
#<class 'pandas.core.frame.DataFrame'>

```

Note that to_pandas() loads all data from multiple machines into the spark driver’s memory hence, it should only be used if the resulting pandas DataFrame is expected to be small and fits in pandas memory.

To convert pandas.core.frame.DataFrame to pyspark.pandas.frame.DataFrame (Convert Pandas DataFrame to Pandas API on Spark DataFrame) use ps.from_pandas() .

```

# Convert Pandas DataFrame to Pandas API on Spark DataFrame
psdf = ps.from_pandas(pdf)
print(type(psdf))

# Output
# <class 'pyspark.pandas.frame.DataFrame'>

```

We can also convert a Pandas API on Spark Dataframe into a Spark DataFrame by using to_spark() . It converts object from type pyspark.pandas.frame.DataFrame to pyspark.sql.dataframe.DataFrame .

```

# Pandas API on Spark Dataframe into a Spark DataFrame
sdf = df.to_spark()
print(type(sdf))
sdf.show()

# Output
#<class 'pyspark.sql.dataframe.DataFrame'>
#+-------+-----+--------+--------+
#|Courses|  Fee|Duration|Discount|
#+-------+-----+--------+--------+
#|  Spark|22000|  30days|  1000.0|
#|PySpark|25000|  50days|  2300.0|
#| Hadoop|23000|  55days|  1000.0|
#| Python|24000|  40days|  1200.0|
#| Pandas|26000|  60days|  2500.0|
#| Hadoop|25000|  35days|    null|
#|  Spark|25000|  30days|  1400.0|
#| Python|22000|  50days|  1600.0|
#|     NA| 1500|  40days|     0.0|
#+-------+-----+--------+--------+

```

Similarly, use pandas_api() to convert pyspark.sql.dataframe.DataFrame to pyspark.pandas.frame.DataFrame DataFrame.

```

# Convert a Spark Dataframe into a Pandas API on Spark Dataframe
psdf = sdf.pandas_api()
print(type(psdf))

# (or)
# to_pandas_on_spark() is depricated
psdf = sdf.to_pandas_on_spark()
print(type(psdf))

# Output
<class 'pyspark.pandas.frame.DataFrame'>

```

## 10. Compare Pandas API on Spark vs PySpark

In this section let’s see some operations using pandas API and compare that with PySpark.

In PySpark, first, you need to create a SparkSession in PySpark programming, by using builder() let’s create one. If you are using Azure Databricks, you don’t have to create a session object as the Databricks runtime environment by default provides you with the spark object similar to the PySpark shell .

```

spark = SparkSession.builder().master("local[1]")
          .appName("SparkByExamples.com")
          .getOrCreate()

```

### 10.1 Select Columns

Let’s select columns from both these approaches and see the difference in Syntax.

```

# Pandas API on Spark
df[["Courses","Fee"]]

# PySpark
sdf.select("Courses","Fee").show()

```

## 10.2 Select or Filter Rows

Similarly, select rows from the DataFrame. On both == operator is used to check if a value is matching.

```

# Pandas API on Spark
df2 = df.loc[ (df.Courses == "Python")]

# PySpark
sdf2 = sdf.filter(sdf.Courses == "Python")
sdf2.show()

```

### 10.2 Count

count() method is pretty much the same on both API’s. It basically returns the number of rows in a DataFrame.

```

# Pandas API on Spark
df.count()

# PySpark
sdf.count()

```

## 10.3 Sort Rows

Sort rows based on two columns.

```

# Pandas API on Spark
df2 = df.sort_values(["Courses", "Fee"])

# PySpark
sdf2 = sdf.sort("Courses", "Fee")
sdf2.show()

```

### 10.4 Rename Columns

Let’s see how to rename columns on pandas using this API vs pyspark rename columns with examples.

```

# Pandas API on Spark
df2 = df.rename(columns={'Fee': 'Courses_Fee'})

# PySpark
sdf2 = sdf.withColumnRenamed("Fee", "Courses_Fee")
sdf2.show()

```

## 10.5 Group By

Let’s do a group by on Courses and get the count for each group.

```

# Pandas API on Spark
df.groupby(['Courses']).count()

# PySpark
sdf.groupBy("Courses").count()

```

### 10.6 Access CSV File

Finally, let’s read a CSV file in both frameworks. For details examples on pandas refer to read CSV file in Pandas .

```

# Pandas API on Spark
pdf = ps.read_csv('/tmp/resources/courses.csv')

# PySpark
sdf = spark.read.csv("/tmp/resources/courses.csv")

```

## 11. Data Types of Pandas API on Spark vs PySpark

When converting pandas on Spark DataFrame from/to PySpark DataFrame, all data types will be automatically cast to the appropriate type.

Note that pandas API on Spark DataFrame and pandas DataFrame contains the same data types hence when you do the conversion you don’t see any differences in type. However, you need to keep a close eye when you convert from/to PySpark.

```

# Pandas API on Spark
print(df.dtypes)

# Output
#Courses      object
#Fee           int64
#Duration     object
#Discount    float64
#dtype: object

# PySpark
sdf.printSchema()

# Output
#root
# |-- Courses: string (nullable = false)
# |-- Courses_Fee: long (nullable = false)
# |-- Duration: string (nullable = false)
# |-- Discount: double (nullable = true)

```

## 12. Conclusion

In this article, you have learned what is pandas, Apache Spark, PySpark, and how to use pandas API on Spark and finally run pandas on Spark by utilizing its capabilities. pandas DataFrame is the de facto option for data scientists and data engineers whereas Apache Spark (PySpark) framework is the de facto to run large datasets. By running pandas API on PySpark you will overcome the following challenges.
- Avoids learning a new framework
- More productive
- Maintain single codebase
- Time-consuming to rewrite & testing
- Confusion between pandas vs Spark API
- Finally Error prone

Happy Learning !!

## Related Articles
- Pandas Get DataFrame Shape
- How to Count Duplicates in Pandas DataFrame
- How to Transpose() DataFrame in Pandas?
- How to Plot a Histogram Using Pandas?
- How to Add Title to Pandas Plot?
- Pandas Convert Column to Numpy Array
- Pandas DataFrame count() Function
- Pandas Filter DataFrame by Multiple Conditions
- How to Convert Pandas Uppercase Column

