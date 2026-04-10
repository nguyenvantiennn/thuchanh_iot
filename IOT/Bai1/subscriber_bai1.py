import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"

# Khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print("Da ket noi broker!")
    print("Topic:", TOPIC)
    client.subscribe(TOPIC)

# Khi nhận được message
def on_message(client, userdata, msg):
    now = datetime.now().strftime("%H:%M:%S")
    
    print("\n===== MESSAGE =====")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())
    print("Time:", now)
    print("===================")

# Tạo client
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    print("Ctrl+C de dung subscriber")
    client.loop_forever()

except KeyboardInterrupt:
    print("Dung subscriber")
finally:
    client.disconnect()