from confluent_kafka import Producer

import socket

def delivery_report(err, msg):
    if err is not None:
        print(msg.id(), err)
    else:
        print('delivered')


conf = {'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname()}

producer = Producer(conf)

for i in range(10):
    producer.produce('test_topic', key=f'key_{i}', value=f'value_{i}',
                     callback=delivery_report)
    
producer.flush()