import paho.mqtt.client as mqtt
import json
from datetime import datetime

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/+/data"

def on_connect(client, userdata, flags, rc):
    print("Da ket noi broker!")
    print("Dang lang nghe du lieu sensor...\n")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        device = data["device_id"]
        temp = data["temperature"]
        hum = data["humidity"]

        now = datetime.now().strftime("%H:%M:%S")

        print("===== SENSOR DATA =====")
        print("Time:", now)
        print("Device:", device)
        print("Temperature:", temp, "C")
        print("Humidity:", hum, "%")

        # Kiểm tra cảnh báo
        if temp > 35:
            print("CANH BAO: Nhiet do cao")

        if hum < 40:
            print("CANH BAO: Do am thap")

        print("========================\n")

    except Exception as e:
        print("Loi xu ly du lieu:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("\nDung monitoring subscriber")

finally:
    client.disconnect()