# Example 05 from: PySpark StructType & StructField Explained with Examples

# Create StructType from DDL String
ddlSchemaStr = "`fullName` STRUCT<`first`: STRING, `last`: STRING,
 `middle`: STRING>,`age` INT,`gender` STRING"
ddlSchema = StructType.fromDDL(ddlSchemaStr)
ddlSchema.printTreeString()
