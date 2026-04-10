import paho.mqtt.client as mqtt
import threading

BROKER = "test.mosquitto.org"
PORT = 1883

CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc):
    print("\nController da ket noi broker!")
    client.subscribe(STATUS_TOPIC)

def on_message(client, userdata, msg):
    print("\nTrang thai nhan duoc:")
    print(msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# chạy loop ở thread riêng để vừa nhận vừa nhập
threading.Thread(target=client.loop_forever).start()

try:
    while True:
        cmd = input("\nNhap lenh (ON/OFF/EXIT): ").upper()

        if cmd == "EXIT":
            break

        if cmd not in ["ON", "OFF"]:
            print("Lenh khong hop le!")
            continue

        client.publish(CMD_TOPIC, cmd)
        print(f"Da gui lenh {cmd} toi light01")

except KeyboardInterrupt:
    print("\nDung controller")

finally:
    client.disconnect()