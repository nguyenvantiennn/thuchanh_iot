# THỰC HÀNH: LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

## Yêu cầu
- Python 3.x
- paho-mqtt

## Cài đặt
pip install paho-mqtt

## Broker sử dụng
test.mosquitto.org:1883

## Cách chạy Bài 1. Ứng dụng gửi và nhận thông điệp MQTT cơ bản

### B1: Chạy subscriber trong terminal 1
python subscriber_bai1.py
<img width="952" height="126" alt="image" src="https://github.com/user-attachments/assets/f46fd69e-ba71-4309-92d3-a9d8587bd5cd" />

### B2: Chạy publisher trong terminal 2
python publisher_bai1.py
<img width="945" height="107" alt="image" src="https://github.com/user-attachments/assets/8649cab1-a797-4972-928d-25b224d6dca3" />
### Subcriber nhận kết quả
<img width="526" height="230" alt="image" src="https://github.com/user-attachments/assets/55a238d4-0ed6-43ad-ba55-6251435e1e18" />

## Mô tả
Publisher gửi message chứa:
- Họ tên
- Mã sinh viên
- Nội dung chào

Subscriber nhận và hiển thị:
- Topic
- Payload
- Thời gian

## Cách chạy Bài 2. Mô phỏng cảm biến nhiệt độ và độ ẩm bằng MQTT

### B1: Chạy subscriber trong terminal 1
python monitoring_subscriber_bai2.py
<img width="1004" height="125" alt="image" src="https://github.com/user-attachments/assets/2ed3dff1-dea1-441b-9c9d-eb0225f387b4" />

### B2: Chạy publisher trong terminal 2
python sensor_publisher_bai2.py
<img width="987" height="176" alt="image" src="https://github.com/user-attachments/assets/36334a63-2c58-4c91-b424-ecfc128ca19f" />

### Subscriber nhận kết quả
<img width="335" height="254" alt="image" src="https://github.com/user-attachments/assets/09939b8f-5e77-416e-a08b-fef796adcea4" />

## Mô tả

Payload JSON
{
  "device_id": "sensor01",
  "temperature": 28.5,
  "humidity": 65.2
}

Điều kiện cảnh báo
- Nhiệt độ > 35°C
- Độ ẩm < 40%

## Cách chạy Bài 3. Mô phỏng hệ thống điều khiển đèn thông minh qua MQTT

### B1: Chạy device trong terminal 1
python device_bai3.py
<img width="923" height="99" alt="image" src="https://github.com/user-attachments/assets/077d2aa6-344d-41fa-953d-74038a8c0c3e" />

### B2: Chạy controller trong terminal 2
python controller_bai3.py
<img width="948" height="223" alt="image" src="https://github.com/user-attachments/assets/560b9469-4fe3-4c7a-bfc2-664334b1cb13" />

### Device xử lý và gửi lại trạng thái
<img width="936" height="125" alt="image" src="https://github.com/user-attachments/assets/e4551f56-7987-42ff-ac64-2f4483dfbc21" />

## Mô tả

JSON
{ "device_id": "light01", "status": "ON" }

Subscribe nhận lệnh:
- ON → bật đèn
- OFF → tắt đèn
Sau mỗi lệnh hợp lệ:
- Cập nhật trạng thái
- Publish trạng thái lên topic status

