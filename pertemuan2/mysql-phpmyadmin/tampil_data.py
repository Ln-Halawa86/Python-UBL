import mysql.connector

# Koneksi ke MySQL (service name: db)
db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="kepegawaian"
)

cursor = db.cursor()

sql = "SELECT nip, nama FROM pegawai"
cursor.execute(sql)

hasil = cursor.fetchall()

print("=== DAFTAR PEGAWAI ===")

if not hasil:
    print("Data pegawai belum ada.")
else:
    for nip, nama in hasil:
        print(f"NIP  : {nip}")
        print(f"Nama : {nama}")
        print("-" * 20)

cursor.close()
db.close()
