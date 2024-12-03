### Penjelasan DNS (Domain Name System)

Pengertian DNS: DNS (Domain Name System) adalah sistem yang digunakan untuk menerjemahkan nama domain yang mudah diingat oleh manusia (seperti www.example.com) menjadi alamat IP yang digunakan oleh komputer dan perangkat lain untuk berkomunikasi melalui jaringan, seperti internet. Tanpa DNS, kita harus mengingat alamat IP numerik setiap kali mengakses sebuah situs web.

###   Cara Kerja DNS:

## 1. Permintaan DNS: Ketika pengguna memasukkan alamat situs web di browser, seperti "www.example.com", browser mengirimkan permintaan ke server DNS.
## 2. Pencarian Alamat IP: Server DNS kemudian mencari nama domain tersebut dalam basis data mereka untuk menemukan alamat IP yang sesuai. Jika alamat IP ditemukan, server DNS akan mengembalikannya ke browser.
## 3. Pencarian Rekursif atau Iteratif: Jika server DNS tidak dapat menemukan alamat IP di basis data lokalnya, permintaan tersebut akan diteruskan ke server DNS lain yang lebih tinggi dalam hierarki, hingga menemukan server yang memiliki informasi yang diperlukan.

### Bagaimana DNS Bekerja:

Resolusi Nama: DNS menyimpan informasi dalam bentuk database yang terdiri dari catatan atau "record". Misalnya, catatan A (A record) menyimpan alamat IP dari domain tertentu, sedangkan catatan MX (Mail Exchange) menyimpan informasi terkait server email.
Hierarki DNS: DNS bekerja berdasarkan sistem hierarki, yang terdiri dari beberapa level:
## 1. Root DNS Servers: Server yang mengarahkan permintaan ke domain tingkat atas.
## 2. TLD (Top Level Domain) Servers: Server yang menangani domain tingkat atas seperti .com, .org, .net, dan sebagainya.
## 4. Authoritative DNS Servers: Server yang memiliki informasi paling akurat dan terupdate mengenai domain tertentu.
