# Example 05 from: PySpark – Difference between two dates (days, months, years)

# SQL Example
spark.sql("select round(months_between('2019-07-01',current_date())/12,2) as years_diff")
     .show()
