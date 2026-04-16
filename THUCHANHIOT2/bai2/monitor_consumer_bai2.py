import pika
import json

# Kết nối RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

queue_name = "sensor_data_queue"
channel.queue_declare(queue=queue_name)

print("Dang cho du lieu sensor...")

def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode())

        device = data["device_id"]
        temp = data["temperature"]
        hum = data["humidity"]

        print("\n===== SENSOR DATA =====")
        print("Device:", device)
        print("Temperature:", temp)
        print("Humidity:", hum)

        if temp > 35:
            print("CANH BAO: Nhiet do cao")

        if hum < 40:
            print("CANH BAO: Do am thap")

        print("========================")

    except Exception as e:
        print("Loi xu ly:", e)

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

try:
    channel.start_consuming()

except KeyboardInterrupt:
    print("\nDung consumer")

finally:
    connection.close()