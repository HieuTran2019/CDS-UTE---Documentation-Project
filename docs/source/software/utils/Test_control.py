import serial
import time

# Mở cổng Serial
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # chờ mạch khởi động

def control(speed=0, angle=0):
    """
    Gửi lệnh điều khiển ESC (speed) và Servo (angle) qua Serial.
    speed: -25..25
    angle: -25..25
    """
    # Giới hạn giá trị
    speed = max(min(speed, 25), -25)
    angle = max(min(angle, 25), -25)

    # Tạo chuỗi lệnh dạng "speed,angle\n"
    cmd = f"{speed},{angle}\n"
    ser.write(cmd.encode())

    print(f"Sent -> Speed: {speed}, Angle: {angle}")

# ---- Ví dụ sử dụng ----
if __name__ == "__main__":
    control(10, 10)  # Tiến và đánh lái sang phải
    time.sleep(5)
    control(-5, -15) # Lùi và đánh lái sang trái
    time.sleep(5)
    control(10, 25)  # Tiến và đánh lái sang phải
    time.sleep(5)
    control(-15, -25) # Lùi và đánh lái sang trái
    time.sleep(5)
    control(0, 0)    # Dừng và lái thẳng

    control(0, 0)    # Dừng và lái thẳng
