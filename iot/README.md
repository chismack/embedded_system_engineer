# Technical Test Embedded System Engineer 2025
**PT Ravelware Technology Indonesia**  
Nama: Raudhafilhaq Alfitrah  
Email: [dhafie.alf@gmail.com]  

# Deskripsi Proyek

**IoT Monitoring System** adalah sistem embedded yang terintegrasi dengan beberapa sensor yaitu Power Meter dan Temperature, serta aktuator berupa Cooler Fan. Sistem ini berfungsi untuk memonitor penggunaan voltage, current, power, dan temperature pada ruang mesin yang memerlukan kontrol suhu secara rutin.

Sistem akan membaca data setiap 1 detik, dan jika terjadi kenaikan suhu sebesar 2% dari suhu sebelumnya, maka aktuator Cooler Fan akan aktif secara otomatis untuk menjaga suhu tetap stabil. Selain itu, sistem juga menyimpan dan mengirimkan data secara real-time setiap detik ke database lokal dan server online menggunakan protokol MQTT.

# 📦 Struktur Sistem

## Node:
- Membaca data suhu dan daya (voltage, current, power)
- Mengaktifkan fan (relay) bila suhu naik ≥ 2% dari sebelumnya
- Mengirim data via MQTT ke broker lokal

## Gateway:
- Menerima data dari Node melalui MQTT lokal
- Menyimpan data ke MySQL
- Meneruskan data ke HiveMQ Cloud (MQTT online)

# 🧩 Arsitektur & Diagram

Diagram disimpan di folder /diagram:

- 🗂️ `schematic_diagram.png` 
- 🗂️ `flowchart_node.png` 
- 🗂️ `flowchart_gateway.png` 
- 🗂️ `mqtt_connection_diagram.png` 
