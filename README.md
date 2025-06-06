# Smart Shopping Trolley

![Tampilan Aplikasi](assets/Screenshot%202025-05-05%20235712.png)

Proyek ini bertujuan untuk mengembangkan Smart Shopping Trolley berbasis mikrokontroler yang dirancang untuk mempermudah pengalaman berbelanja di toko atau supermarket. Keranjang belanja ini dilengkapi dengan sensor RFID untuk membaca barang yang dimasukkan, menghitung total harga belanjaan secara otomatis, dan mengirimkan data pembelian ke aplikasi Android milik pembeli. 
Sistem ini menggunakan kombinasi teknologi barcode scanner, sensor RFID, dan komunikasi UART untuk memberikan solusi cerdas yang memungkinkan konsumen memantau total harga belanjaan secara real-time. Dengan konsep ini, konsumen tidak perlu lagi mengantri di kasir, sehingga proses checkout menjadi lebih cepat, efisien, dan nyaman.

## Fitur
- #### Barang Otomatis Terdeteksi :
    Setiap barang yang dimasukkan ke keranjang akan discan menggunakan barcode scanner atau RFID scanner.
- #### Perhitungan Otomatis Total Belanja :
    Setelah barang discan, sistem otomatis menambahkan harga barang ke total belanja.
- #### Koneksi Bluetooth UART ke Android :
    Total belanjaan, daftar barang, dan info lainnya dikirimkan secara real-time via modul Bluetooth (HC-05/HC-06) ke aplikasi Android.
- #### Manajemen Item :
    Di aplikasi Android, pengguna bisa Melihat daftar item belanja dan Menghapus item (fitur cancel jika batal beli barang).
- #### Notifikasi Suara/LED :
    LED indikator dan buzzer berbunyi jika terjadi event penting: Barang baru dimasukkan, Barang dibatalkan, dan Total harga berubah.
- #### Code Qris Pembayaran :
    Konsumen dapat melakukan pembayaran secara langsung melalui code Qris yang telah diinformasikan melalui gadget konsumen.

## Support By
- Dosen Pengampu : Akhmad Hendriawan ST., MT. (NIP.197501272002121003)
- Mata kuliah : Mikrokontroller
- Program Studi : D4 Teknik Elektronika
- Departemen Teknik Elektro
- Politeknik Elektronika Negeri Surabaya

## Team Member :

| NRP        | Nama                   | Jobdesk              | Akun        |
|------------|------------------------|----------------------|-------------|
| 2123600002 | Suci Tri Rahayu        |  Software Developer  | [Suci](https://github.com/sucirhyu)|
| 2123600008 | Samsul Ma'arif         |  Hardware Spesialist | [Samsul](https://github.com/samsul-21)|
| 2123600009 | M. Diki Putra Afandi   |  Project Manager     | [Diki](https://github.com/Muhamaddikiputraafandi)|
| 2123600012 | M. Daniel Prakusye     |  3D Designer         | [Daniel](https://github.com/danielwibowo)|
| 2123600016 | Ibrahim Fansori        |  PCB Designer        | [Ibrahim](https://github.com/IbrahimFansori)  |
| 2123600028 | M. Faqih Zulfikar      |  Software Developer  | [Faqih](https://github.com/faqihzulfi)|

## Preview Video Produk
[![Smart Trolley Video](https://img.youtube.com/vi/qu6nkCT1aYU/0.jpg)](https://youtu.be/qu6nkCT1aYU)

📽️ [Tonton Video Produk](Dokumentasi/Video%20Promotion%20Product%20(1).mp4)

## 🛒 Cara Kerja Smart Trolley
1. Inisialisasi Aplikasi
•	Pengguna membuka aplikasi Smart Trolley.
•	Tersedia dua fitur utama: SCAN dan LIST.

2. Pemindaian Produk
•	Pengguna menekan tombol SCAN NOW untuk memulai pemindaian barcode/QR code produk.
•	Aplikasi mengaktifkan kamera dan membaca kode produk (misalnya: ITEM001).
•	Kode produk dikirim ke Arduino via Bluetooth (HC-06).

3. Pemrosesan di Arduino
•	Arduino menerima kode produk.
•	Mencocokkan kode dengan daftar item yang tersimpan di dalam memori (array).
•	Jika cocok:
    o	Tambahkan ke daftar belanja.
    o	Tampilkan nama & harga produk di OLED.
    o	Aktifkan buzzer sebagai konfirmasi.

4. Detail Produk di Aplikasi
•	Aplikasi menerima informasi barang (nama & harga) dari Arduino via Bluetooth.
•	Menampilkan detail produk.
•	User menekan “Add to Shopping List” → data tersimpan di daftar belanja aplikasi.

5. Daftar Belanja
•	Aplikasi menampilkan seluruh item yang telah dipindai.
•	Total harga ditampilkan secara otomatis.
•	Terdapat tombol Checkout untuk proses pembayaran.
•	(Opsional) User bisa membatalkan item tertentu → aplikasi kirim perintah BATAL ITEMxxx ke Arduino.

6. Pembayaran
•	Setelah checkout, aplikasi menampilkan kode QRIS untuk pembayaran menggunakan dompet digital.
•	User membayar menggunakan aplikasi pembayaran QRIS

7. Sukses Pembayaran
•	Setelah transaksi berhasil:
    o	Aplikasi menampilkan notifikasi "Payment Successful".
    o	Aplikasi mengirim sinyal ke Arduino:
            Menyalakan LED hijau.
            Mengaktifkan relay (misalnya membuka kunci troli/pintu loker sebagai tanda transaksi selesai).

## Foto 3D 
![Desain 3D Smart Trolley](./3D%20Design/Picture%20Desain%203D%20Smart%20Trolley.png)

🔗 [Desain 3D Smart Trolley di Thingiverse](https://www.thingiverse.com/thing:7042336)

## Video Cara pembuatan 3D
📽️ [Tonton Video Panduan Desain 3D](https://intip.in/VIDEOPANDUANDESAIN3D)

## Demo Video Simulasi
🧪 [Klik di sini untuk melihat simulasi Wokwi](https://intip.in/simulasiwokwi)

## Design Figma
[Lihat Desain di Figma](https://www.figma.com/proto/pQICiX3LwqUT9YJWLTK00W/Smart-Trolley?node-id=0-1&t=6SqoGFO5Xu7j4LwM-1)

## Cara Kerja Apklikasi
[Tonton Video Penggunaan Apk](https://github.com/Muhamaddikiputraafandi/ProjectSmartTrolly_TimSTECU/blob/main/UI%20UX%20Design/Figma/Penggunaan%20Apk.mp4)


