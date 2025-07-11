import pandas as pd
import matplotlib.pyplot as plt

# Baca data CSV hasil monitoring 1 bulan
df = pd.read_csv("data/sensor_data_month.csv")

# Definisi kondisi normal motor:
# - Voltage: 219 – 221 V
# - Temperature: 24 – 25 °C
def is_normal(row):
    return 219.0 <= row["voltage"] <= 221.0 and 24.0 <= row["temperature"] <= 25.0

# Tandai kondisi tiap data
df["is_normal"] = df.apply(is_normal, axis=1)

# Hitung statistik
total = len(df)
normal_count = df["is_normal"].sum()
abnormal_count = total - normal_count

normal_pct = round(normal_count / total * 100, 2)
abnormal_pct = round(abnormal_count / total * 100, 2)

# Estimasi penurunan lifetime:
# Misal: setiap 10% abnormal menyebabkan 10% penurunan lifetime
lifetime_drop = round((abnormal_pct / 100) * 10, 2)

# Tampilkan hasil
print("=== PREDIKSI PERFORMA MOTOR ===")
print(f"Total data               : {total}")
print(f"Jumlah kondisi NORMAL    : {normal_count} data ({normal_pct}%)")
print(f"Jumlah kondisi ABNORMAL  : {abnormal_count} data ({abnormal_pct}%)")
print(f"Estimasi penurunan lifetime bulan ini: {lifetime_drop}%")

# Visualisasi
plt.figure(figsize=(6,4))
plt.bar(["Normal", "Abnormal"], [normal_count, abnormal_count], color=["green", "red"])
plt.title("Distribusi Kondisi Motor dalam 1 Bulan")
plt.ylabel("Jumlah Data")
plt.tight_layout()
plt.show()

with open("report/prediksi_performa_motor.txt", "w") as f:
    f.write("PREDIKSI PERFORMA MOTOR\n")
    f.write("------------------------\n\n")
    f.write("Tanggal Analisis     : 11 Juli 2025\n")
    f.write("Periode Data         : 1 Juni 2025 – 30 Juni 2025\n")
    f.write(f"Total Data           : {total} (1 data per menit)\n\n")
    f.write("Kriteria Motor Normal:\n")
    f.write("- Voltage     : 219 V – 221 V\n")
    f.write("- Temperature : 24 °C – 25 °C\n\n")
    f.write("Hasil Analisis:\n")
    f.write("----------------\n")
    f.write(f"Jumlah Kondisi NORMAL    : {normal_count} data ({normal_pct}%)\n")
    f.write(f"Jumlah Kondisi ABNORMAL  : {abnormal_count} data ({abnormal_pct}%)\n\n")
    f.write("Estimasi Penurunan Lifetime:\n")
    f.write("----------------------------\n")
    f.write("Sesuai asumsi bahwa:\n")
    f.write("- Setiap 10% data abnormal berkontribusi pada 10% penurunan lifetime\n\n")
    f.write(f"→ Estimasi penurunan lifetime bulan ini: {lifetime_drop}%\n\n")
    f.write("Kesimpulan:\n")
    f.write("-----------\n")
    f.write("Motor berjalan dalam kondisi cukup stabil dengan mayoritas data menunjukkan kondisi normal.\n")
    f.write("Namun demikian, terdapat {:.2f}% data abnormal yang menunjukkan adanya potensi penyimpangan,\n".format(abnormal_pct))
    f.write("maka perlu dilakukan monitoring berkala untuk mencegah kerusakan jangka panjang.\n\n")
    f.write("Disusun oleh:\nRaudhafilhaq Alfitrah\n")
