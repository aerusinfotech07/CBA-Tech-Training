# Example 04 from: PySpark transform() Function with Example

# custom function
def select_columns(df):
    return df.select("CourseName","discounted_fee")

# Chain transformations
df2 = df.transform(to_upper_str_columns) \
        .transform(reduce_price,1000) \
        .transform(apply_discount) \
        .transform(select_columns)
