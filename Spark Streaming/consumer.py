from kafka import KafkaConsumer
import time

class ConsumerServer(KafkaConsumer):
    
    def __init__(self, topic_name):
        self.consumer = KafkaConsumer(
                        bootstrap_servers = "localhost:9092", 
                        request_timeout_ms = 1000, 
                        auto_offset_reset="earliest", 
                        max_poll_records=10
                        )   
        self.consumer.subscribe(topics = topic_name)
    
    def consume(self):
        try:
            while True:
                for consumer_record in self.consumer.poll().items():
                    if consumer_record:
                        for record in consumer_record:
                            print(f'Consumer : {record.value} \n')
                    else:
                        print("No message")
                        
                time.sleep(0.5)
        except:
            self.consumer.close()
            
if __name__ == "__main__":
    consumer = ConsumerServer("calls-api")
    consumer.consume()