# PySpark show() – Display DataFrame Contents in Table

---

PySpark DataFrame show() is used to display the contents of the DataFrame in a Table Row and Column Format. By default, it shows only 20 Rows, and the column values are truncated at 20 characters.

Advertisements

## 1. Quick Example of show()

Following are quick examples of how to show the contents of DataFrame.

```

# Default - displays 20 rows and 
# 20 charactes from column value 
df.show()

#Display full column contents
df.show(truncate=False)

# Display 2 rows and full column contents
df.show(2,truncate=False) 

# Display 2 rows & column values 25 characters
df.show(2,truncate=25) 

# Display DataFrame rows & columns vertically
df.show(n=3,truncate=25,vertical=True)

```

## 2. show() Syntax

Following is the syntax of the show() function.

```

# Syntax
def show(self, n=20, truncate=True, vertical=False):

```

## 3. PySpark show() To Display Contents

Use PySpark show() method to display the contents of the DataFrame and use pyspark printSchema() method to print the schema . show() method by default shows only 20 rows/records from the DataFrame and truncates the column values at 20 characters.

```

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
columns = ["Seqno","Quote"]
data = [("1", "Be the change that you wish to see in the world"),
    ("2", "Everyone thinks of changing the world, but no one thinks of changing himself."),
    ("3", "The purpose of our lives is to be happy."),
    ("4", "Be cool.")]
df = spark.createDataFrame(data,columns)
df.show()

# Output
#+-----+--------------------+
#|Seqno|               Quote|
#+-----+--------------------+
#|    1|Be the change tha...|
#|    2|Everyone thinks o...|
#|    3|The purpose of ou...|
#|    4|            Be cool.|
#+-----+--------------------+

```

As you see above, values in the Quote column are truncated at 20 characters, Let’s see how to display the full column contents.

```

#Display full column contents
df.show(truncate=False)

#+-----+-----------------------------------------------------------------------------+
#|Seqno|Quote                                                                        |
#+-----+-----------------------------------------------------------------------------+
#|1    |Be the change that you wish to see in the world                              |
#|2    |Everyone thinks of changing the world, but no one thinks of changing himself.|
#|3    |The purpose of our lives is to be happy.                                     |
#|4    |Be cool.                                                                     |
#+-----+-----------------------------------------------------------------------------+

```

By default show() method displays only 20 rows from PySpark DataFrame. The below example limits the rows to 2 and full column contents. Our DataFrame has just 4 rows hence I can’t demonstrate with more than 4 rows. If you have a DataFrame with thousands of rows try changing the value from 2 to 100 to display more than 20 rows.

```

# Display 2 rows and full column contents
df.show(2,truncate=False) 

#+-----+-----------------------------------------------------------------------------+
#|Seqno|Quote                                                                        |
#+-----+-----------------------------------------------------------------------------+
#|1    |Be the change that you wish to see in the world                              |
#|2    |Everyone thinks of changing the world, but no one thinks of changing himself.|
#+-----+-----------------------------------------------------------------------------+

```

## 4. Show() with Truncate Column Values

You can also truncate the column value at the desired length. By default it truncates after 20 characters however, you can display all contents by using truncate=False. If you wanted to truncate at a specific length use truncate=n.

```

# Display 2 rows & column values 25 characters
df.show(2,truncate=25) 

#+-----+-------------------------+
#|Seqno|                    Quote|
#+-----+-------------------------+
#|    1|Be the change that you...|
#|    2|Everyone thinks of cha...|
#+-----+-------------------------+
#only showing top 2 rows

```

## 5. Display Contents Vertically

Finally, let’s see how to display the DataFrame vertically record by record.

```

# Display DataFrame rows & columns vertically
df.show(n=3,truncate=25,vertical=True)

#-RECORD 0--------------------------
# Seqno | 1                         
# Quote | Be the change that you... 
#-RECORD 1--------------------------
# Seqno | 2                         
# Quote | Everyone thinks of cha... 
#-RECORD 2--------------------------
# Seqno | 3                         
# Quote | The purpose of our liv... 

```

Happy Learning !!

6. Conclusion

In this article, you have learned how to show the PySpark DataFrame contents to the console and learned to use the parameters to limit the rows and truncate or display the contents of columns.

## Related Articles
- PySpark Select First Row of Each Group?
- PySpark Select Nested struct Columns
- PySpark Select Columns From DataFrame
- Dynamic way of doing ETL through Pyspark
- Pyspark Select Distinct Rows
- PySpark Get Number of Rows and Columns
- PySpark count() – Different Methods Explained
- PySpark SQL Self Join With Example

