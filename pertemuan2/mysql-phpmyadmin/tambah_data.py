import mysql.connector

# Koneksi ke MySQL (service name: db)
db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="kepegawaian"
)

cursor = db.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS pegawai (
    nip VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(100)
)
""")

nip = input("Masukkan NIP  : ")
nama = input("Masukkan Nama : ")

sql = "INSERT INTO pegawai (nip, nama) VALUES (%s, %s)"
val = (nip, nama)

cursor.execute(sql, val)
db.commit()

print("Data berhasil disimpan!")
