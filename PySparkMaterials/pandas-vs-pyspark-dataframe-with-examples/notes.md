# Pandas vs PySpark DataFrame With Examples

---

What are the differences between Pandas and PySpark DataFrame? Pandas and PySpark are both powerful tools for data manipulation and analysis in Python. Pandas is a widely-used library for working with smaller datasets in memory on a single machine, offering a rich set of functions for data manipulation and analysis. In contrast, PySpark, built on top of Apache Spark, is designed for distributed computing, allowing for the processing of massive datasets across multiple machines in a cluster.

Advertisements

## What is Pandas?

Pandas is one of the most used open-source Python libraries to work with Structured tabular data for analysis. Pandas library is heavily used for Data Analytics, Machine learning,  data science projects, and many more.

Pandas can load the data by reading CSV, JSON, SQL, many other formats and creates a DataFrame which is a structured object containing rows and columns (similar to SQL table).

It doesn’t support distributed processing; hence, you would always need to increase the resources when you need additional horsepower to support your growing data.

Pandas DataFrames are mutable and are not lazy, statistical functions are applied on each column by default. You can learn more on pandas at pandas DataFrame Tutorial For Beginners Guide .

## Pandas DataFrameExample

In order to use the Pandas library in Python, you need to import it using the following.

```

# Import
import pandas as pd

```

The below example creates a Pandas DataFrame from the list.

```

import pandas as pd    
data = [["James","","Smith",30,"M",60000], 
        ["Michael","Rose","",50,"M",70000], 
        ["Robert","","Williams",42,"",400000], 
        ["Maria","Anne","Jones",38,"F",500000], 
        ["Jen","Mary","Brown",45,None,0]] 
columns=['First Name','Middle Name','Last Name','Age','Gender','Salary']

# Create the pandas DataFrame 
pandasDF=pd.DataFrame(data=data, columns=columns) 
  
# print dataframe. 
print(pandasDF)

```

Outputs below data on the console. Note that Pandas add an index sequence number to every data frame.

Pandas vs PySpark DataFrame

## Pandas Transformations

Below are some transformations you can perform on Pandas DataFrame. Note that statistical functions calculate at each column by default. you don’t have to explicitly specify on what column you wanted to apply the statistical functions. Even count() function returns count of each column (by ignoring null/None values).
- df.count() – Returns the count of each column (the count includes only non-null values).
- df.corr() – Returns the correlation between columns in a data frame.
- df.head(n) – Returns first n rows from the top.
- df.max() – Returns the maximum of each column.
- df.mean() – Returns the mean of each column.
- df.median() – Returns the median of each column.
- df.min() – Returns the minimum value in each column.
- df.std() – Returns the standard deviation of each column
- df.tail(n) – Returns last n rows.

```

# Output:
print(pandasDF.count())
First Name     5
Middle Name    5
Last Name      5
Age            5
Gender         4
Salary         5

print(pandasDF.max())
First Name       Robert
Middle Name        Rose
Last Name      Williams
Age                  50
Salary           500000

print(pandasDF.mean())
Age           41.0
Salary    206000.0

```

## What is PySpark?

PySpark is a Python API for Apache Spark, a distributed computing framework designed for processing large-scale datasets across clusters of machines. PySpark enables parallelized data processing and analysis by distributing computations across multiple nodes in a cluster, providing scalability and high performance for big data analytics tasks. It offers a DataFrame API that resembles Pandas, allowing users to perform similar data manipulation operations but on distributed datasets.

Difference Between Pandas vs PySpark
source:https://databricks.com/
In comparison, PySpark is designed for handling large-scale datasets that exceed the memory capacity of a single machine, making it suitable for big data analytics tasks that require distributed computing capabilities. While both PySpark and Pandas offer similar DataFrame APIs and data manipulation functionalities, PySpark’s distributed architecture provides scalability and parallelism for processing massive datasets across distributed clusters. Ultimately, the choice between PySpark and Pandas depends on the scale of the datasets and the computational resources available for data analysis tasks.

## PySpark DataFrame Example

PySpark DataFrame is immutable (cannot be changed once created), fault-tolerant and Transformations are Lazy evaluation (they are not executed until actions are called). PySpark DataFrames are distributed in the cluster (meaning the data in PySpark DataFrames are stored in different machines in a cluster) and any operations in PySpark execute in parallel on all machines.

```

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
               .appName('SparkByExamples.com') \
               .getOrCreate()

data = [("James","","Smith",30,"M",60000),
        ("Michael","Rose","",50,"M",70000),
        ("Robert","","Williams",42,"",400000),
        ("Maria","Anne","Jones",38,"F",500000),
        ("Jen","Mary","Brown",45,"F",0)]

columns = ["first_name","middle_name","last_name","Age","gender","salary"]
pysparkDF = spark.createDataFrame(data = data, schema = columns)
pysparkDF.printSchema()
pysparkDF.show(truncate=False)

```

Outputs Below Schema & DataFrame.

pandas vs pyspark dataframe

Reading a CSV file.

```

# Read a CSV file
df = spark.read.csv("/tmp/resources/zipcodes.csv")

```

## PySpark Transformations

PySpark transformations are Lazy in nature, meaning they do not execute until actions are called. The following are some of the transformations.
- select() – Choose specific columns from a DataFrame.
- filter() – Filter rows based on a condition.
- groupBy() – Group rows based on one or more columns.
- agg() – Perform aggregate functions (e.g., sum, average) on grouped data.
- orderBy() – Sort rows based on one or more columns.
- dropDuplicates() – Remove duplicate rows from the DataFrame.
- withColumn() – Add a new column or replace an existing column with modified data.
- drop() – Remove one or more columns from the DataFrame.
- join() – Merge two DataFrames based on a common column or index.
- pivot() – Pivot the DataFrame to reorganize data based on column values.

Below is an example

```

# PySpark transformations
from pyspark.sql.functions import mean, col, max
# Example 1
df2=pysparkDF.select(mean("age"),mean("salary"))
             .show()

# Example 2
pysparkDF.groupBy("gender") \
         .agg(mean("age"),mean("salary"),max("salary")) \
         .show()

```

## PySpark SQL Compatible

PySpark supports SQL queries to run transformations. All you need to do is create a Table/View from the PySpark DataFrame.

```

# PySpark SQL
pysparkDF.createOrReplaceTempView("Employee")
spark.sql("select * from Employee where salary > 100000").show()

# Prints result
#+----------+-----------+---------+---+------+------+
#|first_name|middle_name|last_name|Age|gender|salary|
#+----------+-----------+---------+---+------+------+
#|    Robert|           | Williams| 42|      |400000|
#|     Maria|       Anne|    Jones| 38|     F|500000|
#+----------+-----------+---------+---+------+------+

spark.sql("select mean(age),mean(salary) from Employee").show()

# Prints result
#+---------+------------+
#|mean(age)|mean(salary)|
#+---------+------------+
#|     41.0|    206000.0|
#+---------+------------+

```

## Create PySpark DataFrame from Pandas

Due to parallel execution on all cores on multiple machines, PySpark runs operations faster than Pandas, hence we often required to covert Pandas DataFrame to PySpark (Spark with Python) for better performance. This is one of the major differences between Pandas vs PySpark DataFrame.

```

# Create PySpark DataFrame from Pandas
pysparkDF2 = spark.createDataFrame(pandasDF) 
pysparkDF2.printSchema()
pysparkDF2.show()

```

## Create Pandas from PySpark DataFrame

Once the transformations are done on Spark, you can easily convert it back to Pandas using toPandas() method.

Note: toPandas() method is an action that collects the data into Spark Driver memory so you have to be very careful while dealing with large datasets. You will get OutOfMemoryException if the collected data doesn’t fit in Spark Driver memory.

```

# Convert PySpark to Pandas
pandasDF = pysparkDF.toPandas()
print(pandasDF)

```

## How to Decide Between Pandas vs PySpark

Deciding between Pandas and PySpark depends on several factors, including the scale of the data, available computational resources, and specific requirements of the data analysis tasks. Here are some considerations to help you decide:
1. Data Scale : Use Pandas for small to medium-sized datasets that fit into memory and require rapid in-memory data manipulation and analysis. Choose PySpark for large-scale datasets that exceed the memory capacity of a single machine and require distributed computing capabilities for parallelized data processing.
1. Computational Resources : If you have limited computational resources or a single machine environment, Pandas may be more suitable due to its in-memory processing capabilities. For distributed computing environments with access to clusters of machines, PySpark offers scalability and parallelism for processing massive datasets across distributed clusters.
1. Performance : Pandas performs well for small to medium-sized datasets but may struggle with large-scale datasets due to memory constraints. PySpark excels in processing large-scale datasets across distributed clusters, offering scalability and parallelism for improved performance.
1. Ecosystem and Integration : Pandas has a mature ecosystem with extensive support for data manipulation, visualization, and analysis tools, making it suitable for a wide range of data analysis tasks. PySpark integrates with the broader Apache Spark ecosystem, offering support for various data sources, machine learning libraries, and streaming processing capabilities.

## Conclusion

In conclusion, both PySpark and Pandas are powerful tools for data manipulation and analysis in Python, each with its own strengths and use cases.

Pandas excels in scenarios where datasets fit into memory on a single machine, offering a rich and intuitive API for rapid in-memory data manipulation and analysis. It is well-suited for interactive data exploration and small to medium-sized data analysis tasks, providing a familiar interface for Python users.

PySpark , on the other hand, is designed for handling large-scale datasets that exceed the memory capacity of a single machine. It offers distributed computing capabilities, allowing parallelized data processing across clusters of machines. PySpark’s scalability and performance make it ideal for big data analytics tasks that require processing massive datasets across distributed environments.

Ultimately, the choice between PySpark and Pandas depends on the scale of the data, available computational resources, and specific requirements of the data analysis tasks. While Pandas is more suitable for small to medium-sized datasets with in-memory processing needs, PySpark is the preferred choice for handling large-scale datasets and distributed computing environments. Understanding the strengths and limitations of each tool is essential for selecting the appropriate solution to meet the demands of the data analysis project.

Happy Learning !!

## Related Articles
- How to Convert Pandas to PySpark DataFrame
- Pandas Groupby Transform
- Pandas apply map (applymap()) Explained
- Find Intersection Between Two Series in Pandas?
- Get First N Rows of Pandas DataFrame
- What is PySpark and who uses it?
- Differences between Pandas Join vs Merge

