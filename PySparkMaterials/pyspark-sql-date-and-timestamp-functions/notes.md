# PySpark SQL Date and Timestamp Functions

---

PySpark Date and Timestamp Functions are supported on DataFrame and SQL queries and they work similarly to traditional SQL, Date and Time are very important if you are using PySpark for ETL. Most of all these functions accept input as, Date type, Timestamp type, or String. If a String used, it should be in a default format that can be cast to date.

Advertisements
- DateType default format is yyyy-MM-dd
- TimestampType default format is yyyy-MM-dd HH:mm:ss.SSSS
- Returns null if the input is a string that can not be cast to Date or Timestamp.

PySpark SQL provides several Date & Timestamp functions hence keep an eye on and understand these. Always you should choose these functions instead of writing your own functions (UDF) as these functions are compile-time safe, handles null, and perform better when compared to PySpark UDF . If your PySpark application is critical on performance try to avoid using custom UDF at all costs as these are not guarantee performance.

For readable purposes, I’ve grouped these functions into the following groups.
- Date Functions
- Timestamp Functions
- Date and Timestamp Window Functions

Before you use any examples below, make sure you Create PySpark Sparksession and import SQL functions.

```

from pyspark.sql.functions import *

```

## PySpark SQL Date Functions

Below are some of the PySpark SQL Date functions, these functions operate on the just Date.

The default format of the PySpark Date is yyyy-MM-dd .
PYSPARK DATE FUNCTIONDATE FUNCTION DESCRIPTIONcurrent_date()Returns the current date as a`DateType`object. This function does not take any arguments and simply returns the current date based on the system clock where the PySpark application is running.date_format()It is used to format a date or timestamp column in a DataFrame to a specified date or time format pattern.to_date()It converts a string column representing a date or timestamp into a date type column in a DataFrameadd_months()It is used to add or subtract a specified number of months to a date or timestamp column in a DataFrame. It takes two arguments: the column representing the date or timestamp, and the number of months to add or subtract.date_add(column, days)date_sub(column, days)date_add() is used to add a specified number of days to a date columndate_sub() is used to subtract a specified number of days from a date columndatediff(end, start)It is used to calculate the difference in days between two date columns in a DataFrame. It takes two arguments: the two date columns to calculate the difference between.months_between(end, start)It is used to calculate the difference in months between two date or timestamp columns in a DataFrame. It takes two arguments: the two date or timestamp columns to calculate the difference between them.If both inputs share the same day of the month or are both the last day of their respective months, a whole number is returned. Otherwise, the difference is computed under the assumption of 31 days per month.months_between(end, start, roundOff)The result is rounded off to 8 digits when `roundOff` is set to true, it is not rounded otherwise.next_day(column, dayOfWeek)It is used to find the first occurrence of a specified day of the week that comes after a given date. It takes two arguments, the date column representing the reference date, and the day of the week specified as a string (e.g., ‘Monday’, ‘Tuesday’, etc.).trunc(column, format)Truncate a date or timestamp column in a DataFrame to a specified level of granularity. For example,`trunc(df['date_column'], 'month')`would truncate the dates in the “date_column” of DataFrame “df” to the first day of the month, effectively removing the day component and retaining only the month and year.date_trunc(format, timestamp)Truncate a timestamp column in a DataFrame to a specified level of granularity, while preserving the timestamp type. It takes two arguments: the column representing the timestamp to be truncated, and the level of granularity to which the timestamp should be truncated.year(column)Returns the year from a given date or timestamp.quarter(column)Returns the quarter as an integer from a given date or timestamp.month(column)Returns the month as an integer from a given date or timestampdayofweek(column)Extract the day of the week from a date or timestamp column in a DataFrame. Monday is represented by 1, Tuesday by 2, and so on until Sunday, which is represented by 7.dayofmonth(column)Extracts the day of the month from a given date or timestamp.dayofyear(column)Extracts the day of the year from a given date or timestamp.weekofyear(column)Extract the week number from a date or timestamp column in a DataFrame.last_day(column)Return the last day of the month for a given date or timestamp column.The result is a date column where each date corresponds to the last day of the month for the original dates in the specified column.from_unixtime(column)Convert a Unix timestamp (represented as the number of seconds since the Unix epoch) to a timestamp columnunix_timestamp()It is used to convert a string representing a date or timestamp to a Unix timestamp (i.e., the number of seconds since the Unix epoch). It takes two arguments: the column containing the string representation of the date or timestamp, and the format string specifying the format of the input string.
## PySpark SQL Timestamp Functions

Below are some of the PySpark SQL Timestamp functions, these functions operate on both date and timestamp values.

The default format of the Spark Timestamp is yyyy-MM-dd HH:mm:ss.SSSS
PYSPARK TIMESTAMP FUNCTION SIGNATURETIMESTAMP FUNCTION DESCRIPTIONcurrent_timestamp()It is used to retrieve the current timestamp at the time of execution within the PySpark application. It does not require any arguments. When called, it returns the current timestamp with timezone information as a timestamp type.hour(column)Return the hours from a timestamp columnminute(column)Return the hours from a timestamp columnsecond(column)Return the seconds from a timestamp columnto_timestamp(column)to_timestamp(column, fmt)Convert a string column representing a date or timestamp to a timestamp column in a DataFrame. It takes two arguments: the column containing the string representation of the date or timestamp, and the format string specifying the format of the input string.
## Date and Timestamp Window Functions

Below are PySpark Data and Timestamp window functions.
DATE & TIME WINDOW FUNCTION SYNTAXDATE & TIME WINDOW FUNCTION DESCRIPTIONwindow(timeColumn, windowDuration,slideDuration, startTime)Bucketize rows into one or more time windows given a timestamp specifying column. Window starts are inclusive but the window ends are exclusive, e.g. 12:05 will be in the window [12:05,12:10) but not in [12:00,12:05). Windows can support microsecond precision. Windows in the order of months are not supported.window(timeColumn, windowDuration, slideDuration)Bucketize rows into one or more time windows given a timestamp specifying column. Window starts are inclusive but the window ends are exclusive, e.g. 12:05 will be in the window [12:05,12:10) but not in [12:00,12:05). Windows can support microsecond precision. Windows in the order of months are not supported. The windows start beginning at 1970-01-01 00:00:00 UTCwindow(timeColumn, windowDuration)Generates tumbling time windows given a timestamp specifying column. Window starts are inclusive but the window ends are exclusive, e.g. 12:05 will be in the window [12:05,12:10) but not in [12:00,12:05). Windows can support microsecond precision. Windows in the order of months are not supported. The windows start beginning at 1970-01-01 00:00:00 UTC.
## PySpark SQL Date and Timestamp Functions Examples

Following are the most used PySpark S QL Date and Timestamp Functions with examples, you can use these on DataFrame and SQL expressions.

```

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create SparkSession
spark = SparkSession.builder \
            .appName('SparkByExamples.com') \
            .getOrCreate()
data=[["1","2020-02-01"],["2","2019-03-01"],["3","2021-03-01"]]
df=spark.createDataFrame(data,["id","input"])
df.show()

#Result
+---+----------+
| id|input     |
+---+----------+
|  1|2020-02-01|
|  2|2019-03-01|
|  3|2021-03-01|
+---+----------+

```

### current_date()

Use current_date() to get the current system date. By default, the data will be returned in yyyy-dd-mm format.

```

#current_date()
df.select(current_date().alias("current_date")
  ).show(1)

#Result
+------------+
|current_date|
+------------+
|  2021-02-22|
+------------+

```

### date_format()

The below example uses date_format() to parses the date and converts from yyyy-dd-mm to MM-dd-yyyy format.

```

#date_format()
df.select(col("input"), 
    date_format(col("input"), "MM-dd-yyyy").alias("date_format") 
  ).show()

#Result
+----------+-----------+
|input     |date_format|
+----------+-----------+
|2020-02-01| 02-01-2020|
|2019-03-01| 03-01-2019|
|2021-03-01| 03-01-2021|
+----------+-----------+

```

### to_date()

Below example converts string in date format yyyy-MM-dd to a DateType yyyy-MM-dd using to_date() . You can also use this to convert into any specific format. PySpark supports all patterns supports on Java DateTimeFormatter .

```

#to_date()
df.select(col("input"), 
    to_date(col("input"), "yyy-MM-dd").alias("to_date") 
  ).show()

#Result
+----------+----------+
|     input|   to_date|
+----------+----------+
|2020-02-01|2020-02-01|
|2019-03-01|2019-03-01|
|2021-03-01|2021-03-01|
+----------+----------+

```

### datediff()

The below example returns the difference between two dates using datediff() .

```

#datediff()
df.select(col("input"), 
    datediff(current_date(),col("input")).alias("datediff")  
  ).show()

#Result
+----------+--------+
|     input|datediff|
+----------+--------+
|2020-02-01|     387|
|2019-03-01|     724|
|2021-03-01|      -7|
+----------+--------+

```

### months_between()

The below example returns the months between two dates using months_between() .

```

#months_between()
df.select(col("input"), 
    months_between(current_date(),col("input")).alias("months_between")  
  ).show()

#Result
+----------+--------------+
|     input|months_between|
+----------+--------------+
|2020-02-01|   12.67741935|
|2019-03-01|   23.67741935|
|2021-03-01|   -0.32258065|
+----------+--------------+

```

### trunc()

The below example truncates the date at a specified unit using trunc() .

```

#trunc()
df.select(col("input"), 
    trunc(col("input"),"Month").alias("Month_Trunc"), 
    trunc(col("input"),"Year").alias("Month_Year"), 
    trunc(col("input"),"Month").alias("Month_Trunc")
   ).show()

#Result
+----------+-----------+----------+-----------+
|     input|Month_Trunc|Month_Year|Month_Trunc|
+----------+-----------+----------+-----------+
|2020-02-01| 2020-02-01|2020-01-01| 2020-02-01|
|2019-03-01| 2019-03-01|2019-01-01| 2019-03-01|
|2021-03-01| 2021-03-01|2021-01-01| 2021-03-01|
+----------+-----------+----------+-----------+

```

### add_months() , date_add(), date_sub()

Here we are adding and subtracting date and month from a given input.

```

#add_months() , date_add(), date_sub()
df.select(col("input"), 
    add_months(col("input"),3).alias("add_months"), 
    add_months(col("input"),-3).alias("sub_months"), 
    date_add(col("input"),4).alias("date_add"), 
    date_sub(col("input"),4).alias("date_sub") 
  ).show()

#Result
+----------+----------+----------+----------+----------+
|     input|add_months|sub_months|  date_add|  date_sub|
+----------+----------+----------+----------+----------+
|2020-02-01|2020-05-01|2019-11-01|2020-02-05|2020-01-28|
|2019-03-01|2019-06-01|2018-12-01|2019-03-05|2019-02-25|
|2021-03-01|2021-06-01|2020-12-01|2021-03-05|2021-02-25|
+----------+----------+----------+----------+----------+

```

### year(), month(), month(),next_day(), weekofyear()

```

df.select(col("input"), 
     year(col("input")).alias("year"), 
     month(col("input")).alias("month"), 
     next_day(col("input"),"Sunday").alias("next_day"), 
     weekofyear(col("input")).alias("weekofyear") 
  ).show()

#Result
+----------+----+-----+----------+----------+
|     input|year|month|  next_day|weekofyear|
+----------+----+-----+----------+----------+
|2020-02-01|2020|    2|2020-02-02|         5|
|2019-03-01|2019|    3|2019-03-03|         9|
|2021-03-01|2021|    3|2021-03-07|         9|
+----------+----+-----+----------+----------+

```

### dayofweek(), dayofmonth(), dayofyear()

```

df.select(col("input"),  
     dayofweek(col("input")).alias("dayofweek"), 
     dayofmonth(col("input")).alias("dayofmonth"), 
     dayofyear(col("input")).alias("dayofyear"), 
  ).show()

#Result
+----------+---------+----------+---------+
|     input|dayofweek|dayofmonth|dayofyear|
+----------+---------+----------+---------+
|2020-02-01|        7|         1|       32|
|2019-03-01|        6|         1|       60|
|2021-03-01|        2|         1|       60|
+----------+---------+----------+---------+

```

### current_timestamp()

Following are the Timestamp Functions that you can use on SQL and on DataFrame. Let’s learn these with examples.

Let’s create a test data.

```

data=[["1","02-01-2020 11 01 19 06"],["2","03-01-2019 12 01 19 406"],["3","03-01-2021 12 01 19 406"]]
df2=spark.createDataFrame(data,["id","input"])
df2.show(truncate=False)

#Result
+---+-----------------------+
|id |input                  |
+---+-----------------------+
|1  |02-01-2020 11 01 19 06 |
|2  |03-01-2019 12 01 19 406|
|3  |03-01-2021 12 01 19 406|
+---+-----------------------+

```

Below example returns the current timestamp in spark default format yyyy-MM-dd HH:mm:ss

```

#current_timestamp()
df2.select(current_timestamp().alias("current_timestamp")
  ).show(1,truncate=False)

#Result
+-----------------------+
|current_timestamp      |
+-----------------------+
|2021-02-22 20:13:29.673|
+-----------------------+

```

### to_timestamp()

Converts string timestamp to Timestamp type format.

```

#to_timestamp()
df2.select(col("input"), 
    to_timestamp(col("input"), "MM-dd-yyyy HH mm ss SSS").alias("to_timestamp") 
  ).show(truncate=False)

#Result
+-----------------------+-----------------------+
|input                  |to_timestamp           |
+-----------------------+-----------------------+
|02-01-2020 11 01 19 06 |2020-02-01 11:01:19.06 |
|03-01-2019 12 01 19 406|2019-03-01 12:01:19.406|
|03-01-2021 12 01 19 406|2021-03-01 12:01:19.406|
+-----------------------+-----------------------+

```

## hour(), Minute() and second()

```

#hour, minute,second
data=[["1","2020-02-01 11:01:19.06"],["2","2019-03-01 12:01:19.406"],["3","2021-03-01 12:01:19.406"]]
df3=spark.createDataFrame(data,["id","input"])

df3.select(col("input"), 
    hour(col("input")).alias("hour"), 
    minute(col("input")).alias("minute"),
    second(col("input")).alias("second") 
  ).show(truncate=False)

#Result
+-----------------------+----+------+------+
|input                  |hour|minute|second|
+-----------------------+----+------+------+
|2020-02-01 11:01:19.06 |11  |1     |19    |
|2019-03-01 12:01:19.406|12  |1     |19    |
|2021-03-01 12:01:19.406|12  |1     |19    |
+-----------------------+----+------+------+

```

## Conclusion:

In this post, I’ve consolidated the complete list of Date and Timestamp Functions with a description and example of some commonly used. You can find the complete list on the following blog .

Happy Learning !!

## Related Articles
- PySpark String Functions with Examples
- PySpark JSON Functions with Examples
- PySpark Column Class | Operators & Functions
- PySpark Aggregate Functions With Examples
- PySpark Window Functions With Examples
- PySpark SQL expr() (Expression ) Function
- PySpark SQL – Working with Unix Time | Timestamp
- PySpark SQL Types (DataType) with Examples
- How to Create a PySpark DataFrame with a Timestamp Column for a Date Range?
- Pyspark to_date() vs date_format()
- Top 100 PySpark Functions for Data Engineering Interviews

