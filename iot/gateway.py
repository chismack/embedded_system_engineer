import json
import mysql.connector
import paho.mqtt.client as mqtt

# KONFIGURASI DATABASE
db = mysql.connector.connect(
    host="localhost",
    user="root",           # Ganti jika user MySQL kamu bukan 'root'
    password="admin123",   # Ganti dengan password yang kamu gunakan di MySQL
    database="iot"         # Sesuai schema yang kamu buat
)
cursor = db.cursor()

# FUNGSI SIMPAN DATA
def save_to_db(data):
    query = """
        INSERT INTO sensor_data (voltage, current, power, temperature, cooler_status)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        float(data.get("voltage", 0)),
        float(data.get("current", 0)),
        float(data.get("power", 0)),
        float(data.get("temperature", 0)),
        bool(data.get("cooler_status", False))
    )
    cursor.execute(query, values)
    db.commit()
    print("✅ Data saved to DB:", values)

# HANDLER MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("🟢 Connected to MQTT broker")
        client.subscribe("DATA/LOCAL/SENSOR/PANEL_1")
    else:
        print("🔴 Failed to connect, return code:", rc)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        print("📥 Received MQTT message:", data)
        save_to_db(data)
    except Exception as e:
        print("❌ Error handling message:", e)

# MQTT CLIENT 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)  # MQTT broker lokal (Mosquitto)
client.loop_forever()
