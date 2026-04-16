import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

exchange_name = "iot_alert_exchange"

# Tạo direct exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='direct'
)

messages = [
    ("info", "He thong hoat dong binh thuong"),
    ("warning", "Nhiet do phong may vuot nguong warning"),
    ("critical", "Cam bien kho lanh mat ket noi critical")
]

try:
    for key, msg in messages:
        channel.basic_publish(
            exchange=exchange_name,
            routing_key=key,
            body=msg
        )

        print(f"Da gui [{key}]: {msg}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Dung producer")

finally:
    connection.close()