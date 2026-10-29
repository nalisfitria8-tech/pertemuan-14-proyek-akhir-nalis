def validasi_nilai(teks_nilai):
    """Memeriksa apakah nilai berupa angka dan berada di rentang 0 - 100."""
    try:
        nilai = float(teks_nilai)
        if 0 <= nilai <= 100:
            return True, nilai
        return False, None
    except ValueError:
        return False, None