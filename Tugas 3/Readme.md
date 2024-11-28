**TUGAS WEBSERVER Dengan Docker**
Untuk menginstal web server berbasis Docker dengan dukungan HTTP/1.1, HTTP/2.0, dan HTTP/3.0, mengaksesnya melalui website, dan menganalisis http yang digunakan, berikut langkah-langkahnya:

---

### 1. **Persiapan Lingkungan**

- Pastikan Docker telah terinstal.
- Unduh dan instal browser versi terbaru.

---

### 2. **Konfigurasi Docker untuk Web Server**

menggunakan **NGINX** sebagai contoh web server karena mendukung HTTP/1.1, HTTP/2, dan HTTP/3.

#### a. **Buat File Docker Compose 1.1 Dan 2.0**

Buat file `docker-compose.yml` dengan konfigurasi berikut:

```yaml
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "8001:80"     # HTTP/1.1
      - "443:443"     # HTTP/2 
    volumes:
      - ./conf.d:/etc/nginx/conf.d
      - ./certs:/etc/nginx/certs
      - ./src:/var/www/

```

#### b. **Buat File Konfigurasi NGINX**

Buat file `default.conf` di dalam direktori  `conf.d`:

```nginx
server {
   listen 80; # HTTP/1.1
   listen 443 ssl http2; # HTTP/2
   listen 443 quic reuseport; # HTTP/3
   ssl_certificate /etc/nginx/certs/server.crt;
   ssl_certificate_key /etc/nginx/certs/server.key;
   ssl_protocols TLSv1.3;
   ssl_prefer_server_ciphers off;
   add_header Alt-Svc 'h3-23=":443"; ma=86400';
   add_header X-Content-Type-Options nosniff;
   root /var/www/;
   index index.html;
}
```

#### c. **Sertifikat SSL**

Buat sertifikat SSL untuk mendukung HTTPS:

```bash
mkdir certs
openssl req -x509 -newkey rsa:2048 -keyout certs/server.key -out certs/server.crt -days 365 -nodes
```

---

### 3. **Jalankan Web Server**

Di terminal, jalankan:

```bash
docker-compose up
```

---
#### 3.1 Tambahan Untuk Aktifkan HTTP 3.0 Aktifkan/Create run.docker.sh
```
#!/bin/sh
sudo docker run --rm \
  -p 0.0.0.0:8888:80 \
  -p 0.0.0.0:8889:443/tcp \
  -p 0.0.0.0:8889:443/udp \
  -v "$PWD/tests":/static:ro \
  -v "$PWD/tests/modules.conf":/etc/nginx/main.d/modules.conf:ro \
  -v "$PWD/tests/perl_rewrite.conf":/etc/nginx/conf.d/perl_rewrite.conf:ro \
  \
  -v "$PWD/tests/static.conf":/etc/nginx/conf.d/static.conf:ro \
  -v "$PWD/tests/https.conf":/etc/nginx/conf.d/https.conf:ro \
  -v "$PWD/ssl_common.conf":/etc/nginx/conf.d/ssl_common.conf:ro \
  \
  -v "$PWD/tests/njs.conf":/etc/nginx/conf.d/njs.conf:ro \
  -v "$PWD/tests/njs":/opt/njs:ro \
  \
  -v "$PWD/tests/localhost.crt":/etc/nginx/ssl/localhost.crt:ro \
  -v "$PWD/tests/localhost.key":/etc/nginx/ssl/localhost.key:ro \
  \
  -v "$PWD/tests/dhparam.pem":/etc/ssl/dhparam.pem:ro \
 --name test_nginx \
  -t macbre/nginx

```
cek konfigurasi
``` sh.run.docker.sh
$ 2024/11/26 16:21:41 [warn] 1#1: "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/localhost.crt"
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/localhost.crt"
172.17.0.1 - - [26/Nov/2024:16:22:42 +0000] "GET / HTTP/2.0" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0" "-" ""
172.17.0.1 - - [26/Nov/2024:16:23:41 +0000] "GET / HTTP/2.0" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0" "-" ""
172.17.0.1 - - [26/Nov/2024:16:23:53 +0000] "GET / HTTP/2.0" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0" "-" ""

```
jika hasil seperti diatas, maka konfigurasi telah berhasil.

### Untuk Lebih Lengkap Seperti Contoh Dibawah Ini##
## Development

Building an image:

```
docker pull ghcr.io/macbre/nginx-http3:latest
DOCKER_BUILDKIT=1 docker build . -t macbre/nginx --cache-from=ghcr.io/macbre/nginx-http3:latest --progress=plain
```

### Docker Compose example

It is necessary to expose both UDP and TCP ports to be able to HTTP/3

```yaml
  nginx:
    image: macbre/nginx-http3
    ports:
      - '443:443/tcp'
      - '443:443/udp' # use UDP for usage of HTTP/3
```

Note: both TCP and UDP HTTP/3 ports needs to be the same

### 4. **Akses di Chrome/mozila**

- Buka Chrome dan akses `http://localhost:8001/ ` untuk HTTP/1.1.
- Gunakan `https://localhost:8889/` untuk HTTPS dengan HTTP/2 dan HTTP/3.

---

### 5. **Pantau Lalu Lintas di Wireshark**

1. Buka Wireshark dan pilih jaringan yang Anda gunakan (misalnya, Wi-Fi atau Ethernet).
2. Gunakan filter:
    - **HTTP/1.1**: `http`
    - **HTTP/2**: `http2` atau `tcp.port==443`
    - **HTTP/3**: `udp.stream eq 2`
3. Akses URL di Chrome/mozila dan amati lalu lintas di Wireshark.

---

### 6. **Verifikasi Versi HTTP di Chrome**

- Buka **Developer Tools** di Chrome (tekan F12).
- Pergi ke tab **Network**.
- Muat ulang halaman dan perhatikan kolom **Protocol** untuk melihat apakah koneksi menggunakan HTTP/1.1, HTTP/2, atau HTTP/3.

Dengan langkah-langkah ini, Anda bisa menjalankan web server NGINX dalam Docker, mengamati perilaku protokol HTTP di browser Chrome, dan menganalisis lalu lintas menggunakan Wireshark.

# Membuat Aplikasi Sederhana
Dengan HTML 
---

---

### **Cara Menjalankan**

1. **Tempatkan Semua File di Folder yang Sama**: Pastikan `index.html`, berada di direktori yang sama.
    
2. **Jalankan Web Server**:
    
    - Gunakan web server seperti **NGINX** yang mendukung HTTP/1.0, HTTP/2.0, dan HTTP/3.0.
    - Pastikan sertifikat SSL sudah diatur untuk mendukung HTTP/2.0 dan HTTP/3.0.
3. **Akses Halaman di Browser**:
    
    - Gunakan Chrome atau browser lain yang mendukung HTTP/2 dan HTTP/3.
    - Buka halaman melalui URL server Anda (misalnya, `http://localhost` atau `https://localhost`).
4. **Amati di Wireshark**:
    
    - Filter protokol untuk melihat lalu lintas HTTP:
        - HTTP/1.0: `http`
        - HTTP/2.0: `http2`
        - HTTP/3.0: `udp.stream eq 2`

---

### Hasil yang Diharapkan
akan ditampilkan pada gambar **Folder Assets**
