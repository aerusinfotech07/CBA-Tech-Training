# Example 09 from: PySpark Column Class | Operators & Functions

#getField from MapType
df.select(df.properties.getField("hair")).show()

#getField from Struct
df.select(df.name.getField("fname")).show()
