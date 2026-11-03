# Portal Penerimaan Mahasiswa Baru (PMB) - Universitas Ma'arif Nahdlatul Ulama Kebumen

Kloning 100% persis dari portal resmi PMB UNU Kebumen:
`https://umnu.siakadcloud.com/spmbfront/`

## 🌟 Fitur & Halaman yang Tersedia

1. **Beranda (`index.html`)**
   - Header lengkap dengan Logo resmi UMNU Kebumen, menu navigasi, pemilih bahasa (ID/EN), dan tombol Masuk.
   - Banner Hero dengan foto kampus resmi UMNU Kebumen dan pesan beasiswa.
   - Filter Pencarian Jalur Pendaftaran interaktif (Jenjang, Program Studi, Sistem Kuliah).
   - Daftar Program Studi (Tab S1 Strata 1 & S2 Strata 2 interaktif).
   - Tata Cara Pendaftaran Mahasiswa Baru (4 langkah panduan).
   - Informasi & Pengumuman lengkap dengan poster beresolusi tinggi.
   - Banner Bantuan "Kami Siap Membantu Anda" & tombol WhatsApp langsung.
   - Footer resmi dengan info kontak (Alamat, Telepon, Email) dan link navigasi.
   - Floating WhatsApp Widget interaktif ("Butuh Bantuan? Hubungi Kami!").
   - Responsif 100% (Desktop, Tablet, dan Mobile dengan hamburger drawer).

2. **Jalur Pendaftaran (`jalur-seleksi.html`)**
   - Menampilkan jalur pendaftaran yang dibuka (Program Internasional, RPL Perolehan SKS, dll.).

3. **Informasi Program Studi (`program-studi.html` & `program-studi-detail-*.html`)**
   - Menampilkan seluruh prodi S1 dan S2 dengan detail masing-masing prodi (Teknik Informatika, Pendidikan Olahraga, Pendidikan Bahasa Inggris, PG-PAUD, Manajemen Haji dan Umroh, dll.).

4. **Informasi & Pengumuman (`pengumuman.html` & `detail-pengumuman-*.html`)**
   - Berisi informasi beasiswa, brosur biaya, cek desil, berkas KIP-K, UKT, dan artikel lengkap.

5. **Masuk Akun (`login.html`)**
   - Halaman login pendaftar dengan input ID Pendaftar & PIN.

6. **Petunjuk Pendaftaran (`user-guide.html`)**
   - Panduan alur pendaftaran PMB.

---

## 🚀 Cara Menjalankan

### Cara 1: Langsung Buka di Browser
Anda dapat langsung membuka file `index.html` di browser apapun (Chrome, Edge, Firefox, dll.).

### Cara 2: Menjalankan Local Web Server
Buka terminal / PowerShell di direktori project:
```bash
# Menggunakan Python
python -m http.server 8080

# Atau menggunakan Node.js
npx serve .
```
Lalu buka di browser: `http://localhost:8080`
