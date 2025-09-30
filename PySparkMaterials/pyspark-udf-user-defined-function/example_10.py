# Example 10 from: PySpark UDF (User Defined Function)

spark.udf.register("_nullsafeUDF", lambda str: convertCase(str) if not str is None else "" , StringType())

spark.sql("select _nullsafeUDF(Name) from NAME_TABLE2") \
     .show(truncate=False)

spark.sql("select Seqno, _nullsafeUDF(Name) as Name from NAME_TABLE2 " + \
          " where Name is not null and _nullsafeUDF(Name) like '%John%'") \
     .show(truncate=False)
