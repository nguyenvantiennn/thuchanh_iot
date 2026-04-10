import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "test.mosquitto.org"
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

devices = ["sensor01", "sensor02", "sensor03"]

try:
    while True:

        device_id = random.choice(devices)
        TOPIC = f"iot/lab/{device_id}/data"
        # Sinh dữ liệu
        temperature = round(random.uniform(25, 40), 1)  # 25 -> 40°C
        humidity = round(random.uniform(30, 80), 1)     # 30 -> 80%

        data = {
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity
        }

        payload = json.dumps(data)

        client.publish(TOPIC, payload)

        print("Da gui:", payload)

        time.sleep(3)

except KeyboardInterrupt:
    print("\nDung sensor publisher")

finally:
    client.disconnect()