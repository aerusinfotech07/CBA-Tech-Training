# Example 03 from: PySpark where() & filter() for efficient data filtering

# Prepare Data
data2 = [(2,"Michael Rose"),(3,"Robert Williams"),
     (4,"Rames Rose"),(5,"Rames rose")
  ]
df2 = spark.createDataFrame(data = data2, schema = ["id","name"])

# like - SQL LIKE pattern
df2.filter(df2.name.like("%rose%")).show()

# Output
#+---+----------+
#| id|      name|
#+---+----------+
#|  5|Rames rose|
#+---+----------+

# rlike - SQL RLIKE pattern (LIKE with Regex)
# This check case insensitive
df2.filter(df2.name.rlike("(?i)^*rose$")).show()

# Output
#+---+------------+
#| id|        name|
#+---+------------+
#|  2|Michael Rose|
#|  4|  Rames Rose|
#|  5|  Rames rose|
