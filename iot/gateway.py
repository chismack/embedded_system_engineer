import json
import mysql.connector
import paho.mqtt.client as mqtt
import ssl

# Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",  # ganti sesuai MySQL kamu
    database="iot"
)
cursor = db.cursor()

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

# MQTT LOCAL (Node → Gateway)
def on_connect_local(client, userdata, flags, rc):
    print("🟢 Connected to LOCAL broker")
    client.subscribe("DATA/LOCAL/SENSOR/PANEL_1")

def on_message_local(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        print("📥 Received MQTT:", data)

        # Simpan ke DB lokal
        save_to_db(data)

        # Kirim ulang ke MQTT Cloud
        payload_str = json.dumps(data)
        cloud_client.publish("DATA/ONLINE/SENSOR/PANEL_1", payload_str)
        print("📤 Forwarded to CLOUD MQTT")

    except Exception as e:
        print("❌ Error:", e)

local_client = mqtt.Client()
local_client.on_connect = on_connect_local
local_client.on_message = on_message_local
local_client.connect("localhost", 1883, 60)

# MQTT CLOUD (Gateway → Server)
cloud_client = mqtt.Client()
cloud_client.username_pw_set("embedded_test", "Ravelware1402")

cloud_client.tls_set(
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
    ciphers=None
)

cloud_client.connect("942ef292b9954450bfe231590d100cf3.s1.eu.hivemq.cloud", 8883)

# Start MQTT Loop
cloud_client.loop_start()
local_client.loop_forever()
