from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("probando", bootstrap_servers=['localhost:29092'], value_deserializer=lambda x: json.loads(x))

for msg in consumer:
    print(msg.value)
    print("recibido")