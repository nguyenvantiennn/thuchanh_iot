# THỰC HÀNH: LẬP TRÌNH PYTHON VỚI GIAO THỨC AMQP

## Yêu cầu
- Python 3.x
- paho-mqtt

## Cài đặt
pip install pika

## Broker sử dụng
Broker cục bộ: RabbitMQ chạy trên localhost
Port: 5672 (AMQP mặc định)
Management UI: http://localhost:15672 (user: guest / pass: guest)

## Cách chạy Bài 1. Gửi và nhận message cơ bản qua queue

### B1: Chạy Consumer trong terminal 1
```bash
python consumer_bai1.py
```
<img width="464" height="89" alt="image" src="https://github.com/user-attachments/assets/827d0a5c-fc50-493b-a2f0-d8280b896466" />

### B2: Chạy Producer trong terminal 2
```bash
python producer_bai1.py
```
<img width="517" height="103" alt="image" src="https://github.com/user-attachments/assets/2d3545f3-7485-46e0-a9cc-090a5cdc31fc" />

### Consumer nhận kết quả

<img width="597" height="201" alt="image" src="https://github.com/user-attachments/assets/34c0c6ba-9343-481c-b21e-5c3a3012730e" />

## Mô tả
Producer → Queue → Consumer

Producer: gửi message vào queue
Queue: lưu trữ message tạm thời
Consumer: nhận và xử lý message

Message chứa:

Nội dung chào mừng
Mã sinh viên
Họ tên sinh viên

## Cách chạy Bài 2. Mô phỏng cảm biến IoT gửi dữ liệu môi trường

### B1: Chạy Consumer trong terminal 1

```bash
python monitor_consumer_bai2.py
```
<img width="502" height="76" alt="image" src="https://github.com/user-attachments/assets/cd94686d-6d59-4b46-b9ff-372db39f6a7e" />

### B2: Chạy Producer trong terminal 2
``` bash
python sensor_publisher_bai2.py
```
<img width="519" height="120" alt="image" src="https://github.com/user-attachments/assets/225304ee-ee8d-4ca3-b909-b7c305c2b620" />

### Consumer nhận kết quả

<img width="257" height="202" alt="image" src="https://github.com/user-attachments/assets/b56bcf39-c8c5-49dc-8b6f-ddae0e3774f7" />


## Mô tả

Sensor Producer → Queue → Monitoring Consumer

Producer gửi dữ liệu vào queue
Consumer nhận và xử lý dữ liệu

Payload JSON
{
  "device_id": "sensor01",
  "temperature": 28.5,
  "humidity": 65.2
}

Điều kiện cảnh báo
- Nhiệt độ > 35°C
- Độ ẩm < 40%

## Cách chạy Bài 3. Mô phỏng hệ thống điều phối cảnh báo IoT với exchange

### B1: Chạy device trong terminal 1
python device_bai3.py
<img width="491" height="81" alt="image" src="https://github.com/user-attachments/assets/d2049126-4804-4f65-a2e2-afa31de1f5a2" />

### B2: Chạy controller trong terminal 2
python controller_bai3.py
<img width="503" height="80" alt="image" src="https://github.com/user-attachments/assets/d0bc52ad-69c8-47a4-93a9-3e9674755612" />

### Kết quả:

Alert Producer gửi 3 cảnh báo với routing key info, warning, critical

Warning Consumer (warning_queue) chỉ nhận message có routing key warning

Critical Consumer (critical_queue) chỉ nhận message có routing key critical

Message info không được consumer nào nhận

<img width="488" height="127" alt="image" src="https://github.com/user-attachments/assets/9ec6421d-962d-4dcb-a484-4d53c79ee218" />


<img width="491" height="89" alt="image" src="https://github.com/user-attachments/assets/9213a812-d5b7-4369-8e8f-aeadb5ed2949" />


<img width="511" height="94" alt="image" src="https://github.com/user-attachments/assets/9702f2a4-a6a4-4279-94bb-4a5fc2505faf" />


## Mô tả

Producer → Exchange → Queue → Consumer

Producer gửi message vào exchange
Exchange phân phối message dựa trên routing key
Queue nhận message phù hợp
Consumer đọc message từ queue
