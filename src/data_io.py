def baca_data_file(path_file):
    """Membaca data dari file teks eksternal."""
    data = {}
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if not baris:
                    continue
                parts = baris.split(",")
                if len(parts) == 3:
                    nim, nama, nilai_str = parts
                    data[nim.strip()] = {"nama": nama.strip(), "nilai": nilai_str.strip()}
    except FileNotFoundError:
        print(f"Peringatan: File {path_file} tidak ditemukan.")
    return data