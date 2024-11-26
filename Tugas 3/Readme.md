# Membuat Docker
Untuk menginstal web server berbasis Docker dengan dukungan HTTP/1.1, HTTP/2.0, dan HTTP/3.0, mengaksesnya melalui website, dan menganalisis http yang digunakan, berikut langkah-langkahnya:

---

### 1. **Persiapan Lingkungan**

- Pastikan Docker telah terinstal di sistem Anda.
- Unduh dan instal browser versi terbaru.

---

### 2. **Konfigurasi Docker untuk Web Server**

Kita akan menggunakan **NGINX** sebagai contoh web server karena mendukung HTTP/1.1, HTTP/2, dan HTTP/3.

#### a. **Buat File Docker Compose**

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
#### 3.1 Aktifkan run.docker.sh
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
## What is this?
[![Docker Image CI](https://github.com/macbre/docker-nginx-http3/actions/workflows/dockerimage.yml/badge.svg)](https://github.com/macbre/docker-nginx-http3/actions/workflows/dockerimage.yml)

Stable and up-to-date [nginx](https://nginx.org/en/CHANGES) with [QUIC + HTTP/3 support](https://nginx.org/en/docs/http/ngx_http_v3_module.html), [Google's `brotli` compression](https://github.com/google/ngx_brotli), [`zstd` compression](https://github.com/tokers/zstd-nginx-module), [`njs` module](https://nginx.org/en/docs/njs/), [kTLS/sendfile support](https://delthas.fr/blog/2023/kernel-tls/) and [Grade A+ SSL config](https://ssl-config.mozilla.org/)

## How to use this image
As this project is based on the official [nginx image](https://hub.docker.com/_/nginx/) look for instructions there. In addition to the standard configuration directives, you'll be able to use the brotli module specific ones, see [here for official documentation](https://github.com/google/ngx_brotli#configuration-directives)

```
docker pull macbre/nginx-http3:latest
```

You can fetch an image from [Github Containers Registry](https://github.com/macbre/docker-nginx-brotli/pkgs/container/nginx-http3) as well:

```
docker pull ghcr.io/macbre/nginx-http3:latest
```

## What's inside

* [built-in nginx modules](https://nginx.org/en/docs/)
* [`headers-more-nginx-module`](https://github.com/openresty/headers-more-nginx-module#readme) - sets and clears HTTP request and response headers
* [`ngx_brotli`](https://github.com/google/ngx_brotli#configuration-directives) - adds [brotli response compression](https://datatracker.ietf.org/doc/html/rfc7932)
* [`zstd-nginx-module`](https://github.com/tokers/zstd-nginx-module#directives) - adds [Zstandard response compression](https://datatracker.ietf.org/doc/html/rfc8878)
* [`ngx_http_geoip2_module`](https://github.com/leev/ngx_http_geoip2_module#download-maxmind-geolite2-database-optional) - creates variables with values from the maxmind geoip2 databases based on the client IP
* [`njs` module](https://nginx.org/en/docs/njs/) - a subset of the JavaScript language that allows extending nginx functionality ([GitHub repository](https://github.com/nginx/njs))

```
$ docker run -it macbre/nginx-http3 nginx -V
nginx version: nginx/1.27.2 (331eae3dccf8)
built by gcc 13.2.1 20240309 (Alpine 13.2.1_git20240309) 
built with OpenSSL 3.3.2 3 Sep 2024
TLS SNI support enabled
configure arguments: 
	--build=331eae3dccf8
	--prefix=/etc/nginx 
	--sbin-path=/usr/sbin/nginx 
	--modules-path=/usr/lib/nginx/modules 
	--conf-path=/etc/nginx/nginx.conf 
	--error-log-path=/var/log/nginx/error.log 
	--http-log-path=/var/log/nginx/access.log 
	--pid-path=/var/run/nginx/nginx.pid 
	--lock-path=/var/run/nginx/nginx.lock 
	--http-client-body-temp-path=/var/cache/nginx/client_temp 
	--http-proxy-temp-path=/var/cache/nginx/proxy_temp 
	--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp 
	--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp 
	--http-scgi-temp-path=/var/cache/nginx/scgi_temp 
	--user=nginx 
	--group=nginx 
	--with-http_ssl_module 
	--with-http_realip_module 
	--with-http_addition_module 
	--with-http_sub_module 
	--with-http_dav_module 
	--with-http_flv_module 
	--with-http_mp4_module 
	--with-http_gunzip_module 
	--with-http_gzip_static_module 
	--with-http_random_index_module 
	--with-http_secure_link_module 
	--with-http_stub_status_module 
	--with-http_auth_request_module 
	--with-http_xslt_module=dynamic 
	--with-http_image_filter_module=dynamic 
	--with-http_geoip_module=dynamic 
	--with-http_perl_module=dynamic 
	--with-threads 
	--with-stream 
	--with-stream_ssl_module 
	--with-stream_ssl_preread_module 
	--with-stream_realip_module 
	--with-stream_geoip_module=dynamic 
	--with-http_slice_module 
	--with-mail 
	--with-mail_ssl_module 
	--with-compat 
	--with-file-aio 
	--with-http_v2_module 
	--with-http_v3_module
	--with-openssl-opt=enable-ktls
	--add-module=/usr/src/ngx_brotli 
	--add-module=/usr/src/headers-more-nginx-module-0.37 
	--add-module=/usr/src/njs/nginx 
	--add-module=/usr/src/zstd
	--add-dynamic-module=/usr/src/ngx_http_geoip2_module
	--with-cc-opt='-g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -I /usr/src/quickjs'
	--with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -L /usr/src/quickjs'

$ docker run -it macbre/nginx-http3 njs -v
0.8.7
```

## SSL Grade A+ handling

Please refer to [Mozilla's SSL Configuration Generator](https://ssl-config.mozilla.org/). This image has `https://ssl-config.mozilla.org/ffdhe2048.txt` DH parameters for DHE ciphers fetched and stored in `/etc/ssl/dhparam.pem`:

```
    ssl_dhparam /etc/ssl/dhparam.pem;
```

See [ssllabs.com test results for wbc.macbre.net](https://www.ssllabs.com/ssltest/analyze.html?d=wbc.macbre.net).

## nginx config files includes

* `.conf` files mounted in `/etc/nginx/main.d` will be included in the `main` nginx context (e.g. you can call [`env` directive](http://nginx.org/en/docs/ngx_core_module.html#env) there)
* `.conf` files mounted in `/etc/nginx/conf.d` will be included in the `http` nginx context

## QUIC + HTTP/3 support

<img width="577" alt="Screenshot 2021-05-19 at 16 31 10" src="https://user-images.githubusercontent.com/1929317/118840921-baf7d300-b8bf-11eb-8c0f-e57d573a28ce.png">

Please refer to `tests/https.conf` config file for an example config used by the tests. And to Cloudflare docs on [how to enable http/3 support in your browser](https://developers.cloudflare.com/http3/firefox).

```
server {
    # http/3
    listen 443 quic reuseport;

    # http/2 and http/1.1
    listen 443 ssl;
    http2 on;

    server_name localhost;  # customize to match your domain

    # you need to mount these files when running this container
    ssl_certificate     /etc/nginx/ssl/localhost.crt;
    ssl_certificate_key /etc/nginx/ssl/localhost.key;

    # TLSv1.3 is required for QUIC.
    ssl_protocols TLSv1.2 TLSv1.3;

    # 0-RTT QUIC connection resumption
    ssl_early_data on;

    # Add Alt-Svc header to negotiate HTTP/3.
    add_header alt-svc 'h3=":443"; ma=86400';

    # Sent when QUIC was used
    add_header QUIC-Status $http3;

    location / {
        # your config
    }
}
```

Refer to `run-docker.sh` script on how to run this container and properly mount required config files and assets.

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

1. **Tempatkan Semua File di Folder yang Sama**: Pastikan `index.html`, `style.css`, `script.js`, dan `image.png` berada di direktori yang sama.
    
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
akan ditampilkan pada gambar
