import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Kepegawaian"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pegawai ORDER BY NIP")

myresult = mycursor.fetchall()

print("\nDATA PEGAWAI")
print("-" * 30)

for data in myresult:
  NIP=data[0]
  Nama=data[1]
  print(NIP+" "+Nama)