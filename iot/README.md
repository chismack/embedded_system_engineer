# Technical Test Embedded System Engineer 2025
**PT Ravelware Technology Indonesia**  
Nama: Raudhafilhaq Alfitrah  
Email: [dhafie.alf@gmail.com]  

# Deskripsi Proyek

**IoT Monitoring System** adalah sistem embedded yang terintegrasi dengan beberapa sensor yaitu Power Meter dan Temperature, serta aktuator berupa Cooler Fan. Sistem ini berfungsi untuk memonitor penggunaan voltage, current, power, dan temperature pada ruang mesin yang memerlukan kontrol suhu secara rutin.

Sistem akan membaca data setiap 1 detik, dan jika terjadi kenaikan suhu sebesar 2% dari suhu sebelumnya, maka aktuator Cooler Fan akan aktif secara otomatis untuk menjaga suhu tetap stabil. Selain itu, sistem juga menyimpan dan mengirimkan data secara real-time setiap detik ke database lokal dan server online menggunakan protokol MQTT.

# Fitur Utama

- Simulasi pembacaan sensor Power Meter dan suhu
- Logika otomatis Cooler Fan berbasis kenaikan suhu ≥ 2%
- Pengiriman data via MQTT ke gateway
- Penyimpanan data ke database MySQL lokal
- Forward data ke server MQTT 
- Dashboard terminal untuk melihat data real-time
- (Opsional) Analisis performa motor untuk prediksi maintenance

## 📂 Struktur Proyek

├── node.py 
├── gateway.py 
├── read_data.py 
├── predict.py 
├── database/
│ └── mydb_local.sql 
├── data/
│ └── sensor_data_month.csv
├── diagram/
│ ├── schematic_diagram.png
│ ├── wiring_diagram.png
│ ├── flowchart_node.png
│ └── flowchart_gateway.png
