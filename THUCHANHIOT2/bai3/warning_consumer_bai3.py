import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

exchange_name = "iot_alert_exchange"
queue_name = "warning_queue"

# Tạo exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='direct'
)

# Tạo queue
channel.queue_declare(queue=queue_name)

# Bind với routing key "warning"
channel.queue_bind(
    exchange=exchange_name,
    queue=queue_name,
    routing_key="warning"
)

print("Dang cho warning...")

def callback(ch, method, properties, body):
    print(f"[warning_queue] Da nhan: {body.decode()}")

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()