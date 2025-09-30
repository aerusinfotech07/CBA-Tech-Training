# PySpark DataFrame groupBy and Sort by Descending Order

---

PySpark DataFrame groupBy(), filter(), and sort() – In this PySpark example, let’s see how to do the following operations in sequence 1) DataFrame group by using aggregate function sum(), 2) filter() the group by result, and 3) sort() or orderBy() to do descending or ascending order.

Advertisements

In order to demonstrate all these operations together, let’s create a PySpark DataFrame.

```

simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NV",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","DE",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","NV",80000,25,18000),
    ("Kumar","Marketing","NJ",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)

```

## Using DataFrame groupBy(), filter() and sort()

Below is a complete PySpark DataFrame example of how to do group by, filter, and sort by descending order.

```

from pyspark.sql.functions import sum, col, desc
df.groupBy("state") \
  .agg(sum("salary").alias("sum_salary")) \
  .filter(col("sum_salary") > 100000)  \
  .sort(desc("sum_salary")) \
  .show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NY|    252000|
#|   CA|    171000|
#|   NV|    166000|
#+-----+----------+

```

Alternatively, you can use the following SQL expression to achieve the same result.

```

df.createOrReplaceTempView("EMP")
spark.sql("select state, sum(salary) as sum_salary from EMP " +
          "group by state having sum_salary > 100000 " + 
          "order by sum_salary desc").show()

```

#### Below is an Explanation of First DataFrame Example.

First, let’s do a PySpark groupBy() on Dataframe by using an aggregate function sum("salary") , groupBy() returns GroupedData object which contains aggregate functions like sum() , max() , min() , avg() , mean() , count() .

```

df.groupBy("state").sum("salary").show()
#+-----+-----------+
#|state|sum(salary)|
#+-----+-----------+
#|   NJ|      91000|
#|   NV|     166000|
#|   CA|     171000|
#|   DE|      99000|
#|   NY|     252000|
#+-----+-----------+

```

In the above example, you cannot give an alias name to the aggregate column and the column name would be defaults to agg function name and column name (sum("salary")) . This default name is not user friendly hence let’s see how to provide an alias by using agg() function. Also, to do filter and sort it’s better if you know the exact column name.

```

# Group by using by giving alias name.
from pyspark.sql.functions import sum
dfGroup=df.groupBy("department") \
          .agg(sum("bonus").alias("sum_salary"))

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|NJ   |91000     |
#|NV   |166000    |
#|CA   |171000    |
#|DE   |99000     |
#|NY   |252000    |
#+-----+----------+

```

Here, I have used the PySpark SQL function sum() that returns a Column type and uses alias() of this class. Now let’s see how to filter the group by data. The below example selects the data that has a total sum of a salary greater than 100,000.

```

# Filter after group by
dfFilter=dfGroup.filter(dfGroup.sum_salary > 100000)
dfFilter.show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NV|    166000|
#|   CA|    171000|
#|   NY|    252000|
#+-----+----------+

```

Now, let’s use DataFrame sort() transformation to sort on group by column, by default it does sort by ascending order.

```

# Sory by on group by column
from pyspark.sql.functions import asc
dfFilter.sort("sum_salary").show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NV|    166000|
#|   CA|    171000|
#|   NY|    252000|
#+-----+----------+

```

In order to descending order, use Spark SQL function desc() .

```

# Sort by descending order.
from pyspark.sql.functions import desc
dfFilter.sort(desc("sum_salary")).show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NY|    252000|
#|   CA|    171000|
#|   NV|    166000|
#+-----+----------+

```

## Conclusion

In this PySpark example I have explained how to do DataFrame groupby(), filter() and sort() by descending order. hope you like it.

Happy Learning !!

## Related Articles
- PySpark Groupby Count Distinct
- PySpark Groupby on Multiple Columns
- PySpark Groupby Agg (aggregate) – Explained
- PySpark GroupBy Count – Explained
- PySpark Groupby Explained with Example
- PySpark Column alias after groupBy() Example
- PySpark distinct vs dropDuplicates
- PySpark Get Number of Rows and Columns

