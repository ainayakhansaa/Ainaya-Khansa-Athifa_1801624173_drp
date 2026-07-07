"""
mood_analysis.py

Menganalisis data mood yang telah tersimpan.
"""

from collections import Counter
from manager import database_manager as db


def analisis_mood():
    """Menganalisis riwayat mood pengguna."""

    history = db.load_history()

    if not history:
        print("\nBelum ada data mood untuk dianalisis.")
        return None

    # Ambil semua mood dan skor
    daftar_mood = [item["mood"] for item in history]
    daftar_skor = [item["skor"] for item in history]

    # Mood yang paling sering muncul
    frekuensi = Counter(daftar_mood)
    mood_terbanyak = frekuensi.most_common(1)[0]

    # Rata-rata skor
    rata_skor = sum(daftar_skor) / len(daftar_skor)

    # Menentukan kondisi mood
    if rata_skor >= 4:
        kondisi = "Positif 😊"
    elif rata_skor >= 2.5:
        kondisi = "Netral 😐"
    else:
        kondisi = "Negatif 😔"

    print("\n" + "=" * 50)
    print("           ANALISIS MOOD")
    print("=" * 50)
    print(f"Total Data        : {len(history)}")
    print(f"Mood Terbanyak    : {mood_terbanyak[0]} ({mood_terbanyak[1]} kali)")
    print(f"Rata-rata Skor    : {rata_skor:.2f}")
    print(f"Kondisi Emosi     : {kondisi}")
    print("=" * 50)

    return {
        "total_data": len(history),
        "mood_terbanyak": mood_terbanyak[0],
        "jumlah": mood_terbanyak[1],
        "rata_skor": rata_skor,
        "kondisi": kondisi
    }