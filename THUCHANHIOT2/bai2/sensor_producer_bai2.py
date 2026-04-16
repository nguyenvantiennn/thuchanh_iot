import pika
import json
import random
import time

# Kết nối RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

queue_name = "sensor_data_queue"
channel.queue_declare(queue=queue_name)

devices = ["sensor01", "sensor02", "sensor03"]

try:
    while True:
        device_id = random.choice(devices)

        temperature = round(random.uniform(25, 40), 1)
        humidity = round(random.uniform(30, 80), 1)

        data = {
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity
        }

        message = json.dumps(data)

        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message
        )

        print("Da gui:", message)

        time.sleep(3)

except KeyboardInterrupt:
    print("\nDung sensor producer")

finally:
    connection.close()