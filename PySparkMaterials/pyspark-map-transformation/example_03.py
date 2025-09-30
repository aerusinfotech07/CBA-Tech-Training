# Example 03 from: PySpark map() Transformation

# By Calling function
def func1(x):
    firstName=x.firstname
    lastName=x.lastname
    name=firstName+","+lastName
    gender=x.gender.lower()
    salary=x.salary*2
    return (name,gender,salary)

# Apply the func1 function using lambda
rdd2 = df.rdd.map(lambda x: func1(x))

#or
# Apply the func1 function to each element of the RDD using map()
rdd2 = df.rdd.map(func1)
