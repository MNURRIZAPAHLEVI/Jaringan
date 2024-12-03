### SMTP (Simple Mail Transfer Protocol) 

SMTP adalah protokol yang digunakan untuk mengirimkan email antar server di internet. SMTP memungkinkan pengiriman pesan dari email client (seperti Outlook, Gmail, atau Thunderbird) ke server email dan antar server email untuk menyampaikan pesan ke penerima yang dituju.
SMTP bekerja dengan sistem antrian, di mana email yang dikirim akan diproses dan diserahkan ke server tujuan hingga mencapai inbox penerima.

Berikut Contoh Desain SMTP


 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/SMTP/Simple-Mail-Transfer-Protocol-1.png?raw=true)

 Alur Pengiriman Email Melalui SMTP dan POP3/IMAP

 # Pemahaman Dasar
- SMTP (Simple Mail Transfer Protocol): Protokol yang digunakan untuk mengirim email dari satu server ke server lainnya.
- POP3 (Post Office Protocol 3): Protokol yang digunakan untuk mengunduh email dari server ke perangkat klien (misalnya, komputer, smartphone). Email yang sudah diunduh biasanya dihapus dari server.
- IMAP (Internet Message Access Protocol): Protokol yang juga digunakan untuk mengakses email di server, tetapi dengan fleksibilitas yang lebih tinggi. Email dapat diakses, dikelola, dan dihapus baik di server maupun di perangkat klien.

# Alur Proses Pengiriman Email
1. Pengguna Membuat Email: Pengguna membuat email baru menggunakan aplikasi email (misalnya, Outlook, Gmail) dan menekan tombol kirim.
2. Email Dikirim ke Server Pengirim: Aplikasi email akan mengirimkan email tersebut ke server email pengirim (Sender's Mail Server) menggunakan protokol SMTP.
3. Server Pengirim Mentransfer Email: Server pengirim akan meneruskan email tersebut ke server email penerima (Receiver's Mail Server) melalui internet, juga menggunakan protokol SMTP.
4. Server Penerima Menerima Email: Server penerima akan menerima email dan menyimpannya di kotak masuk penerima.
5. Pengguna Mengunduh Email: Pengguna penerima kemudian dapat mengakses emailnya menggunakan aplikasi email yang terhubung ke server penerima melalui protokol POP3 atau IMAP.
- POP3: Email akan diunduh dan biasanya dihapus dari server.
- IMAP: Email tetap berada di server, dan pengguna dapat mengakses, mengelola, dan menghapusnya dari berbagai perangkat.

# Keuntungan Menggunakan SMTP, POP3, dan IMAP
- Standarisasi: Protokol ini sudah menjadi standar industri, sehingga email dapat dikirim dan diterima antar berbagai sistem email.
- Fleksibilitas: IMAP memberikan fleksibilitas yang lebih tinggi dalam mengelola email, memungkinkan pengguna untuk mengakses email dari berbagai perangkat.
- Keamanan: Implementasi modern dari protokol ini biasanya dilengkapi dengan enkripsi untuk melindungi privasi email.
