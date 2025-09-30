# Example 11 from: PySpark 4.0 Tutorial For Beginners with Examples

# Stream from Kafka
df = spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "192.168.1.100:9092")
        .option("subscribe", "json_topic")
        .option("startingOffsets", "earliest") // From starting
        .load()
