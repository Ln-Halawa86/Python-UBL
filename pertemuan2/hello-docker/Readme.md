Pada Meeting 2
- melakukan instal docker
after instal docker and then you can using code under :
- you using teriminal visual studio code 
==========================================================
1. Membuat Docker Image:
docker build -t hello-python .

2. Menjalankan Container:
docker run hello-python

3. Cara Melihat Hasil Build (Docker Image):
docker images

4. Membangun ulang (build) image Docker terlebih dahulu, kemudian menjalankan semua service yang didefinisikan di file docker-compose.yml:
docker-compose up –build

5. Membuat dan menjalankan semua service yang didefinisikan di file docker-compose.yml, lalu menjalankannya di background:
docker-compose up -d

6. Menjalankan Aplikasi Tambah Data:
docker-compose run app python tambah_data.py

7. Menjalankan Aplikasi Tampil Data:
docker-compose run app python tampil_data.py

8. Menghapus Image Berdasarkan Nama Image:
docker rmi hello-python

9. Membersihkan Semua Resource Docker:
docker-compose down --rmi all -v
