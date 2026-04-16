import pika
import time

# Kết nối RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

# Tạo queue
queue_name = "iot_lab_queue"
channel.queue_declare(queue=queue_name)

# Thông tin sinh viên
name = "Nguyen Van Tien"
student_id = "B21DCCN706"

message = f"Xin chao tu ung dung Python AMQP - {student_id} - {name}"

print("Nhap message (go 'exit' de thoat):")

try:
    while True:
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message
        )

        print("Da gui:", message)
        
        time.sleep(3)

except KeyboardInterrupt:
    print("\nDung producer")

finally:
    connection.close()