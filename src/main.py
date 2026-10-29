from data_io import baca_data_file
from analisis import hitung_statistik, tentukan_status
from utilitas import validasi_nilai

def main():
    print("=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA ===")
    path = "data/nilai_contoh.txt"
    data_mentah = baca_data_file(path)
    
    if not data_mentah:
        print("Tidak ada data untuk diproses.")
        return
    
    list_nilai = []
    for nim, info in data_mentah.items():
        valid, nilai = validasi_nilai(info["nilai"])
        if valid:
            list_nilai.append(nilai)
            status = tentukan_status(nilai)
            print(f"NIM: {nim} | Nama: {info['nama']} | Nilai: {nilai} | Status: {status}")
        else:
            print(f"NIM: {nim} | Data nilai tidak valid.")
            
    if list_nilai:
        rata, mini, maksi = hitung_statistik(list_nilai)
        print("\n--- STATISTIK KELAS ---")
        print(f"Rata-rata Kelas : {rata:.2f}")
        print(f"Nilai Minimum   : {mini}")
        print(f"Nilai Maksimum  : {maksi}")

if __name__ == "__main__":
    main()