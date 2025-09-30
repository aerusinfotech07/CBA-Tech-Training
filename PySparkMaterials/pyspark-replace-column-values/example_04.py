# Example 04 from: PySpark Replace Column Values in DataFrame

#Replace values from Dictionary
stateDic={'CA':'California','NY':'New York','DE':'Delaware'}
df2=df.rdd.map(lambda x: 
    (x.id,x.address,stateDic[x.state]) 
    ).toDF(["id","address","state"])
df2.show()

#+---+------------------+----------+
#| id|           address|     state|
#+---+------------------+----------+
#|  1|  14851 Jeffrey Rd|  Delaware|
#|  2|43421 Margarita St|  New York|
#|  3|  13111 Siemon Ave|California|
#+---+------------------+----------+
