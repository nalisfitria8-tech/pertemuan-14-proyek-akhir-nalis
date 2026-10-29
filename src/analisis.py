def hitung_statistik(data_nilai):
    """Menghitung rata-rata, minimum, dan maksimum dari sekumpulan nilai."""
    if not data_nilai:
        return 0, 0, 0
    rata = sum(data_nilai) / len(data_nilai)
    minimal = min(data_nilai)
    maksimal = max(data_nilai)
    return rata, minimal, maksimal

def tentukan_status(nilai, kkm=60):
    """Menentukan status tuntas atau belum tuntas berdasarkan KKM."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"