# Tugas 2 : Analisis Koneksi TCP Menggunakan Wireshark

## Deskripsi Singkat

Pada tugas ini, saya melakukan analisis terhadap komunikasi TCP antara client dan server berdasarkan sample capture Wireshark yang diberikan, yaitu file **http.cap**. dari sample capture ini, analisis dilakukan untuk mengamati alur komunikasi mulai dari Connection establishment using three-way handshaking, Data Transfer dan Connection termination using three-way handshaking.

Dari **43 paket** yang tercatat dalam file capture **http.cap**,  hanya **34 paket** yang berhasil diproses dalam komunikasi TCP yang melibatkan client dan server.


## TCP Sequence Diagram

**1. Connection Establishment (Three-way handshaking)**

- **Client** mengirimkan paket **SYN** untuk memulai koneksi
- **Server** merespon dengan paket **SYN + ACK** untuk mengkonfirmasi penerimaan dan siap berkomunikasi
- **Client** kemudian mengirimkan **ACK** untuk menyelesaikan handshake dan membuka koneksi
- tahap ini digambarkan pada TCP Sequence diagram dimulai dari step 1-3.

**2. Data Transfer** 

- **Step 4: PSH + ACK**
   Seq = 1, Ack = 1. Client mengirimkan 479 byte data.

- **Step 5: ACK**
   Seq = 1, Ack = 480. Server mengonfirmasi penerimaan data yang dikirim oleh client, Ack = 480 menunjukkan bahwa server sudah menerima data hingga byte ke 479 dari client dan mengharapkan data selanjutnya dimulai dari byte 480.

- **Step 6: ACK**
   Seq = 1, Ack = 480. Server mengirimkan 1380 byte data dimulai dari Seq = 1, yang berarti data yang dikirimkan dimulai dari byte ke-1 hingga byte ke-1380.

- **Step 7: ACK**
   Seq = 480, Ack = 1381. Client mengkonfirmasi penerimaan data dari server dengan Ack = 1381, menunjukkan bahwa client sudah menerima semua data hinga byte ke 1380 dari server. Seq = 480 menunjukkan urutan data yang dikirimkan oleh client setelah menerima data dari server.

Proses Data Transfer terus berlanjut hingga Step 30. Data yang dikirimkan akan terus memiliki urutan nomor Sequence yang sesuai, dan Acknowledgment Number dari kedua pihak akan mengonfirmasi bahwa setiap paket diterima dengan benar. Setelah seluruh data terkirim, koneksi akan ditutup dengan paket FIN untuk mengakhiri sesi komunikasi.

**3. Connection termination (three-way handshaking)** 

- **Step 31 :** Server mengirimkan **FIN + ACK** yang menandakan bahwa server ingin menutup koneksi.
- **Step 32 :** Client mengkonfirmasi dengan **ACK**.
- **Step 33 :** Client mengirimkan **FIN + ACK** yang menandakan bahwa client juga ingin menutup koneksi.
- **Step 34 :** server mengkonfirmasi penutupan koneksi dengan **ACK**.
