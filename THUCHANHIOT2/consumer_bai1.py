import pika
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

queue_name = "iot_lab_queue"
channel.queue_declare(queue=queue_name)

print("Dang cho message... Nhan Ctrl+C de dung")

def callback(ch, method, properties, body):
    now = datetime.now().strftime("%H:%M:%S")

    print("\nDa nhan message:", body.decode())
    print("Thoi gian nhan:", now)

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