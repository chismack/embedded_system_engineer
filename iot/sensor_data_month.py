import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Jumlah data: 1 bulan x 60 menit x 24 jam x 30 hari = 43.200 (1 data per menit)
start_time = datetime(2025, 6, 1, 0, 0, 0)
data = []

for i in range(43200):  # 30 hari x 24 jam x 60 menit
    timestamp = start_time + timedelta(minutes=i)

    # Voltage normal: 219–221V, kadang turun/naik
    if random.random() < 0.85:
        voltage = round(random.uniform(219.0, 221.0), 2)
    else:
        voltage = round(random.uniform(216.0, 223.0), 2)

    # Current acak tapi wajar
    current = round(random.uniform(1.5, 2.0), 2)
    power = round(voltage * current, 2)

    # Suhu normal 24–25°C, kadang naik
    if random.random() < 0.85:
        temperature = round(random.uniform(24.0, 25.0), 2)
    else:
        temperature = round(random.uniform(22.0, 27.0), 2)

    # Cooler status random (opsional)
    cooler_status = temperature > 25.0

    data.append([voltage, current, power, temperature, cooler_status, timestamp])

# Simpan ke CSV
df = pd.DataFrame(data, columns=["voltage", "current", "power", "temperature", "cooler_status", "timestamp"])

# Pastikan folder /data ada
os.makedirs("data", exist_ok=True)
df.to_csv("data/sensor_data_month.csv", index=False)

print("✅ File sensor_data_month.csv berhasil dibuat di folder /data")
