# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas[cite: 36]

## 2. Latar Belakang
Guru matematika sering kali membutuhkan waktu yang tidak sedikit untuk merekap nilai ujian siswa secara manual, menghitung rata-rata kelas, menentukan siswa yang tuntas maupun belum tuntas berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyusun laporan ringkas. Oleh karena itu, diperlukan program konsol berbasis Python yang dapat mengotomatisasi proses pembacaan data, validasi, perhitungan statistik, dan penyimpanan laporan secara cepat dan konsisten[cite: 31, 36].

## 3. Pengguna dan Tujuan
- **Pengguna Utama**: Guru Matematika[cite: 31, 36].
- **Tujuan**: Mempermudah rekapitulasi nilai, perhitungan statistik kelas, penentuan status ketuntasan, dan pembuatan laporan secara otomatis[cite: 31, 36].

## 4. Ruang Lingkup
- **Fitur Wajib**:
  1. Membaca data dari file teks[cite: 36].
  2. Memvalidasi rentang nilai (0 - 100) dan format baris[cite: 36].
  3. Menghitung statistik (rata-rata, nilai minimum, dan nilai maksimum)[cite: 36].
  4. Menentukan status kelulusan/ketuntasan berdasarkan KKM[cite: 36].
  5. Menyimpan laporan hasil rekap ke dalam file teks baru[cite: 36].
- **Batasan**: Program dijalankan melalui terminal/console berbasis Python tanpa antarmuka grafis (GUI/Web)[cite: 30, 31].

## 5. Analisis Kebutuhan
### User Story
> "Sebagai guru matematika, saya ingin memasukkan atau membaca data nilai siswa melalui file, agar saya dapat memperoleh statistik dan status ketuntasan secara otomatis."

### Kebutuhan Fungsional
- **F01**: Program dapat membaca data nilai dari file.
- **F02**: Program dapat memvalidasi nilai angka berada pada rentang 0-100[cite: 31].
- **F03**: Program menghitung rata-rata, minimum, dan maksimum kelas[cite: 31].
- **F04**: Program menentukan status tuntas / belum tuntas[cite: 31].
- **F05**: Program menyimpan laporan ringkas ke file eksternal[cite: 31].

## 6. Spesifikasi Input, Proses, dan Output (IPO)
- **Input**: File teks (`nilai_contoh.txt`) yang berisi NIM, Nama, dan Nilai[cite: 32].
- **Proses**: Membaca baris, memvalidasi data, menyimpan ke struktur data dictionary/list, menghitung statistik matematika, serta mengklasifikasikan ketuntasan[cite: 32].
- **Output**: Menampilkan ringkasan statistik di terminal dan menulis laporan ke file teks (`laporan_rekap.txt`)[cite: 32].

## 7. Algoritma dan Pseudocode Alur Utama
```text
MULAI
1. Baca data dari file path
2. Jika file tidak ditemukan:
     Tampilkan pesan error FileNotFoundError dan hentikan program
3. Untuk setiap baris dalam file:
     Bersihkan spasi (strip) dan validasi format
     Jika valid, simpan ke struktur data
4. Hitung statistik (rata-rata, min, max) dari data valid
5. Tentukan status ketuntasan berdasarkan KKM
6. Tampilkan ringkasan hasil ke layar terminal
7. Simpan laporan ke file keluaran
SELESAI