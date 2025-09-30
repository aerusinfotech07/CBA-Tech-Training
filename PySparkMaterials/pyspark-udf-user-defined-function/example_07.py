# Example 07 from: PySpark UDF (User Defined Function)

""" 
No guarantee Name is not null will execute first
If convertUDF(Name) like '%John%' execute first then 
you will get runtime error
"""
spark.sql("select Seqno, convertUDF(Name) as Name from NAME_TABLE " + \ 
         "where Name is not null and convertUDF(Name) like '%John%'") \
     .show(truncate=False)
