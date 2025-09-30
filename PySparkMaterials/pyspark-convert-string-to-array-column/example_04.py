# Example 04 from: PySpark Convert String to Array Column

from pyspark.sql.functions import split

# Splitting the "name" column into an array of first name, middle name, and last name
df = df.withColumn("name_array", split(df["name"], ",\s*"))

# Displaying the updated DataFrame
df.show(truncate=False)
