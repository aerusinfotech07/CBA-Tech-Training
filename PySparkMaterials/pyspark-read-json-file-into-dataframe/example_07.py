# Example 07 from: PySpark Read JSON file into DataFrame

spark.sql("CREATE OR REPLACE TEMPORARY VIEW zipcode USING json OPTIONS" + 
      " (path 'resources/zipcodes.json')")
spark.sql("select * from zipcode").show()
