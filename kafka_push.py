from kafka import KafkaProducer, KafkaConsumer
from data_generator import RandomDataGenerator
import json

def make_producer(host):
    producer = KafkaProducer(bootstrap_servers=[host], value_serializer=lambda x: json.dumps(x).encode("utf-8"))
    return producer

def send_random(producer):
    for msg in RandomDataGenerator():
        producer.send("probando", msg)

def main():
    producer = make_producer(host="kafka:29092")
    send_random(producer)

if __name__ == "__main__":
    main()