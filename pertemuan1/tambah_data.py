import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kepegawaian"
)

Nip=input("Masukkan NIP   : ")
Nama=input("Masukkan Nama  : ")

mycursor = mydb.cursor()

sql = "INSERT INTO pegawai (NIP, Nama) VALUES (%s, %s)"
val = (Nip, Nama)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil disimpan.")