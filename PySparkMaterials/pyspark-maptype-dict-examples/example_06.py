# Example 06 from: PySpark MapType (Dict) Usage with Examples

from pyspark.sql.functions import explode,map_keys
keysDF = df.select(explode(map_keys(df.properties))).distinct()
keysList = keysDF.rdd.map(lambda x:x[0]).collect()
print(keysList)
#['eye', 'hair']
