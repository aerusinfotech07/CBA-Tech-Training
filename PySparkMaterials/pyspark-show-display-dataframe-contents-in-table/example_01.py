# Example 01 from: PySpark show() – Display DataFrame Contents in Table

# Default - displays 20 rows and 
# 20 charactes from column value 
df.show()

#Display full column contents
df.show(truncate=False)

# Display 2 rows and full column contents
df.show(2,truncate=False) 

# Display 2 rows & column values 25 characters
df.show(2,truncate=25) 

# Display DataFrame rows & columns vertically
df.show(n=3,truncate=25,vertical=True)
