## Penjelasan DNS (Domain Name System)

Pengertian DNS: DNS (Domain Name System) adalah sistem yang digunakan untuk menerjemahkan nama domain yang mudah diingat oleh manusia (seperti www.example.com) menjadi alamat IP yang digunakan oleh komputer dan perangkat lain untuk berkomunikasi melalui jaringan, seperti internet. Tanpa DNS, kita harus mengingat alamat IP numerik setiap kali mengakses sebuah situs web.

##   Cara Kerja DNS:

### 1. Permintaan DNS: Ketika pengguna memasukkan alamat situs web di browser, seperti "www.example.com", browser mengirimkan permintaan ke server DNS.
### 2. Pencarian Alamat IP: Server DNS kemudian mencari nama domain tersebut dalam basis data mereka untuk menemukan alamat IP yang sesuai. Jika alamat IP ditemukan, server DNS akan mengembalikannya ke browser.
### 3. Pencarian Rekursif atau Iteratif: Jika server DNS tidak dapat menemukan alamat IP di basis data lokalnya, permintaan tersebut akan diteruskan ke server DNS lain yang lebih tinggi dalam hierarki, hingga menemukan server yang memiliki informasi yang diperlukan.

## Bagaimana DNS Bekerja:

Resolusi Nama: DNS menyimpan informasi dalam bentuk database yang terdiri dari catatan atau "record". Misalnya, catatan A (A record) menyimpan alamat IP dari domain tertentu, sedangkan catatan MX (Mail Exchange) menyimpan informasi terkait server email.
Hierarki DNS: DNS bekerja berdasarkan sistem hierarki, yang terdiri dari beberapa level:
### 1. Root DNS Servers: Server yang mengarahkan permintaan ke domain tingkat atas.
### 2. TLD (Top Level Domain) Servers: Server yang menangani domain tingkat atas seperti .com, .org, .net, dan sebagainya.
### 4. Authoritative DNS Servers: Server yang memiliki informasi paling akurat dan terupdate mengenai domain tertentu.

## Berikut Alur Kerja Berdasarkan Desain DNS berikut :
 ![alt text](https://github.com/MNURRIZAPAHLEVI/Jaringan/blob/main/DNS/DNS.drawio.png?raw=true)

 -  Nama Domain: Nama yang mudah diingat oleh manusia untuk mengidentifikasi sebuah website atau layanan online.
 -  Alamat IP: Alamat numerik unik yang diberikan kepada setiap perangkat yang terhubung ke internet.
 -  DNS Resolver: Program yang menjalankan permintaan DNS dan menyimpan cache hasil pencarian.
 -  Root Server: Server tingkat atas yang menyimpan daftar semua TLD (Top-Level Domain) server.
 -  TLD Server: Server yang menyimpan informasi tentang domain tingkat atas (misalnya, .com, .org, .net).
 -  Server: Server yang menyimpan informasi tentang domain tingkat rendah (misalnya, www.example.com).
 -  
# Alur Proses
1. Pengguna Memasukkan Nama Domain: Pengguna mengetikkan nama domain (misalnya, example.com) ke dalam browser.
2. Permintaan ke DNS Resolver: Browser mengirimkan permintaan DNS ke DNS resolver lokal (biasanya disediakan oleh ISP).
3. DNS Resolver Memeriksa Cache: DNS resolver memeriksa cache-nya untuk melihat apakah sudah memiliki alamat IP untuk nama domain tersebut. Jika ada, DNS resolver akan langsung mengembalikan alamat IP ke browser.
4. Permintaan ke Root Server: Jika tidak ditemukan di cache, DNS resolver mengirimkan permintaan ke salah satu root server untuk mendapatkan informasi tentang TLD server untuk .com.
5.Root Server Menjawab TLD Server: Root server merespons dengan memberikan alamat IP dari TLD server untuk .com.
6. Permintaan ke TLD Server: DNS resolver kemudian mengirimkan permintaan ke TLD server .com untuk mendapatkan informasi tentang nama domain example.
7. TLD Server Menjawab Server: TLD server merespons dengan memberikan alamat IP dari server yang mengelola domain example.com.
8. DNS Resolver Menyimpan di Cache: DNS resolver menyimpan hasil pencarian ini di cache-nya untuk permintaan di masa mendatang.
9. DNS Resolver Mengembalikan Alamat IP: DNS resolver mengembalikan alamat IP yang ditemukan ke browser.
10. Browser Mengakses Server: Browser menggunakan alamat IP yang diberikan untuk terhubung ke server yang sesuai dan memuat halaman web.

# Jenis Kueri
- Recursive Query: DNS resolver terus meneruskan permintaan hingga menemukan jawaban yang pasti atau kehabisan sumber daya.
- Iterative Query: DNS resolver hanya meneruskan permintaan ke server berikutnya dan menunggu respons sebelum melanjutkan.

# Manfaat DNS
- Kemudahan Pengguna: Pengguna tidak perlu mengingat deretan angka yang rumit (alamat IP) untuk mengakses website.
- Efisiensi: DNS resolver menyimpan hasil pencarian di cache, sehingga mengurangi waktu yang dibutuhkan untuk menyelesaikan permintaan DNS berulang.
- Skalabilitas: Sistem DNS didesain untuk menangani jutaan permintaan DNS setiap detik.

#### Kesimpulan
Sistem DNS berperan sangat penting dalam infrastruktur internet. Dengan menerjemahkan nama domain menjadi alamat IP, DNS memungkinkan pengguna mengakses internet dengan mudah dan cepat. Alur proses yang melibatkan berbagai server dan jenis kueri memastikan bahwa sistem ini dapat menangani permintaan DNS yang sangat besar dan kompleks.
