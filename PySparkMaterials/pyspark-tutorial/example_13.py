# Example 13 from: PySpark 4.0 Tutorial For Beginners with Examples

# Import
from graphframes import GraphFrame

# Define vertices DataFrame
vertices = spark.createDataFrame([
    ("a", "Raman", 34),
    ("b", "Bob", 36),
    ("c", "Naveen", 30),
    ("d", "Kumar", 29)
], ["id", "name", "age"])

# Define edges DataFrame
edges = spark.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "d", "friend"),
    ("d", "a", "follow")
], ["src", "dst", "relationship"])

# Create a GraphFrame
g = GraphFrame(vertices, edges)

# Query the graph
g.vertices.show()
g.edges.show()

# Find the shortest path between two vertices
results = g.shortestPaths(landmarks=["a", "d"])
results.select("id", "distances").show()

# Stop the SparkSession
spark.stop()
