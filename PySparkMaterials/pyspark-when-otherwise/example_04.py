# Example 04 from: PySpark When Otherwise | SQL Case When Usage

df.createOrReplaceTempView("EMP")
spark.sql("select name, CASE WHEN gender = 'M' THEN 'Male' " + 
               "WHEN gender = 'F' THEN 'Female' WHEN gender IS NULL THEN ''" +
              "ELSE gender END as new_gender from EMP").show()
