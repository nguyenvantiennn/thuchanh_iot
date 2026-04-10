import paho.mqtt.client as mqtt
import time

# Thông tin public broker
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"

# Tạo client
client = mqtt.Client()

# Kết nối broker
client.connect(BROKER, PORT, 60)

# Thông tin sinh viên
name = "Nguyen Van Tien"
student_id = "B21DCCN706"

try:
    while True:
        # Gửi message
        message = f"Xin chao tu Client Python MQTT - {student_id} - {name}"
        
        client.publish(TOPIC, message)
        print("Da gui:", message)
        
        time.sleep(3)

except KeyboardInterrupt:
    print("Dung publisher")
finally:
    client.disconnect()