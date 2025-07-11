import json
import time
import random
import paho.mqtt.client as mqtt

# KONFIGURASI MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "DATA/LOCAL/SENSOR/PANEL_1"
CLIENT_ID = "node1"

# INISIALISASI
prev_temp = 27.0  # suhu awal
client = mqtt.Client(CLIENT_ID)
client.connect(BROKER, PORT)

print("🟢 Node simulator started...")

# LOOP UTAMA
while True:
    # Simulasi voltage, current, power
    voltage = round(random.uniform(218.0, 222.0), 2)
    current = round(random.uniform(1.5, 2.0), 2)
    power = round(voltage * current, 2)

    # Simulasi suhu naik-turun
    delta = random.choice([-0.3, 0, 0.3, 0.5])
    temp = round(prev_temp + delta, 2)

    # Logika pendingin menyala jika suhu naik >= 2%
    cooler_on = temp >= prev_temp * 1.02

    # Simpan suhu terakhir untuk perbandingan
    prev_temp = temp

    # Buat payload JSON
    payload = {
        "voltage": voltage,
        "current": current,
        "power": power,
        "temperature": temp,
        "cooler_status": cooler_on
    }

    # Publish ke broker MQTT lokal
    client.publish(TOPIC, json.dumps(payload))
    print("📤 Published:", payload)

    time.sleep(1)  # interval 1 detik
