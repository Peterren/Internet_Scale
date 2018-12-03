from kafka import KafkaConsumer
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
import json
import time


es = Elasticsearch(['es'])
consumer = KafkaConsumer('drivers', group_id='drivers-indexer', bootstrap_servers=['kafka:9092'])
for message in consumer:
    drivers = (json.loads((message.value).decode('utf-8')))
    es.index(index='drivers-indexer',doc_type = 'listing',id = drivers['username'], body = drivers)
    es.indices.refresh(index="drivers-indexer")