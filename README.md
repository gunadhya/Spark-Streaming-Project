# Spark-Streaming-Project

## Outputs

### Kafka Producer
![Image of Yaktocat](https://github.com/gunadhya/Spark-Streaming-Project/blob/main/Spark%20Streaming/kafka_server%20producer.png)

### Kafka Console Consumer
![Image of Yaktocat](https://github.com/gunadhya/Spark-Streaming-Project/blob/main/Spark%20Streaming/kafka%20console%20consumer.png)

### Progress 
![Image of Yaktocat](https://github.com/gunadhya/Spark-Streaming-Project/blob/main/Spark%20Streaming/Progress.png)
![Image of Yaktocat](https://github.com/gunadhya/Spark-Streaming-Project/blob/main/Spark%20Streaming/Count.png)

### Streaming UI
![Image of Yaktocat](https://github.com/gunadhya/Spark-Streaming-Project/blob/main/Streaming%20UI.PNG)


1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

*  `processedRowsPerSecond` is affected.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

* `spark.default.parallelism`
* `spark.streaming.kafka.maxRatePerPartition`

  Based on the processed rows per second.
