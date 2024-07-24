from confluent_kafka import Consumer

def delivery_report(err, msg):
    if err is not None:
        print(msg.id(), err)
    else:
        print(f'{msg.id()} delivered to {msg.topic()}')

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'foo',
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

consumer.subscribe(['test_topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None: continue
    if msg.error():
        print(f'error: {msg.error()}')
    else:
        print(f'consumed {msg.key()}:  {msg.value()}')

consumer.close()