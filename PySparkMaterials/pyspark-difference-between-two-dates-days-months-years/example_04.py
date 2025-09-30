# Example 04 from: PySpark – Difference between two dates (days, months, years)

# Imports
from pyspark.sql.functions import current_date,to_date

# Create DF with custom date formats
data2 = [("1","07-01-2019"),("2","06-24-2019"),("3","08-24-2019")]  
df2=spark.createDataFrame(data=data2,schema=["id","date"])

# Convert date and calculate
df2.select(
   months_between(to_date(col("date"),"MM-dd-yyyy"),current_date()).alias("monthsdiff")
    ).show()
