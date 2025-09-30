# Example 06 from: PySpark JSON Functions with Examples

from pyspark.sql.functions import schema_of_json,lit
schemaStr=spark.range(1) \
    .select(schema_of_json(lit("""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""))) \
    .collect()[0][0]
print(schemaStr)

//struct<City:string,State:string,ZipCodeType:string,Zipcode:bigint>
