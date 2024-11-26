# Tugas 2: Analisis Koneksi TCP dengan Wireshark

## Deskripsi Singkat

Pada tugas ini, saya menganalisis komunikasi TCP antara client dan server berdasarkan sample capture Wireshark yang diberikan, yaitu file **http.cap.** Analisis dilakukan untuk mengamati alur komunikasi yang meliputi tahap Connection Establishment menggunakan three-way handshaking, Data Transfer, dan Connection Termination menggunakan three-way handshaking.

Dari total**43 paket** yang tercatat dalam file **http.cap**, hanya **34 paket** yang berhasil diproses dalam komunikasi TCP yang terjadi antara client dan server.

## Diagram Urutan TCP

**1.Pendirian Koneksi (Three-Way Handshaking)**

- **Client** mengirimkan paket **SYN** untuk proses koneksi.
- **Server** merespons dengan paket **SYN** + **ACK**, menandakan bahwa server menerima permintaan dan siap untuk melanjutkan komunikasi.
- **Client** kemudian mengirimkan **ACK** menyelesaikan proses handshake dan membuka koneksi.
- Tahap ini digambarkan dalam diagram urutan TCP pada langkah 1 hingga 3.

**2. Transfer Data** 

- **Langkah 4: PSH + ACK**
   Seq = 1, Ack = 1. Client mengirimkan 479 byte data.

- **Langkah 5: ACK**
   SSeq = 1, Ack = 480. Server mengonfirmasi penerimaan data dari client, dengan Ack = 480 yang menunjukkan bahwa data hingga byte ke-479 telah diterima dan server siap menerima data berikutnya mulai dari byte 480.

- **Langkah 6: ACK**
   Seq = 1, Ack = 480. Server mengirimkan 1380 byte data mulai dari Seq = 1, yang berarti data dimulai dari byte pertama hingga byte ke-1380.

- **Langkah 7: ACK**
   Seq = 480, Ack = 1381. Client mengonfirmasi penerimaan data dari server dengan Ack = 1381, menandakan bahwa client telah menerima data hingga byte ke-1380 dan siap menerima data berikutnya mulai dari byte ke-1381.

Proses transfer data ini berlanjut hingga langkah ke-30, dengan urutan nomor Sequence dan Acknowledgment Number yang terus disesuaikan untuk memastikan setiap paket data diterima dengan benar. Setelah seluruh data terkirim, koneksi akan ditutup dengan paket FIN untuk mengakhiri sesi komunikasi.

**3.Pengakhiran Koneksi (Three-Way Handshaking)** 

- **Langkah 31:** Server mengirimkan paket **FIN + ACK** yang menandakan keinginan server untuk menutup koneksi..
- **Langkah 32 :** Client merespons dengan paket **ACK** untuk mengonfirmasi penutupan koneksi.
- **Langkah 33 :** Client mengirimkan paket **FIN + ACK** untuk menandakan bahwa client juga ingin menutup koneksi.
- **Langkah 34:** erver mengonfirmasi penutupan koneksi dengan mengirimkan paket **ACK**.
