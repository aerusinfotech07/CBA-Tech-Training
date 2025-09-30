# Example 03 from: PySpark – Convert array column to a String

df.createOrReplaceTempView("ARRAY_STRING")
spark.sql("select name, concat_ws(',',languagesAtSchool) as languagesAtSchool," + \
    " currentState from ARRAY_STRING") \
    .show(truncate=False)
