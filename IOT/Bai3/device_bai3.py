import paho.mqtt.client as mqtt
import json

BROKER = "test.mosquitto.org"
PORT = 1883

CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

device_id = "light01"
status = "OFF"

# Khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print("Light device da ket noi broker!")
    client.subscribe(CMD_TOPIC)

# Khi nhận được lệnh
def on_message(client, userdata, msg):
    global status

    command = msg.payload.decode().upper()
    print("Nhan lenh:", command)

    if command == "ON":
        status = "ON"
    elif command == "OFF":
        status = "OFF"
    else:
        print("Lenh khong hop le!")
        return

    # Gửi trạng thái
    data = {
        "device_id": device_id,
        "status": status
    }

    payload = json.dumps(data)
    client.publish(STATUS_TOPIC, payload)

    print("Da cap nhat trang thai:", payload)
    
# Tạo client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDung light device")
    client.disconnect()